<template>
    <div>
      <Plotly :data="plotData" :layout="plotLayout" :display-mode-bar="false"></Plotly>
    </div>
  </template>

<script>
import { Plotly } from 'vue-plotly';

export default {
  name: 'violinPlotMain',
  components: {
    Plotly,
  },
  props: {
    predict_result: Object,
    model_used: String,
  },
  data() {
    return {
      plotData: [],
      plotLayout: {
        // title: 'Multiple Traces Violin Plot',
        yaxis: {
          zeroline: false,
        },
        annotations: ['hi1', 'hi2', 'hi3'],
      },
    };
  },
  methods: {
    roundToTwo(num) {
      return Math.round((num + Number.EPSILON) * 100) / 100;
    },
    updatePlot() {
      const data = this.predict_result[this.model_used];
      // Initialize empty arrays for x and y
      const x = [];
      const y = [];

      Object.entries(data).forEach(([key, values]) => {
        // 转换 key 并填充到 x 数组
        let transformedKey;
        switch (key) {
          case 'Applicant':
            transformedKey = '判給父親';
            break;
          case 'Respondent':
            transformedKey = '判給母親';
            break;
          case 'Both':
            transformedKey = '判給雙方*';
            break;
          default:
            transformedKey = key;
        }
        x.push(...new Array(values.all_probs.length).fill(transformedKey));

        // 将 y 值乘以 100 并添加到 y 数组
        y.push(...values.all_probs.map(item => item * 100));
      });

      const plotData = [{
        type: 'violin',
        x,
        y,
        // spanmode: 'count',
        width: 0.2,
        // span: [0, 100],
        points: 'all',
        hoverinfo: 'none',
        pointpos: 0, // 將資料點放在中心
        marker: {
          size: 3, // Change the size as needed
        },
        box: {
          visible: false,
        },
        line: {
          color: 'green',
        },
        meanline: {
          visible: true,
        },
        hoveron: 'violins', // 增加這行
        //   hoverinfo: 'none', // 修改這行
        hovertemplate: 'hello<extra></extra>',
        transforms: [{
          type: 'groupby',
          groups: x,
          styles: [
            { target: '判給父親', value: { line: { color: '#FEBEDF' } } },
            { target: '判給雙方*', value: { line: { color: '#FFC48B' } } },
            { target: '判給母親', value: { line: { color: '#BEDFFF' } } },
          ],
        }],
      },
        // New trace for mean values
      {
        type: 'scatter',
        mode: 'markers',
        x: ['判給父親', '判給雙方*', '判給母親'],
        y: [
          this.predict_result[this.model_used].Applicant.avg_prob,
          this.predict_result[this.model_used].Both.avg_prob,
          this.predict_result[this.model_used].Respondent.avg_prob,
        ],
        name: '平均值',
        marker: {
          size: 5, // Adjust the size for the mean point
          color: '#DE063E', // Choose a color to distinguish mean points
          symbol: 'diamond',
        },
      },
      ];
      let left = 0;
      let right = 0;
      if (window.innerWidth <= 768) { // 假设768px为小屏幕与大屏幕的分界点
        left = 0;
        right = 0;
      } else {
      // 大屏幕时的左右边距设置
        left = 50;
        right = 50;
      }
      const plotLayout = {
        responsive: true,
        dragmode: false, // 禁用拖動模式
        xaxis: { fixedrange: true }, // 禁用 x 軸縮放
        yaxis: { fixedrange: true }, // 禁用 y 軸縮放
        title: {
          text: `${this.model_used}模型的預測機率之分佈圖`,
          y: 0.95,
          font: {
            size: 16,
          },
        },
        showlegend: false, // This will hide the legend
        margin: {
          t: 30, // top margin
          l: left, // left margin
          r: right, // right margin
        //   b: 50, // bottom margin
        //   autoexpand: false,
        },
        yaxis: {
          zeroline: false,
        },
        annotations: [
          {
            x: '判給父親',
            y: -0.1, // now this is relative to the plot area
            text: `<b>${this.roundToTwo(this.predict_result[this.model_used].Applicant.avg_prob)}<br>±<br>${this.predict_result[this.model_used].Applicant.std}(%)</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'top', // anchor the top of the text
          },
          {
            x: '判給雙方*',
            y: -0.1, // now this is relative to the plot area
            text: `<b>${this.roundToTwo(this.predict_result[this.model_used].Both.avg_prob)}<br>±<br>${this.predict_result[this.model_used].Both.std}(%)</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'top', // anchor the top of the text
          },
          {
            x: '判給母親',
            y: -0.1, // now this is relative to the plot area
            text: `<b>${this.roundToTwo(this.predict_result[this.model_used].Respondent.avg_prob)}<br>±<br>${this.predict_result[this.model_used].Respondent.std}(%)</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'top', // anchor the top of the text
          },
        ],
      };
      this.plotData = plotData;
      this.plotLayout = plotLayout;
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

