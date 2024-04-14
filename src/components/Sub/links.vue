<!-- eslint-disable max-len -->
<template>
  <div class="page-container">
    <div class="content-container mt-2">
      <div class="intro-text-container rounded">使用說明：本網頁蒐集國內各縣市中，親權裁判當事人所可能會需要使用或參考的社會服務資源。請先從左方地圖上點選所要查詢的縣市，右方即會呈現該縣市目前相關資源之網頁連結。使用者可以直接點入即連結到該機構的網頁，進一步查詢相關資訊。</div>
      <el-row :gutter="20" class="links-container">
        <el-col :xs="24" :sm="12">
          <div class="map-container">
            <div class="map-btn-container">
              <el-button type="danger" @click="clearAll()">清除</el-button>
              <el-button :type="all_city.status?'primary':'default'" @click="all_city.status = !all_city.status" style="margin-left: 2px;">{{ all_city.name }}</el-button>
              <el-button v-for="city in cities"
              :key="city.name"
              :type="city.status?'primary':'default'"
              @click="city.status = !city.status"
              >{{ city.name }}</el-button>
            </div>
            <!-- <img class="map-img" src="../../../static/taiwan_map.png" /> -->
          </div>
        </el-col>
        <el-col :xs="24" :sm="12">
          <div>本網頁目前包含的資源包括以下8大類：</div>
          <div>(1)政府部門、(2)法律議題、(3)家庭諮商、(4)家庭扶助、(5)親職教育、(6)兒少照顧、(7)心理健康、(8) 多元族群。</div>
          <div class="links-result-container rounded">
            <div v-for="(category, i) in Object.keys(selectedResources)" :key="category" style="margin-top: 5px;">
              <span>({{ i+1 }}){{ category }}:</span>
              <span v-if="selectedResources[category].length == 0">無</span>
              <div v-else>
                <span v-for="(link, i) in selectedResources[category]" :key="i">
                  <a :href="link.link" target="_blank">{{ link.name }}</a>
                  <span v-if="i<selectedResources[category].length-1">、</span>
                </span>
              </div>
            </div>
            <div style="margin-top: 10px;">##目前的內容還在建置中，若有未即時更新或缺少的資訊還請見諒，歡迎與我們聯繫作調整。</div>
          </div>
          <div style="font-style: italic;">感謝育達科技大學社會工作系施睿宜教授 (現任臺灣司法社工學會秘書長)提供本網頁的相關專業資訊。</div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Resources from '../../../static/resources_by_city.json';

export default {
  name: 'Link',
  components: {
  },
  data() {
    return {
      cities: [],
      all_city: { name: '全選', status: false },
      selectedResources: {
        政府部門: [],
        法律議題: [],
        家庭諮商: [],
        家庭扶助: [],
        親職教育: [],
        兒少照顧: [],
        心理健康: [],
        多元族群: [],
      },
    };
  },
  created() {
  },
  mounted() {
    Object.keys(Resources).forEach((key) => {
      if (key !== '全選') {
        this.cities.push({ name: key, status: false });
      }
    });
  },
  methods: {
    mergeUniqueResources(category, newResources) {
      const resourceMap = new Map(this.selectedResources[category].map(item => [item.name, item]));
      newResources.forEach((resource) => {
        if (!resourceMap.has(resource.name)) {
          resourceMap.set(resource.name, resource);
        }
      });
      this.selectedResources[category] = Array.from(resourceMap.values());
    },
    isSelectAll(cities) {
      return !cities.some(city => city.status === false);
    },
    selectAll() {
      let allCity = [];
      Object.keys(Resources).forEach((key) => {
        allCity.push({ name: key, status: true });
      });
      this.cities = allCity;
    },
    clearAll() {
      let allCity = [];
      Object.keys(Resources).forEach((key) => {
        allCity.push({ name: key, status: false });
      });
      this.cities = allCity;
    }
  },
  watch: {
    all_city: {
      deep: true,
      handler() {
        if (this.all_city.status) {
          this.selectAll();
          // const nationalResources = Resources['全選'];
          // Object.keys(this.selectedResources).forEach((category) => {
          //   if (nationalResources[category]) {
          //     this.mergeUniqueResources(category, nationalResources[category]);
          //   }
          // });
        }
      },
    },
    cities: {
      deep: true,
      handler() {
        Object.keys(this.selectedResources).forEach((key) => {
          this.selectedResources[key] = [];
        });

        const activeCities = this.cities.filter(city => city.status).map(city => city.name);

        activeCities.forEach((cityName) => {
          const cityResources = Resources[cityName] || {};
          Object.keys(this.selectedResources).forEach((category) => {
            if (cityResources[category]) {
              this.mergeUniqueResources(category, cityResources[category]);
            }
          });
        });
        if (!this.isSelectAll(this.cities)) {
          this.all_city.status = false;
        } else {
          this.all_city.status = true;
        }
      },
    },
  },
};
</script>

<style lang="scss" scoped>
@import "vue-select/src/scss/vue-select.scss";
@import "~bootstrap/scss/_functions";
@import "~bootstrap/scss/_variables";
@import "~bootstrap/scss/mixins/_breakpoints";

.page-container {
  width: calc( 95% - 40px );
  max-width: 2000px;
  margin: auto;
}
.content-container {
  background-color: #fff;
  border: 2px solid #F3BB5C;
  border-radius: 8px;
  padding: 20px 20px;
  margin-bottom: 50px;
}
.xgboost-img {
  width: 50%;
}
.intro-text-container {
  width: 90%;
  background-color: rgb(209, 232, 246);
  margin: 10px auto;
  padding: 10px 20px;
  font-size: 1rem;
}
.links-container {
  width: 90%;
  margin: 10px auto !important;
  padding: 10px 20px;
}
.links-result-container {
  border: 2px solid #bba0c8;
  margin: 10px 0;
  padding: 10px 20px;
}
.map-container {
  display: flex;
  justify-content: flex-end;
  background-image: url('../../../static/taiwan_map.png');
  background-size: contain;
  background-position: left;
  background-repeat: no-repeat;
}
.map-img {
  width: 65%;
  height: fit-content;
  padding-right: 10px;
}
.map-btn-container {
  width: 180px;
}
.map-btn-container >>> button {
  margin: 5px;
}

@media only screen and (max-width: 600px) {
  .links-container {
    width: 100%;
    padding: 10px 10px;
  }
}
</style>

