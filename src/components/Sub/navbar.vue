<!-- eslint-disable max-len -->
<template>
  <div>
    <b-navbar v-if="!isSmallScreen" toggleable="lg" fixed="top" class="navbarDefault">
        <b-navbar-nav>
          <b-nav-item href="/"><div>AI輔助親權裁判預測系統</div></b-nav-item>
        </b-navbar-nav>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <!-- <b-navbar-nav :to="/ai_junior_award">AIFRxAI Junior Award 2024</b-navbar-nav> -->
        <b-collapse id="nav-collapse" is-nav >
          <b-navbar-nav class="ml-auto">
            <b-nav-item :to="'/'" active-class="router-link-exact-active" exact class="mx-1 my-nav-item">首頁</b-nav-item>
            <b-nav-item :to="'/news'" active-class="router-link-exact-active" class="mx-1 my-nav-item">報導與介紹</b-nav-item>
            <b-nav-item :to="'/userPredict/mode1'" active-class="router-link-exact-active" class="mx-1 my-nav-item">模式一：選項</b-nav-item>
            <b-nav-item :to="'/userPredict/mode2'" active-class="router-link-exact-active" class="mx-1 my-nav-item">模式二：文字</b-nav-item>
            <b-nav-item :to="'/userPredict/mode3'" active-class="router-link-exact-active" class="mx-1 my-nav-item">模式三：選項加文字</b-nav-item>
            <b-nav-item :to="'/links'" active-class="router-link-exact-active" class="mx-1 my-nav-item">友善資源</b-nav-item>
            <b-nav-item :to="'/userDoc'" active-class="router-link-exact-active" class="mx-1 my-nav-item">使用說明</b-nav-item>
            <b-nav-item :to="'/techDoc'" active-class="router-link-exact-active" class="mx-1 my-nav-item">技術說明</b-nav-item>
            <b-nav-item :to="'/contactUs'" active-class="router-link-exact-active" class="mx-1 my-nav-item">開發團隊</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
    </b-navbar>

    <!-- 大螢幕 -->
    <b-navbar v-if="isSmallScreen" class="navbarDefault" toggleable="lg" fixed="top">
      <b-container>
        <b-navbar-nav>
          <b-nav-item :to="'/'">AI輔助親權裁判預測系統</b-nav-item>
        </b-navbar-nav>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <!-- <b-navbar-nav :to="/ai_junior_award">AIFRxAI Junior Award 2024</b-navbar-nav> -->
        <b-collapse id="nav-collapse" is-nav >
          <b-navbar-nav class="ml-auto">
            <b-nav-item :to="'/'" active-class="router-link-exact-active my-nav-item" exact >首頁</b-nav-item>
            <b-nav-item :to="'/news'" active-class="router-link-exact-active" class="mx-1 my-nav-item">報導與介紹</b-nav-item>
            <b-nav-item :to="'/userPredict/mode1'" active-class="router-link-exact-active my-nav-item">模式一：選項</b-nav-item>
            <b-nav-item :to="'/userPredict/mode2'" active-class="router-link-exact-active my-nav-item">模式二：文字</b-nav-item>
            <b-nav-item :to="'/userPredict/mode3'" active-class="router-link-exact-active">模式三：選項加文字</b-nav-item>
            <b-nav-item :to="'/links'" active-class="router-link-exact-active my-nav-item">友善資源</b-nav-item>
            <b-nav-item :to="'/userDoc'" active-class="router-link-exact-active my-nav-item">使用說明</b-nav-item>
            <b-nav-item :to="'/techDoc'" active-class="router-link-exact-active my-nav-item">技術說明</b-nav-item>
            <b-nav-item :to="'/contactUs'" active-class="router-link-exact-active my-nav-item">開發團隊</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      isSmallScreen: false,
    };
  },
  created() {

  },
  mounted() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  },
  methods: {
    checkScreenSize() {
      this.isSmallScreen = window.innerWidth < 992; // 例如，992px 可以是你定义的小屏幕最大宽度
    },
  },
};
</script>


<style lang="scss" scoped>
@charset "UTF-8";
* {
  font-family: 宋體-繁;
}
.navbarDefault {
  background-color: #F8F8F8;
  // border-bottom: 1px solid #F8F8F8;
  color: #777;
  transition: 0.1s;
}

.router-link-exact-active {
  color: rgba(0, 0, 0, 0.7) !important; // 確保文字顏色持續為黑色
  border-top: 1px solid #FF6F39 !important; // 確保橘色的線持續顯示
}


.navbarDefault .my-nav-item:hover {
  color: rgba(0, 0, 0, 0.7);
  // font-weight: bold;
  border-top: 1px solid #FF6F39;
}
</style>
