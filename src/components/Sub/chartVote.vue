<template>
    <div id="chart" class="w-100">
        <apexchart type="area" height="350" :options="chartOptions" :series="series"></apexchart>
    </div>

</template>

<script>
import VueApexCharts from 'vue-apexcharts';

const team1 = {
  name: 'Team1',
  data: [
    { x: new Date('2024-04-04 00:46:18').getTime(), y: 974 },
    { x: new Date('2024-04-04 00:58:49').getTime(), y: 975 },
    { x: new Date('2024-04-04 01:08:50').getTime(), y: 983 },
    { x: new Date('2024-04-04 01:18:51').getTime(), y: 992 },
  ],
};

const team2 = {
  name: 'Team2',
  data: [
    { x: new Date('2024-04-04 00:46:18').getTime(), y: 456 },
    { x: new Date('2024-04-04 00:58:49').getTime(), y: 472 },
    { x: new Date('2024-04-04 01:08:50').getTime(), y: 475 },
    { x: new Date('2024-04-04 01:18:51').getTime(), y: 490 },
  ],
};

const team3 = {
  name: 'Team3',
  data: [
    { x: new Date('2024-04-04 00:46:18').getTime(), y: 234 },
    { x: new Date('2024-04-04 00:58:49').getTime(), y: 243 },
    { x: new Date('2024-04-04 01:08:50').getTime(), y: 254 },
    { x: new Date('2024-04-04 01:18:51').getTime(), y: 279 },
  ],
};

export default {
  components: {
    apexchart: VueApexCharts,
  },
  name: 'ChartVote',
  props: {
    votes_data: Array,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      series: [team1, team2, team3],
      chartOptions: {
        chart: {
          type: 'area',
          stacked: false,
          height: 350,
          zoom: {
            type: 'x',
            enabled: true,
            autoScaleYaxis: true,
          },
          toolbar: {
            autoSelected: 'zoom',
          },
        },
        dataLabels: {
          enabled: false,
        },
        markers: {
          size: 5,
        },
        title: {
        //   text: 'Stock Price Movement',
          align: 'left',
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100],
          },
        },
        yaxis: {
          title: {
            text: 'Votes',
          },
        },
        xaxis: {
          type: 'datetime',
          labels: {
            datetimeUTC: false, // 根據需要設定此值
            format: 'HH:mm:ss', // 以小時:分鐘:秒的格式顯示
          },
          tooltip: {
            format: 'yyyy-MM-dd HH:mm:ss', // 鼠標懸停時顯示完整的日期和時間
          },
        },
        tooltip: {
          shared: false,
          y: {
            formatter(val) {
              return val.toFixed(0);
            },
          },
          x: {
            format: 'yyyy-MM-dd HH:mm:ss',
          },
        },
      },
    };
  },
  watch: {
    votes_data: {
      handler(val) {
        // do stuff
        if (val.length >= 0) {
          this.series = val;
        } else {
          this.series = [team1, team2, team3];
        }
      },
      deep: true,
    },
  },
};
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  </style>
