<template>
  <div class="taiwan-map" ref="map" id="TaiwanMap">
    <div id="map">
        <svg id="svg" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet"></svg>
      </div>
   </div>
</template>

<script>
// import * as d3 from "d3";

export default {
  name: 'taiwanMap',
  props: {
    cities: Array,
  },
  data() {
    return {
    };
  },
  watch: {
    cities: {
      deep: true,
      handler() {
        this.updateMap();
      },
    },
  },
  methods: {
    async updateMap() {
      const svg = await d3.select('#svg');
      const self = this; 
      svg.selectAll('path')
        .classed('active', function(d) {
          return self.cities.some(city => city.name === d.properties.COUNTYNAME && city.status);
        });
    },
    async getTaiwanMap() {
      const width = (this.$refs.map.offsetWidth).toFixed();
      const height = (this.$refs.map.offsetHeight).toFixed();

      let mercatorScale = window.screen.width;
      const w = window.screen.width;
      if (w > 360) {
        mercatorScale = 6000;
      } else if (w <= 360) {
        mercatorScale = 4000;
      }

      const path = await d3.geo.path().projection(
        d3.geo
          .mercator()
          .center([121, 24])
          .scale(mercatorScale)
          .translate([width/2, height/2.5])
      );

      const svg = await d3.select('#svg')
        .attr('width', width)
        .attr('height', height)
        .attr('viewBox', `0 0 ${width} ${height}`);


      const url = '../../../static/taiwan.geojson';
      const geometry = await d3.json(url);
      await d3.json(url, (error, geometry) => {
        if (error) throw error;

        svg
          .selectAll('path')
          .data(geometry.features)
          .enter().append('path')
          .attr('d', path)
          .attr({
            // 設定id，為了click時加class用
            id: (d) => 'city' + d.properties.COUNTYCODE
          })
          .attr({
            name: (d) => d.properties.COUNTYNAME
          })
          .classed('active', function(d) {
            if (this.cities) {
              return this.cities.some(city => city.name === d.properties.COUNTYNAME && city.status);
            }
              return null
          })
      });
      return svg;
    },
  },
  mounted() {
    this.getTaiwanMap();
  },
};

</script>

<style scoped>

.taiwan-map {
  width: 100%;
  height: 100%;
}

#map {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

#map >>> svg {
  max-height: 100vh;
}

#map >>> path {
  fill: transparent;
  stroke: #ffd694;
  transition: fill 0.2s ease, stroke 0.2s ease, transform 0.2s ease;
}

#map >>> path.active {
  fill: #ffd694;
  stroke: #ffd694;
}
#svg {
  height: inherit;
}

@media screen and (max-width: 480px) {
  .container {
    flex-wrap: wrap;
  }

  .taiwan-map{
    width: 100%;
  }

  .taiwan-map {
    height: 20vh;
  }
}

</style>
