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
    <!-- <appFooter :currentApi="currentApi" /> -->
  </div>
</template>

<script>
import Navbar from './components/Sub/navbar';
import Footer from './components/Sub/footer';

export default {
  name: 'App',
  components: {
    appNavbar: Navbar,
    appFooter: Footer,
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

<style lang="scss" scoped>
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
.content {
  min-height: calc(100vh - 56px - 120px);
}
</style>
