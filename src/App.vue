<template>
  <div id="app" class="web-body">
    <!-- <img class="pinkCircle" src="static/pinkCircle.png" />
    <img class="blueCircle" src="static/blueCircle.png" />
    <img class="purpleBar" src="static/purpleBar.png" />
    <img class="yellowBar" src="static/yellowBar.png" />-->
    <div class="headerContainer">
      <appNavbar id="appNavbar"/>
    </div>
    <router-view :currentApi="currentApi" class="content" />
    <appLinks />
    <appFooter :currentApi="currentApi" />
  </div>
</template>

<script>
import Navbar from './components/Sub/navbar';
import Footer from './components/Sub/footer';
import Link from './components/Sub/links.vue';

export default {
  name: 'App',
  components: {
    appNavbar: Navbar,
    appFooter: Footer,
    appLinks: Link
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
    width: calc( 90% - 40px );
    max-width: 1680px;
    margin: 0px auto 50px auto;
}
.Home-title {
  font-size: 2.4rem;
  font-weight: 700;
  max-width: 1170px;
  padding: 1rem 10px;
  text-align: left;
  color: #FFF;
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
