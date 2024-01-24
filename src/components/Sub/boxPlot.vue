<template>
    <div ref="boxplot" style="width: 100%;height:400px;"></div>
  </template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'BoxPlot',
  components: {
  },
  props: {
    predict_result: Object,
    model_used: Array,
  },
  mounted() {
    this.createBoxPlot();
  },
  methods: {
    getFakeData() {
      // Generate fake data for demonstration
      function generateBoxplotData() {
        return new Array(6).fill(0).map(() => {
          const values = Array.from({ length: 100 }, () => Math.random() * 100);
          values.sort((a, b) => a - b);
          const q1 = values[Math.floor(values.length / 4)];
          const median = values[Math.floor(values.length / 2)];
          const q3 = values[Math.ceil(values.length * 3 / 4)];
          const iqr = q3 - q1;
          const lower = q1 - 1.5 * iqr;
          const upper = q3 + 1.5 * iqr;
          return [lower, q1, median, q3, upper].map(Math.round);
        });
      }

      return {
        model1: generateBoxplotData().slice(0, 3),
        model2: generateBoxplotData().slice(3, 6),
      };
    },
    createBoxPlot() {
      const boxplotData = this.getData();
      //   const boxplotData = this.getFakeData();
      const chart = echarts.init(this.$refs.boxplot);
      const option = {
        title: {
          text: '模型的預測結果之機率分佈',
          left: 'center',
          textStyle: {
            fontWeight: 'normal', // 或者使用數字，例如 400, 600 等
            fontSize: 17,
            color: '#212529',
          },
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'shadow',
            link: { xAxisIndex: 'all' },
          },
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '15%',
        },
        xAxis: [
          {
            type: 'category',
            data: [`${this.model_used[0]}`, `${this.model_used[1]}`, `${this.model_used[0]}`, `${this.model_used[1]}`, `${this.model_used[0]}`, `${this.model_used[1]}`],
            position: 'bottom',
            axisTick: {
              alignWithLabel: true,
            },
            axisLabel: {
              color: '#212529', // 文字顏色
              fontSize: 15, // 字體大小
            },
            // offset: 30,
          },
          {
            type: 'category',
            data: ['父親贏得親權', '雙方共享親權', '母親贏得親權'],
            // axisTick: {
            //   alignWithLabel: true,
            // },
            position: 'bottom',
            offset: 30,
            axisLabel: {
              color: '##212529', // 文字顏色
              fontSize: 15, // 字體大小
            },
          },

        ],
        yAxis: {
          type: 'value',
          name: '機率 (%)',
        },
        // series: [
        //   {
        //     name: 'Model1 & Model2',
        //     type: 'boxplot',
        //     data: [].concat(boxplotData.model1, boxplotData.model2),
        //     itemStyle: {
        //       borderColor: '#ccc',
        //       borderWidth: 2,
        //     },
        //   },
        // ],
        series: [
          {
            name: `${this.model_used[0]}`,
            type: 'boxplot',
            gridIndex: 0,
            xAxisIndex: 1,
            data: boxplotData.model1,

            itemStyle: {
              normal: {
                color: '#C8B543',
                borderColor: '#737373', // 您可以選擇您喜歡的顏色
                borderWidth: 1,
              },
            },
            boxWidth: [10, 20],
          },
          {
            name: `${this.model_used[1]}`,
            gridIndex: 0,
            xAxisIndex: 1,
            type: 'boxplot',
            data: boxplotData.model2,

            itemStyle: {
              normal: {
                color: '#10A486',
                borderColor: '#737373', // 選擇不同的顏色
                borderWidth: 1,
              },
            },
            boxWidth: [10, 20],
          },
        //   {
        //     name: `${this.model_used[0]}模型預測父親得到親權的機率分佈`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model1.Applicant, boxplotData.model2.Applicant, boxplotData.model1.Respondent, boxplotData.model2.Respondent, boxplotData.model1.Both, boxplotData.model2.Both],
        //   },
        //   {
        //     name: `${this.model_used[0]}-a`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model1.Applicant],
        //   },
        //   {
        //     name: `${this.model_used[1]}-b`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model2.Applicant],
        //   },
        //   {
        //     name: `${this.model_used[0]}模型預測雙方得到親權的機率分佈`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model1.Both],
        //   },
        //   {
        //     name: `${this.model_used[1]}模型預測雙方得到親權的機率分佈`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model2.Both],
        //   },
        //   {
        //     name: `${this.model_used[0]}模型預測母親得到親權的機率分佈`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model1.Respondent],
        //   },
        //   {
        //     name: `${this.model_used[1]}模型預測母親得到親權的機率分佈`,
        //     type: 'boxplot',
        //     xAxisIndex: 0,
        //     data: [boxplotData.model2.Respondent],
        //   },
        ],
      };
      chart.setOption(option);
    },
    getData() {
      const returnData = {
        model1: [[this.predict_result[this.model_used[0]].Applicant.min, this.predict_result[this.model_used[0]].Applicant.q1, this.predict_result[this.model_used[0]].Applicant.q2, this.predict_result[this.model_used[0]].Applicant.q3, this.predict_result[this.model_used[0]].Applicant.max], [this.predict_result[this.model_used[0]].Both.min, this.predict_result[this.model_used[0]].Both.q1, this.predict_result[this.model_used[0]].Both.q2, this.predict_result[this.model_used[0]].Both.q3, this.predict_result[this.model_used[0]].Both.max], [this.predict_result[this.model_used[0]].Respondent.min, this.predict_result[this.model_used[0]].Respondent.q1, this.predict_result[this.model_used[0]].Respondent.q2, this.predict_result[this.model_used[0]].Respondent.q3, this.predict_result[this.model_used[0]].Respondent.max]],
        model2: [[this.predict_result[this.model_used[1]].Applicant.min, this.predict_result[this.model_used[1]].Applicant.q1, this.predict_result[this.model_used[1]].Applicant.q2, this.predict_result[this.model_used[1]].Applicant.q3, this.predict_result[this.model_used[1]].Applicant.max], [this.predict_result[this.model_used[1]].Both.min, this.predict_result[this.model_used[1]].Both.q1, this.predict_result[this.model_used[1]].Both.q2, this.predict_result[this.model_used[1]].Both.q3, this.predict_result[this.model_used[1]].Both.max], [this.predict_result[this.model_used[1]].Respondent.min, this.predict_result[this.model_used[1]].Respondent.q1, this.predict_result[this.model_used[1]].Respondent.q2, this.predict_result[this.model_used[1]].Respondent.q3, this.predict_result[this.model_used[1]].Respondent.max]],
      };
      //   returnData.model1.Applicant = [this.predict_result[this.model_used[0]].Applicant.min, this.predict_result[this.model_used[0]].Applicant.q1, this.predict_result[this.model_used[0]].Applicant.q2, this.predict_result[this.model_used[0]].Applicant.q3, this.predict_result[this.model_used[0]].Applicant.max];

      //   returnData.model1.Respondent = [this.predict_result[this.model_used[0]].Respondent.min, this.predict_result[this.model_used[0]].Respondent.q1, this.predict_result[this.model_used[0]].Respondent.q2, this.predict_result[this.model_used[0]].Respondent.q3, this.predict_result[this.model_used[0]].Respondent.max];

      //   returnData.model1.Both = [this.predict_result[this.model_used[0]].Both.min, this.predict_result[this.model_used[0]].Both.q1, this.predict_result[this.model_used[0]].Both.q2, this.predict_result[this.model_used[0]].Both.q3, this.predict_result[this.model_used[0]].Both.max];

      //   returnData.model2.Applicant = [this.predict_result[this.model_used[1]].Applicant.min, this.predict_result[this.model_used[1]].Applicant.q1, this.predict_result[this.model_used[1]].Applicant.q2, this.predict_result[this.model_used[1]].Applicant.q3, this.predict_result[this.model_used[1]].Applicant.max];

      //   returnData.model2.Respondent = [this.predict_result[this.model_used[1]].Respondent.min, this.predict_result[this.model_used[1]].Respondent.q1, this.predict_result[this.model_used[1]].Respondent.q2, this.predict_result[this.model_used[1]].Respondent.q3, this.predict_result[this.model_used[1]].Respondent.max];

      //   returnData.model2.Both = [this.predict_result[this.model_used[1]].Both.min, this.predict_result[this.model_used[1]].Both.q1, this.predict_result[this.model_used[1]].Both.q2, this.predict_result[this.model_used[1]].Both.q3, this.predict_result[this.model_used[1]].Both.max];

      return returnData;
    },
  },
  watch: {
    async predict_result(newVal, oldVal) {
      // 當 dataSource 改變時，更新 plot
      if (newVal !== oldVal) {
        this.createBoxPlot();
      }
    },
  },
//   async created() {
//     this.createBoxPlot();
//     // No need for axios or CSV parsing here, just use the data directly
//   },
};
</script>

