<template>
  <div>
    <div class="jumbotron" id="Home">
      <div class="inner">
        <h1 class="py-3 Home-title" style="z-index:100">過往案例資料</h1>
        <UserGuide :guide="guide" :isHome="false"></UserGuide>
        <div id="btn-det">
          <div class="d-inline-flex w-100 justify-content-center">
            <div class="mt-4 px-2" @click="getTestJudgement()" style="z-index:100">
              <a class="btn-lg btn-default btn" href="javascript:void(0)">隨機取得案例</a>
            </div>
          </div>
        </div>
        <div class="testOutBox" style="z-index:100">
          <div class="mt-4 test-number" v-if="testJudgement.length != 0" :key="testJudgement.ID">
            以下內容出自隨機範例編號：{{ testJudgement.ID }}
            <br />
            <div class="d-inline-flex text-left">
              <div class="px-2">
                <div>聲請方身份：({{ testJudgement.AK }}) {{AkDetail}}</div>
                <div>聲請方國籍：({{ testJudgement.AN }}) {{AnDetail}}</div>
              </div>
              <div class="px-2">
                <div>相對方身份：({{ testJudgement.RK }}) {{RkDetail}}</div>
                <div>相對方國籍：({{ testJudgement.RN }}) {{RnDetail}}</div>
              </div>
            </div>
            <br />
            <div class="test-result">判決結果：{{ testResult }}</div>
          </div>
        </div>
      </div>
    </div>

    <section id="meanResult" style="position:relative">
      <!-- <loading
    loader="bars"
    :active.sync="isLoading"
    :can-cancel="true"
      :is-full-page="false" />-->

      <div class="container mt-4" v-visible="visible">
        <div class="d-inline-flex w-100 mt-3 row">
          <div class="a-advantage data-outer-box w-100 col-sm-6" style="z-index:100">
            <h4 class="data-title" style="z-index:100">聲請方有利條件：</h4>
            <div v-if="!testJudgement.AA" class="none-title">(無)</div>
            <ul class="data-inner-box mt-3 pl-4 pr-2" style="z-index:100">
              <li class="mt-0 py-3" v-for="(item, index) in testJudgement.AA" :key="'key_AA'+index">
                <div
                  class="w-100 h-25 reasoningText form-control"
                  :id="'AA'+index"
                >{{testJudgement.AA[index]}}</div>
              </li>
            </ul>
          </div>
          <div class="b-advantage data-outer-box w-100 col-sm-6" style="z-index:100">
            <h4 class="data-title" style="z-index:100">相對方有利條件：</h4>
            <div v-if="!testJudgement.RA" class="none-title">(無)</div>
            <ul class="data-inner-box mt-3 pl-4 pr-2" style="z-index:100">
              <li class="mt-0 py-3" v-for="(item, index) in testJudgement.RA" :key="'key_RA'+index">
                <div
                  class="w-100 h-25 reasoningText form-control"
                  :id="'RA'+index"
                >{{testJudgement.RA[index]}}</div>
              </li>
            </ul>
          </div>
          <div class="a-disadvantage data-outer-box w-100 col-sm-6" style="z-index:100">
            <h4 class="data-title" style="z-index:100">聲請方不利條件：</h4>
            <div v-if="!testJudgement.AD" class="none-title">(無)</div>
            <ul class="data-inner-box mt-3 pl-4 pr-2" style="z-index:100">
              <li class="mt-0 py-3" v-for="(item, index) in testJudgement.AD" :key="'key_AD'+index">
                <div
                  class="w-100 h-25 reasoningText form-control"
                  :id="'AD'+index"
                >{{testJudgement.AD[index]}}</div>
              </li>
            </ul>
          </div>
          <div class="b-disadvantage data-outer-box w-100 col-sm-6" style="z-index:100">
            <h4 class="data-title" style="z-index:100">相對方不利條件：</h4>
            <div v-if="!testJudgement.RD" class="none-title">(無)</div>
            <ul class="data-inner-box mt-3 pl-4 pr-2" style="z-index:100">
              <li class="mt-0 py-3" v-for="(item, index) in testJudgement.RD" :key="'key_RD'+index">
                <div
                  class="w-100 h-25 reasoningText form-control"
                  :id="'RD'+index"
                >{{testJudgement.RD[index]}}</div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="container" v-visible="visible2">
        <h3 class="pt-3" style="z-index:100">發生錯誤</h3>
      </div>
      <router-link to="/userPredict" class="btn-lg btn-default btn-navigate">進入判決預測網頁 ></router-link>
    </section>
    <div class="back-top" v-if="backTop" @click="backToTop()">
      <i class="fas fa-chevron-up"></i>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueVisible from 'vue-visible';
import VueLoading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import Case1 from '../../../static/case1.json';
import Case2 from '../../../static/case2.json';
import Case3 from '../../../static/case3.json';
import Case4 from '../../../static/case4.json';
import Case5 from '../../../static/case5.json';
import Case6 from '../../../static/case6.json';

import UserGuide from '../Sub/userGuide';

Vue.use(VueVisible);

export default {
  name: 'PastCase',
  components: {
    loading: VueLoading,
    UserGuide,
  },
  data() {
    // test api
    const testApi = this.axios.create({
      baseURL: 'http://127.0.0.1:5001/api/',
    });
    // public api
    const publicApi = this.axios.create({
      baseURL: 'http://140.114.80.82:29757/api/',
    });

    return {
      visible: true,
      visible2: false,
      backTop: false,
      testJudgement: [],
      isLoading: false,
      elapsedTime: 0,
      predict_result: [],
      backend: [],
      AkDetail: '',
      AnDetail: '',
      RkDetail: '',
      RnDetail: '',
      testResult: '',
      queryID: '',
      // current use api
      // currentApi: testApi,
      currentApi: publicApi,
      guide:
        '一、請先隨機點選「隨機取得案例」而閱讀若干過往案例資料。<br />二、相關案例是從司法院的法學資料檢索系統所下載，與「離婚後親權判決」相關，且雙方皆有意願爭取孩子監護權的判決書。<br />三、所有案例皆已去除可識別的個人資料並提取對雙方有利或不利的判決文字，且已將指稱雙方用語分別改為當事人與對方，並非判決書全文。',
    };
  },
  methods: {
    backToTop() {
      const element = document.getElementById('appNavbar');
      element.scrollIntoView();
    },
    handleScroll() {
      // 改变元素#searchBar的top值
      const scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 100) {
        this.backTop = true;
      } else {
        this.backTop = false;
      }
    },
    getTestJudgement() {
      const data = [Case1, Case2, Case3, Case4, Case5, Case6];
      const targetNumber = Math.floor(Math.random() * 6) + 1;
      this.testJudgement = data[targetNumber - 1];
      if (this.testJudgement.AK === 'a') {
        this.AkDetail = '父 ';
      } else {
        this.AkDetail = '母 ';
      }
      if (this.testJudgement.RK === 'a') {
        this.RkDetail = '父 ';
      } else {
        this.RkDetail = '母 ';
      }
      if (this.testJudgement.AN === 'a') {
        this.AnDetail = '本國';
      } else if (this.testJudgement.AN === 'b') {
        this.AnDetail = '大陸籍';
      } else if (this.testJudgement.AN === 'c') {
        this.AnDetail = '其他';
      } else {
        this.AnDetail = '雙重國籍';
      }
      if (this.testJudgement.RN === 'a') {
        this.RnDetail = '本國';
      } else if (this.testJudgement.RN === 'b') {
        this.RnDetail = '大陸籍';
      } else if (this.testJudgement.RN === 'c') {
        this.RnDetail = '其他';
      } else {
        this.RnDetail = '雙重國籍';
      }
      if (this.testJudgement.Result === 'a') {
        this.testResult = '判給聲請人';
      } else if (this.testJudgement.Result === 'b') {
        this.testResult = '判給相對人';
      } else {
        this.testResult = '判給雙方';
      }
      console.log(Case1.AK);
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
@import "vue-select/src/scss/vue-select.scss";
@import "~bootstrap/scss/_functions";
@import "~bootstrap/scss/_variables";
@import "~bootstrap/scss/mixins/_breakpoints";

* {
  position: relative;
  font-family: 微軟正黑體;
}

.web-body {
  overflow: hidden;
}

.container {
  @media (min-width: 1800px) {
    max-width: 1500px;
  }
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

ul {
  list-style-type: decimal;
  line-height: 35px;
  @media screen and (max-width: 700px) {
    padding-left: 0px;
    padding-right: 10px;
  }
}

.reasoningText {
  vertical-align: top;
  border: none;
  background-color: transparent;
  @media (min-width: 1800px) {
    font-size: 1.5rem;
  }
}

.description {
  letter-spacing: 4px;
  line-height: 35px;
}

.data-outer-box {
  padding: 10px;
}
.data-inner-box {
  max-height: 300px;
  overflow: auto;
}

@media (min-width: map-get($grid-breakpoints, sm)) {
  .a-advantage,
  .a-disadvantage {
    border-right: solid 1px #282f44;
  }

  .b-advantage,
  .b-disadvantage {
    border-left: solid 1px #282f44;
  }
}

.test-number {
  color: gray;
  line-height: 30px;
}

.back-top {
  width: 60px;
  height: 60px;
  background-color: hsla(5, 76%, 62%, 0.8);
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  color: white;
  line-height: 60px;
  z-index:101;
}
.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 0px;
  padding-bottom: 0px;
  border-radius: 0px;
}

#only-sentence {
  @media (min-width: 500px) {
    max-width: 220px;
  }
  border-radius: 5px;
  border: solid 1px #bbbbbbad;
  padding: 10px;
  background-color: transparent;
  color: black;
}

input,
textarea {
  &:focus,
  &:hover {
    border-width: 1.5px !important;
    border-style: inset !important;
    border-color: rgb(138, 113, 206) !important;
    box-shadow: 0 0 20px rgb(138, 113, 206);
  }
}

li {
  text-align: left;
}

.btn {
  color: white;
  background-color: gray;
  padding: 15px;
  letter-spacing: 2px;
  border-radius: 0px;
  border: none;
  font-weight: 800;
  font-size: 15px;
  transition: background-color 0.2s ease-in-out;
  &:hover {
    background: #d8235e;
  }
}

.btn-navigate {
  color: white;
  background-color: rgb(226, 145, 60);
  padding: 15px;
  letter-spacing: 2px;
  border-radius: 0px;
  border: none;
  font-weight: 800;
  font-size: 15px;
  transition: background-color 0.2s ease-in-out;
  &:hover {
    background: rgb(74, 163, 175);
  }
}

.navbar {
  background-color: #f7f7f7;
  box-shadow: 0 0 0.1em 0 rgba(0, 0, 0, 0.25);
  a {
    color: black;
    font-weight: 800;
    font-size: 50px;
  }
}

#Home {
  background-color: #f7f7f7;
  overflow: hidden;
  height: 100%;
  position: relative;
  color: black;
}

.Home-title {
  color: black;
}

#meanResult {
  padding-top: 2rem;
  padding-bottom: 2rem;
  background-color: #f7f7f7;
  color: black;
}

.test-result {
  font-weight: 800;
}

.none-title {
  color: gray;
}
.user-instruction {
  z-index: 100;
  line-height: 35px;
  letter-spacing: 4px;
  // margin-left: 50%;
  // transform: translateX(-50%);
  text-align: left;
  margin-top: -25px;
}
.test-number {
  color: gray;
  line-height: 30px;
}
.test-result {
  font-weight: 800;
}
</style>
