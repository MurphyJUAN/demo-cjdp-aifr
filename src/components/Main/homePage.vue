<template>
  <div class="jumbotron content" id="Home">
    <div class="Home-container">
      <div class="Home-subtitle">Demo Landing Page</div>
      <div class="Home-title">Predicting Judicial Decisions on Post-Divorce Child Custody by Intermediate Self-Supervised Learning Method</div>
    </div>
    <UserGuide :guide="guide_en" :isHome="true"></UserGuide>
    <!-- <a href="/userPredict" class="btn-lg btn-default btn-navigate">Start Predict →</a> -->
    <router-link class="btn-lg btn-default btn-navigate" to="/userPredict" data-toggle="collapse" data-target=".dual-collapse2">Start Predict →</router-link>
  </div>
</template>

<script>
import UserGuide from '../Sub/userGuide';

export default {
  name: 'HomePage',
  components: {
    UserGuide,
  },
  data() {
    return {
      mainIntro:
        '本網頁是國立清華大學執行科技部AI人社領域計畫的成果展示與測試網頁。本計畫是使用司法院所公開釋出的判決書作為訓練資料，運用人工智慧中的自然語言處理技術建立人工智慧模型，針對若干司法案件預測可能的判決結果，提供案件的當事人參考。',
      guide:
        '一、本系統目前僅處理「離婚後父母雙方爭取孩子撫養權」的相關案例。<br />二、為增加預測結果的可靠度與避免錯誤使用，使用者請先閱讀相關案例。<br />三、本系統假設使用者所需要之輸入雙方與相關文字描述皆是正確與完整。若有資料提供不完整、錯誤、誇大或刻意偏袒等，結果可能會受影響。建議使用前可以自行多一些整理，或請公正第三方協助輸入。<br />四、本系統的功能與準確度亦隨時改進中，若有任何疑問與建議，歡迎留言指教。',
      guide_en:
        '<ul style="list-style-type: decimal;"><li> This judgment prediction is for the cases of post-divorce child custody, under the culture and law tradition of Taiwan society.</li><li>It is assumed that both parents are willing to raise the child. Please follow the steps below to input relevant information to make judgment prediction. </li><li> Any prediction result is insufficient due to the limitations of model training and does not have any legal effect.</li><li> This demo landing page and AI model is constructed by Y.-N. Juan et al. for the paper submitted for ACL 2023. </li><ul></ul></ul>',

    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
@import "vue-select/src/scss/vue-select.scss";
@import "~bootstrap/scss/_functions";
@import "~bootstrap/scss/_variables";
@import "~bootstrap/scss/mixins/_breakpoints";

.btn-navigate {
  color: #000;
  background-color: #f3bb5c;
  padding: 10px 20px;
  border-radius: 4px;
  border: 2px solid #f3bb5c;
  text-decoration: none;
  font-size: 1.2rem;
  transition: background-color .2s ease-in-out;
  &:hover {
    background: #FFA200;
    border: 2px solid #FFA200;
  }
}

#Home {
  background-color: #1f191b;
  height: 100%;
  position: relative;
  text-align: center;
  color: #fff;
}
.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 0;
  padding-bottom: 50px;
  border-radius: 0;
  overflow-y: auto;
}
.content {
  min-height: calc(100vh - 110px);
  width: 90%;
  max-width: 1680px;
  margin: auto;
}
.Home-subtitle {
  font-size: 2.1rem;
  font-weight: 300;
  padding-top: 2rem;
}
.Home-title {
  font-size: 2.4rem;
  font-weight: 700;
  max-width: 1170px;
  margin: auto;
  padding: 2rem 10px;
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
</style>
