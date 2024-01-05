<!-- eslint-disable max-len -->
<template>
  <div>
    <div class="web-header">
      <router-link to="/">
        <span class="web-title">AI輔助親權酌定預測系統</span>
      </router-link>
      <div class="head-divider"></div>
    </div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :router="true" text-color="#000" active-text-color="#F3BB5C">
      <!-- <el-menu-item index="0">LOGO</el-menu-item>
      <div class="flex-grow" /> -->
      <el-menu-item index="/">首頁</el-menu-item>
      <el-menu-item index="/userPredict/mode1">模式一：選項</el-menu-item>
      <el-menu-item index="/userPredict/mode2">模式二：文字</el-menu-item>
      <el-menu-item index="/userPredict/mode3">模式三：選項加文字</el-menu-item>
      <!-- <el-menu-item index="/predict-mode4">模式四：選項加文字(多模型)</el-menu-item> -->
      <el-menu-item index="/techDoc">技術說明</el-menu-item>
      <el-menu-item index="/links">友善資源</el-menu-item>
      <el-menu-item index="/contactUs">開發團隊</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      activeIndex: '/',
    };
  },
};
</script>

<style>
.el-menu {
  display: flex;
  justify-content: center;
}
.el-menu--horizontal>.el-menu-item {
  font-size: 1rem;
}
</style>
<style scoped>
.flex-grow {
  flex-grow: 1;
}
.web-header {
  width: 100%;
  background-color: #fff;
  padding-top: 10px;
  text-align: center;
}
.web-title {
  font-size: 1.5rem;
  line-height: 80px;
  font-weight: bold;
  padding-left: 20px;
}
.head-divider {
  width: 80%;
  margin: auto;
  height: 1px;
  margin-top: 10px;
  background-color: #ddd;
}
a {
  color: #000;
  text-decoration: none !important;
}
</style>
