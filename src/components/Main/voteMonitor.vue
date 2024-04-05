<template>
    <div class="vote-page">
      <NavbarVote></NavbarVote>
      <!-- {{ dateRange }}
      {{ selectDataDateType }} -->
      <!-- {{ chartLoading }} -->
      <b-container class="bv-example-row">
        <b-row class="setting-block">
          <div class="w-100 d-flex flex-column flex-sm-row align-items-center setting-row">
            <div class="mb-2 mb-sm-0">
              <img class="vote-refresh" @click="getVotesData()" src="../../../static/refresh_gray.png">
            </div>
            <ToggleVote class="mb-2 mb-sm-0"  @selectType="handleSelectDataDateType"></ToggleVote>
            <date-range-picker
            class="date-range-picker mb-2 mb-sm-0 ml-sm-2"
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
            <div class="verticle-line d-none d-sm-block"></div>
            <div class="px-3 w-100">
                <Multiselect  class="team-selector mb-2 mb-sm-0" v-model="selectedTeam" :options="team_selector_options" :searchable="false" :close-on-select="false" :show-labels="false"></Multiselect>
            </div>

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
        startDate: new Date(),
        endDate: new Date(),
      },
    };
  },
  methods: {
    handleSelectDataDateType(type) {
      this.selectDataDateType = type;
    },
    formatDate(date) {
      const d = new Date(date);
      let month = `${d.getMonth() + 1}`;
      let day = `${d.getDate()}`;
      const year = d.getFullYear();

      if (month.length < 2) month = `0${month}`;
      if (day.length < 2) day = `0${day}`;

      return [year, month, day].join('-');
    },
    getVotesData() {
      this.chartLoading = true;
      const params = {
        team_target: this.selectedTeam,
        date_type: this.selectDataDateType,
        start_date: this.formatDate(this.dateRange.startDate),
        end_date: this.formatDate(this.dateRange.endDate),
      };

      axios({
        method: 'get',
        url: `${this.$api}/api/intermediate-vote-monitor`,
        params,
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
          start_date: this.formatDate(this.dateRange.startDate),
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
    this.dateRange = {
      startDate: new Date(),
      endDate: new Date(),
    };
    this.getVotesData();
  },
  watch: {
    selectedTeam(newValue, oldValue) {
      this.getVotesData();
    },
    dateRange: {
      handler(val) {
        // do stuff
        this.getVotesData();
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
        const sevenDaysAgo = new Date(new Date().setDate(new Date().getDate() - 7));
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
      this.getVotesData();
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
    width: 100%;
  }
  .date-range-picker {
    /* margin-left: 1rem; */
    width: 15rem;
  }
  .vote-refresh {
    width: 1.5rem;
    height: 1.5rem;
    margin-left: 2rem;
    cursor: pointer;
  }
  </style>
