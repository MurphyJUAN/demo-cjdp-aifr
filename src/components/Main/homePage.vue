<!-- eslint-disable max-len -->
<template>
  <div class="home-content" id="Home">
    <div class="Home-title">系統說明</div>
    <UserGuide :guide="mainIntro" :isHome="true"></UserGuide>
    <div class="btn-content bg-white">
      <el-row :gutter="10" justify="space-around">
        <el-col :span="8">
          <router-link to="userPredict/mode1">
            <div class="grid-content bg-orange">
              <strong>輸入模式一(選項勾選)</strong>
              <div>優點：可快速勾選</div>
              <div>缺點：需判斷分類</div>
              <div>準確度：~75%-77%</div>
            </div>
          </router-link>
        </el-col>
        <el-col :span="8">
          <router-link to="userPredict/mode2">
            <div class="grid-content bg-green">
              <strong>輸入模式二(文字描述)</strong>
              <div>優點：可直接文字輸入不分類</div>
              <div>缺點：輸入需時較久不易完整</div>
              <div>準確度：~83%-88%</div>
            </div>
          </router-link>
        </el-col>
        <el-col :span="8">
          <router-link to="userPredict/mode3">
            <div class="grid-content bg-pink">
              <strong>輸入模式三(選項勾選+文字描述)</strong>
              <div>優點：準確度最高(特別是對共同親權)</div>
              <div>缺點：輸入需時最久且需要判斷分類</div>
              <div>準確度：~86%-90%</div>
            </div>
          </router-link>
        </el-col>
        <!-- <el-col :span="6">
          <router-link to="/predict-mode4">
            <div class="grid-content bg-info">
              <strong>輸入模式四(選項勾選+文字描述)(多模型)</strong>
              <div>優點：準確度最高(特別是對共同親權)、預測結果較具有魯棒性</div>
              <div>缺點：輸入需時最久且需要判斷分類</div>
              <div>準確度：~86%-90%</div>
            </div>
          </router-link>
        </el-col> -->
      </el-row>
    </div>
    <div class="user-instruction mt-2 text-center">
      本系統AI模型所預測的結果僅供使用者參考用，建議由法律專業人士協助輸入資料並多方測試比較以發揮最大的效果。但本系統預測的結果並無任何法律效力。使用者仍須以法院實際審理結果為最後依據。
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
        '本系統是國立清華大學人文社會AI應用與發展研究中心為執行AI公共化相關計畫之成果展示。所使用的AI模型是以司法院少家廳所公開的家事裁判書為訓練資料，就使用者所輸入的個案狀況提供親權酌定結果的機率預測。為了更符合本中心所追求「可信賴之AI」的開發原則，本系統提供三種不同的個案資料輸入模式，說明其優缺點，且各模式皆有兩種以上的AI模型結果同時顯現以作比較，減少使用者對特定資料類型或特定AI模型的倚賴而產生的偏見，詳情可見「技術說明」。本系統預計2024年2月完成部署，開放各界使用。',
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
  padding: 20px 10px 20px 10px;
  min-height: calc(100vh - 255px);
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
  height: fit-content;
  margin: 1.3rem;
  padding: 0.8rem 2rem;
  text-align: left;
  font-size: 1rem;
  color: #000;
  transition: 0.4s;
  &:hover {
    opacity: 0.8;
    font-size: 1.1rem;
  }
}
.grid-content > strong {
  font-size: 1.2rem;
}
.grid-content > div {
  text-align: left;
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
