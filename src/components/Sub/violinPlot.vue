<template>
    <div>
      <Plotly :data="plotData" :layout="plotLayout"/>
    </div>
  </template>

<script>
import axios from 'axios';
import { Plotly } from 'vue-plotly';

export default {
  name: 'App',
  components: {
    Plotly,
  },
  props: {
    predict_result: Object,
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
    updatePlot() {
      const data = this.predict_result.detail_info;
      const plotData = [{
        type: 'violin',
        x: data.map(row => row.label),
        y: data.map(row => row.probability),
        points: 'all',
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
          groups: data.map(row => row.label),
          styles: [
            { target: '聲請方(Plaintiff)', value: { line: { color: '#FEBEDF' } } },
            { target: '雙方(Both)', value: { line: { color: 'orange' } } },
            { target: '相對方(Defendant)', value: { line: { color: '#BEDFFF' } } },
          ],
        }],
      },
        // New trace for mean values
      {
        type: 'scatter',
        mode: 'markers',
        x: ['聲請方(Plaintiff)', '雙方(Both)', '相對方(Defendant)'],
        y: [
          this.predict_result.avg_prob.plaintiff,
          this.predict_result.avg_prob.both,
          this.predict_result.avg_prob.defendant,
        ],
        name: 'Mean',
        marker: {
          size: 5, // Adjust the size for the mean point
          color: '#DE063E', // Choose a color to distinguish mean points
          symbol: 'diamond',
        },
      },
      ];
      const plotLayout = {
        title: {
          text: 'Model-Predicted Probability Distributions <br> of Custody Verdict Outcomes',
          font: {
            size: 16,
          },
        },
        margin: {
          t: 110, // top margin
        //   l: 50, // left margin
        //   r: 50, // right margin
        //   b: 50, // bottom margin
        //   autoexpand: false,
        },
        yaxis: {
          zeroline: false,
        },
        annotations: [
          {
            x: '聲請方(Plaintiff)',
            y: 0.95, // now this is relative to the plot area
            text: `<b>Mean: ${this.predict_result.avg_prob.plaintiff}%<br>Std: ${this.predict_result.std.plaintiff}%</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'bottom', // anchor the bottom of the text
          },
          {
            x: '雙方(Both)',
            y: 0.95, // now this is relative to the plot area
            text: `<b>Mean: ${this.predict_result.avg_prob.both}%<br>Std: ${this.predict_result.std.both}%</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'bottom', // anchor the bottom of the text
          },
          {
            x: '相對方(Defendant)',
            y: 0.95, // now this is relative to the plot area
            text: `<b>Mean: ${this.predict_result.avg_prob.defendant}%<br>Std: ${this.predict_result.std.defendant}%</b>`,
            showarrow: false,
            font: {
              size: 12,
            },
            yref: 'paper', // relative to the plot area
            yanchor: 'bottom', // anchor the bottom of the text
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

