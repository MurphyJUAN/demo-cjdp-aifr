<!-- eslint-disable max-len -->
<template>
    <div class="page-container">
        <div class="content-container mt-2">
          <div>
          <h6>指導教授</h6>
            <ul>
              <li>
                王道維教授 (國立清華大學物理系)
              </li>
              <li>
                林昀嫺教授 (國立清華大學科技法律研究所)
              </li>
            </ul>
          </div>

          <div>
          <h6>資工技術</h6>
            <ul>
              <li>
                阮羿寧 (清華大學人文社會AI應用與發展研究中心)
              </li>
              <li>
                李亞倫 (清華大學資訊系統與應用研究所)
              </li>
              <li>
                劉弘祥 (清華大學電機系)
              </li>
            </ul>
          </div>

          <div>
          <h6>資料分析</h6>
            <ul>
              <li>
                林雲貂 (清華大學跨院國際博士班學位學程)
              </li>
            </ul>
          </div>

          <div>
          <h6>法律專業</h6>
            <ul>
              <li>
                孫維曼、林倚婕、何宣逸、陳彥熹、蘇雍俊、洪于茜 (清華大學科技法律研究所)
              </li>
            </ul>
          </div>

          <div>
          <h6>網站設計</h6>
            <ul>
              <li>
                何捷睿 (清華大學服務科學研究所)
              </li>
            </ul>
          </div>


        </div>

    </div>
  </template>

<script>

export default {
  name: 'ContactUs',
  components: {
  },
  data() {
    return {

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

</style>

