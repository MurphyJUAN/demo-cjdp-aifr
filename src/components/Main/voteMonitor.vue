<template>
    <div class="vote-page">
      <NavbarVote></NavbarVote>
      <!-- {{ dateRange }}
      {{ selectDataDateType }} -->
      <!-- {{ chartLoading }} -->
      <b-container class="bv-example-row">
        <b-row class="setting-block">
          <div class="w-100 d-inline-flex setting-row">
            <ToggleVote @selectType="handleSelectDataDateType"></ToggleVote>
            <date-range-picker
            class="date-range-picker"
              ref="picker"
              :readonly="isDatePickerReadOnly"
              opens="center"
              :locale-data="{ firstDay: 1, format: 'yyyy-mm-dd' }"
              minDate="2024-04-04T00:00:00.000Z" maxDate="2024-04-23T00:00:00.000Z"
              :singleDatePicker="selectDateMode"
              :timePicker="showTimePicker"
              :timePicker24Hour="showTimePicker24Hour"
              :showWeekNumbers="showWeekNumbers"
              :showDropdowns="showDropdowns"
              :autoApply="autoApply"
              v-model="dateRange"
            >
                <!-- <template v-slot:input="picker" style="min-width: 350px;">
                    {{ picker.startDate | date }} - {{ picker.endDate | date }}
                </template> -->
            </date-range-picker>
            <div class="verticle-line"></div>
            <Multiselect  class="team-selector" v-model="selectedTeam" :options="team_selector_options" :searchable="false" :close-on-select="false" :show-labels="false"></Multiselect>
          </div>
        </b-row>
        <b-row v-if="chartLoading" class="d-flex justify-content-center w-100 mt-3">
            <b-button variant="primary" class="mx-2">
                <b-spinner small></b-spinner>
                <span class="sr-only">Loading...</span>
            </b-button>

            <b-button variant="primary">
                <b-spinner small type="grow"></b-spinner>
                Loading...
            </b-button>
        </b-row>
        <b-row class="">
          <ChartVote :votes_data="votesData"></ChartVote>
        </b-row>
        <b-row v-if="selectDataDateType==='日'" class="d-flex justify-content-center w-100 mt-3">
            <b-button variant="dark" @click="downloadCsv()">下載 csv 檔</b-button>
        </b-row>
      </b-container>

    </div>
  </template>

<script>
import NavbarVote from '../Sub/navbarVote';
import ChartVote from '../Sub/chartVote';
import ToggleVote from '../Sub/toggleVote';
import Multiselect from 'vue-multiselect';
import DateRangePicker from 'vue2-daterange-picker';
import 'vue2-daterange-picker/dist/vue2-daterange-picker.css';
import axios from 'axios';

const today = new Date();
export default {
  components: {
    NavbarVote,
    ChartVote,
    ToggleVote,
    Multiselect,
    DateRangePicker,
  },
  name: 'VoteMonitor',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      loading: true,
      chartLoading: false,
      votesData: [],
      isDatePickerReadOnly: false,
      selectDataDateType: '日',
      selectedTeam: '全部',
      team_selector_options: ['全部', 'Le姊家事商談好夥伴-結合生成式AI與親權判決模型解決親權難題',
        'AI 啟動市民力量-喚醒居住環境共好意識', '協助視障者提升情緒判讀能力弭平社交障礙', '新聞領域展開 — 多元新聞整合平台',
        'SPEAK WITH U 弭平強勢語言帶來的落差: 用生成式AI進行多模態翻譯與方言保存'],
      selectDateMode: 'single',
      showTimePicker: false,
      showTimePicker24Hour: true,
      showWeekNumbers: true,
      showDropdowns: false,
      autoApply: true,
      dateRange: {
        startDate: today,
        endDate: today,
      },
    };
  },
  methods: {
    handleSelectDataDateType(type) {
      this.selectDataDateType = type;
    },
    getVotesData(selectedTeam, selectDataDateType, dateRange) {
      this.chartLoading = true;
      axios({
        method: 'get',
        // url: `${this.$api}/api/predict`,
        url: `${this.$api}/api/intermediate-vote-monitor`,
        params: {
          team_target: selectedTeam,
          date_type: selectDataDateType,
          start_date: dateRange.startDate,
          end_date: dateRange.endDate,
        },
      }).then((res) => {
        this.votesData = res.data;
        this.chartLoading = false;
      }).catch((error) => {
        console.log(error);
        this.chartLoading = false;
      });
    },
    downloadCsv() {
      this.chartLoading = true;
      axios({
        url: `${this.$api}/api/intermediate-vote-download`, // Flask后端提供的下载CSV的API端点
        method: 'GET',
        params: {
          start_date: this.dateRange.startDate,
        },
        responseType: 'blob', // 重要：为了处理二进制文件下载
      }).then((response) => {
        // 创建一个新的Blob对象，使用从服务器收到的数据
        const url = window.URL.createObjectURL(new Blob([response.data]));
        // 创建一个a标签用于下载
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'votes.csv'); // 或者你想要命名的文件名
        document.body.appendChild(link);
        link.click();
        link.remove(); // 完成后移除该元素
        window.URL.revokeObjectURL(url); // 释放URL对象
        this.chartLoading = false;
      }).catch((error) => {
        console.log(error);
        this.chartLoading = false;
      });
    },
  },
  mounted() {
    this.getVotesData(this.selectedTeam, this.selectDataDateType, this.dateRange);
  },
  watch: {
    selectedTeam(newValue, oldValue) {
      this.getVotesData(this.selectedTeam, this.selectDataDateType, this.dateRange);
    },
    dateRange: {
      handler(val) {
        // do stuff
        this.getVotesData(this.selectedTeam, this.selectDataDateType, this.dateRange);
      },
      deep: true,
    },
    selectDataDateType(newValue, oldValue) {
      if (newValue === '日') {
        this.selectDateMode = 'single';
        this.isDatePickerReadOnly = false;
        this.dateRange = {
          startDate: new Date(),
          endDate: new Date(),
        };
      } else if (newValue === '週') {
        this.selectDateMode = 'range';
        this.isDatePickerReadOnly = false;
        const sevenDaysAgo = new Date(today.setDate(today.getDate() - 7));
        const compareDate = new Date('2024-04-04');
        if (sevenDaysAgo < compareDate) {
          sevenDaysAgo.setTime(compareDate.getTime());
        }

        this.dateRange = {
          startDate: sevenDaysAgo,
          endDate: new Date(),
        };
      } else {
        this.selectDateMode = 'range';
        this.isDatePickerReadOnly = true;
        this.dateRange = {
          startDate: '2024-04-04T00:00:00.000Z',
          endDate: '2024-04-23T00:00:00.000Z',
        };
      }
      this.getVotesData(this.selectedTeam, this.selectDataDateType, this.dateRange);
    },
  },
};
</script>

  <style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .vote-page {
    background: white;
    height: 100vh;
  }
  .bg-gray {
    background: gray;
  }
  .verticle-line{
    background: #ECEDEF;
    width: 1px;
    height: 2rem;
    margin-right: 2rem;
    margin-left: 2rem;

  }
  .setting-row {
    justify-content: flex-end;
  }
  .setting-block {
    margin-top: 1rem;
    margin-bottom: 2rem;
  }
  .team-selector {
    width: 40rem;
  }
  .date-range-picker {
    margin-left: 1rem;
    width: 15rem;
  }
  </style>
