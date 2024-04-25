<template>
  <div>
    <div id="app" class="web-body" v-if="!$route.path.includes('vote')">
      <!-- <img class="pinkCircle" src="static/pinkCircle.png" />
      <img class="blueCircle" src="static/blueCircle.png" />
      <img class="purpleBar" src="static/purpleBar.png" />
      <img class="yellowBar" src="static/yellowBar.png" />-->
      <div class="headerContainer">
        <appNavbar v-if="!$route.path.includes('demo') && !$route.path.includes('chat')" id="appNavbar"/>
        <appNavbarAIJuniorAward v-if="$route.path.includes('chat')" id="appNavbarAIJuniorAward"/>
        <appNavbarDemo v-if="$route.path.includes('demo')" id="appNavbarDemo"/>
      </div>
      <router-view :currentApi="currentApi" class="content" />
      <appFooter :currentApi="currentApi" />
    </div>
    <router-view v-if="$route.path.includes('vote')" :currentApi="currentApi" class="content" />
  </div>
</template>

<script>
import Navbar from './components/Sub/navbar';
import NavbarDemo from './components/Sub/navbarDemo';
import Footer from './components/Sub/footer';
import NavbarAIJuniorAward from './components/Sub/navbarAIJuniorAward';


export default {
  name: 'App',
  components: {
    appNavbar: Navbar,
    appNavbarDemo: NavbarDemo,
    appFooter: Footer,
    appNavbarAIJuniorAward: NavbarAIJuniorAward,
  },
  data() {
    // test api
    const testApi = this.axios.create({
      baseURL: 'http://127.0.0.1:5001/api/',
    });
    // public api
    const publicApi = this.axios.create({
      baseURL: 'http://predict.aifr.ml:29757/api/',
    });
    // public api
    const publicApi2 = this.axios.create({
      baseURL: 'https://custodyprediction-api.herokuapp.com/api/',
    });
    return {
      // current use api
      // currentApi: testApi,
      currentApi: publicApi,
      // currentApi: publicApi2,
    };
  },
  created() {
    // if (!this.$route.path.includes('demo')) {
    //   this.$confirm('<div style="color:red;">本網頁正在進行升級，目前所呈現的結果請勿參考<div>', '', {
    //     confirmButtonText: '我了解',
    //     type: 'warning',
    //     showCancelButton: false,
    //     dangerouslyUseHTMLString: true,
    //   });
    // }
  },
};
</script>

<style lang="scss">
@import url(https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;700&display=swap);

body {
  background: #1f191b;
}

#app {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #1f191b;
}
.headerContainer {
  background-color: #fff;
}
.page-container {
    max-width: 1680px;
    min-height: calc(100vh - 305px);
}

/* 媒体查询（大屏幕） */
@media (min-width: 768px) { /* 例如，使用 768px 作为小屏幕和大屏幕的分界点 */
    .page-container {
        width: calc(90% - 40px);
        margin: 0px auto 50px auto;
        max-width: 1680px;
        min-height: calc(100vh - 305px);
    }
}

.Home-title {
  font-size: 2rem;
  font-weight: 700;
  max-width: 1170px;
  padding: 2rem 10px;
  text-align: left;
  color: #FFF;
}
.user-instruction {
  font-size: 1rem;
  z-index: 100;
  line-height: 1.6rem;
  text-align: left;
  color: #fff;
}
#appNavbar {
  width: 90%;
  max-width: 1680px;
  margin: auto;
}
.web-body {
  overflow: hidden;
  position: relative;
  background-color: #1f191b;
}
.pinkCircle {
  position: absolute;
  width: 80vh;
  height: 80vh;
  z-index: 90;
  left: -20vh;
}
.blueCircle {
  position: absolute;
  width: 80vh;
  height: 80vh;
  z-index: 90;
  right: -20vh;
  top: 60vh;
}
.yellowBar {
  position: absolute;
  z-index: 90;
  height: 80vh;
  left: 20px;
  bottom: 30vh;
  transform: rotate(-45deg);
}
.purpleBar {
  position: absolute;
  z-index: 90;
  height: 80vh;
  right: 20px;
  bottom: 20vh;
  transform: rotate(-20deg);
}

</style>
