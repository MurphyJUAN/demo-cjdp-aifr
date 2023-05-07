<!-- eslint-disable max-len -->
<template>
  <div class="home-content" id="Home">
    <div class="Home-title">系統說明</div>
    <UserGuide :guide="mainIntro" :isHome="true"></UserGuide>
    <div class="btn-content bg-white">
      <el-row :gutter="10" justify="space-around">
        <el-col :span="8"><router-link to="userPredict/mode1"><div class="grid-content bg-orange"><strong>輸入模式一</strong><div>選項勾選</div></div></router-link></el-col>
        <el-col :span="8"><router-link to="userPredict/mode2"><div class="grid-content bg-green"><strong>輸入模式二</strong><div>文字描述</div></div></router-link></el-col>
        <el-col :span="8"><router-link to="userPredict/mode3"><div class="grid-content bg-pink"><strong>輸入模式三</strong><div>選項+文字</div></div></router-link></el-col>
      </el-row>
    </div>
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
        '本網頁是國立清華大學人文社會AI應用與發展研究中心執行AI公共化相關計畫之成果展示。本系統的AI模型是使用司法院公開釋出的離婚後親權酌定裁判書，經由法律專業人工標註結果作為訓練資料。藉由自然語言處理技術，本系統可對使用者所提供的個案文字資料預測離婚後親權酌定結果(以機率表示各種可能性的高低)。但本系統任何結果都僅供參考，並無法律效力，使用者仍須以法院實際審理結果為最後依據。',
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
  position: relative;
  text-align: center;
  color: #fff;
}
.home-content {
  width: 90%;
  max-width: 1680px;
  margin: auto;
  padding: 20px 10px 50px 10px;
  min-height: calc(100vh - 255px);
}
.Home-subtitle {
  font-size: 2.1rem;
  font-weight: 300;
  padding-top: 2rem;
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

.btn-content {
  width: 100%;
  border-radius: 12px;
  border: 2px solid #cfbf84;
}
a {
  text-decoration: none !important;
}
.grid-content {
  border-radius: 4px;
  height: 8.5rem;
  margin: 30px;
  padding: 2rem;
  font-size: 1.5rem;
  color: #000;
  transition: 0.4s;
  &:hover {
    opacity: 0.8;
    font-size: 1.6rem;
  }
}
.bg-white{
  background-color: rgba(243,187,92,0.08);
}
.bg-orange {
  background: #FFD286;
}
.bg-green {
  background: #E1E898;
}
.bg-pink {
  background: #FBCACA;
}
</style>
