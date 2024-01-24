<template>
    <div id="chart">
        <apexchart type="boxPlot" height="350" :options="chartOptions" :series="series"></apexchart>
    </div>
  </template>

<script>
// import ApexCharts from 'apexcharts';
import VueApexCharts from 'vue-apexcharts';

export default {
  name: 'BoxPlot',
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    predict_result: Object,
    model_used: Array,
  },
  data() {
    return {
      series: [
        {
          data: [
            {
              x: '判給父親(L1)',
              y: [54, 66, 69, 75, 88],
              color: '#FF4560',
            },
            {
              x: '判給父親(L2)',
              y: [43, 65, 69, 76, 81],
            },
            {
              x: '判給母親(L1)',
              y: [31, 39, 45, 51, 59],
            },
            {
              x: '判給母親(L2)',
              y: [39, 46, 55, 65, 71],
            },
            {
              x: '判給雙方(L1)',
              y: [29, 31, 35, 39, 44],
            },
            {
              x: '判給雙方(L2)',
              y: [41, 49, 58, 61, 67],
            },
          ],
        },
      ],
      chartOptions: {
        chart: {
          type: 'boxPlot',
          height: 350,
        },
        title: {
          text: 'Horizontal BoxPlot Chart',
          align: 'left',
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: '50%',
          },
          boxPlot: {
            colors: {
              upper: '#e9ecef',
              lower: '#f8f9fa',
            },
          },
        },
        stroke: {
          colors: ['#6c757d'],
        },
      },


    };
  },
  methods: {
    updatePlot() {
      for (let i = 0; i < this.series[0].data.length; i += 1) {
        const item = this.series[0].data[i];

        if (i == 0) {
          item.x = `判給父親(${this.model_used[0]})`;
          item.y = [this.predict_result[this.model_used[0]].Applicant.min, this.predict_result[this.model_used[0]].Applicant.q1, this.predict_result[this.model_used[0]].Applicant.q2, this.predict_result[this.model_used[0]].Applicant.q3, this.predict_result[this.model_used[0]].Applicant.max];
        } else if (i == 1) {
          item.x = `判給父親(${this.model_used[1]})`;
          item.y = [this.predict_result[this.model_used[1]].Applicant.min, this.predict_result[this.model_used[1]].Applicant.q1, this.predict_result[this.model_used[1]].Applicant.q2, this.predict_result[this.model_used[1]].Applicant.q3, this.predict_result[this.model_used[1]].Applicant.max];
        } else if (i == 2) {
          item.x = `判給母親(${this.model_used[0]})`;
          item.y = [this.predict_result[this.model_used[0]].Respondent.min, this.predict_result[this.model_used[0]].Respondent.q1, this.predict_result[this.model_used[0]].Respondent.q2, this.predict_result[this.model_used[0]].Respondent.q3, this.predict_result[this.model_used[0]].Respondent.max];
        } else if (i == 3) {
          item.x = `判給母親(${this.model_used[1]})`;
          item.y = [this.predict_result[this.model_used[1]].Respondent.min, this.predict_result[this.model_used[1]].Respondent.q1, this.predict_result[this.model_used[1]].Respondent.q2, this.predict_result[this.model_used[1]].Respondent.q3, this.predict_result[this.model_used[1]].Respondent.max];
        } else if (i == 4) {
          item.x = `判給雙方(${this.model_used[0]})`;
          item.y = [this.predict_result[this.model_used[0]].Both.min, this.predict_result[this.model_used[0]].Both.q1, this.predict_result[this.model_used[0]].Both.q2, this.predict_result[this.model_used[0]].Both.q3, this.predict_result[this.model_used[0]].Both.max];
        } else {
          item.x = `判給雙方(${this.model_used[1]})`;
          item.y = [this.predict_result[this.model_used[1]].Both.min, this.predict_result[this.model_used[1]].Both.q1, this.predict_result[this.model_used[1]].Both.q2, this.predict_result[this.model_used[1]].Both.q3, this.predict_result[this.model_used[1]].Both.max];
        }
      }
    },
  },
  watch: {
    async predict_result(newVal, oldVal) {
      // 當 dataSource 改變時，更新 plot
      if (newVal !== oldVal) {
        this.updatePlot();
      }
    },
  },
  async created() {
    this.updatePlot();
    // No need for axios or CSV parsing here, just use the data directly
  },
};
</script>

