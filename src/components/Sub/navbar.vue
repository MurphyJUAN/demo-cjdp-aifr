<!-- eslint-disable max-len -->
<template>
  <div>
    <div class="web-header">
      <router-link to="/">
        <span class="web-title">AI輔助親權酌定預測系統</span>
      </router-link>
      <div class="head-divider"></div>
    </div>
    <el-row class="menu-container">
      <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" :router="true" text-color="#000" active-text-color="#F3BB5C" v-if="!isMobile">
        <!-- <el-menu-item index="0">LOGO</el-menu-item>
        <div class="flex-grow" /> -->
        <el-menu-item index="/">首頁</el-menu-item>
        <el-menu-item index="/userPredict/mode1">模式一：選項</el-menu-item>
        <el-menu-item index="/userPredict/mode2">模式二：文字</el-menu-item>
        <el-menu-item index="/userPredict/mode3">模式三：選項加文字</el-menu-item>
        <!-- <el-menu-item index="/predict-mode4">模式四：選項加文字(多模型)</el-menu-item> -->
        <el-menu-item index="/userDoc">使用說明</el-menu-item>
        <el-menu-item index="/techDoc">技術說明</el-menu-item>
        <el-menu-item index="/links">友善資源</el-menu-item>
        <el-menu-item index="/contactUs">開發團隊</el-menu-item>
      </el-menu>

      <div class="hamburger-menu" @click="toggleSidebar" v-if="isMobile">
        ☰
      </div>
      <!-- 側邊欄 -->
      <el-drawer
        :visible.sync="sidebarVisible"
        direction="ltr"
        size="200px"
        v-if="isMobile">
        <el-menu :default-active="$route.path" mode="vertical" :router="true">
          <el-menu-item index="/" @click.native="closeSidebar">首頁</el-menu-item>
          <el-menu-item index="/userPredict/mode1" @click.native="closeSidebar">模式一：選項</el-menu-item>
          <el-menu-item index="/userPredict/mode2" @click.native="closeSidebar">模式二：文字</el-menu-item>
          <el-menu-item index="/userPredict/mode3" @click.native="closeSidebar">模式三：選項加文字</el-menu-item>
          <!-- <el-menu-item index="/predict-mode4">模式四：選項加文字(多模型)</el-menu-item> -->
          <el-menu-item index="/userDoc" @click.native="closeSidebar">使用說明</el-menu-item>
          <el-menu-item index="/techDoc" @click.native="closeSidebar">技術說明</el-menu-item>
          <el-menu-item index="/links" @click.native="closeSidebar">友善資源</el-menu-item>
          <el-menu-item index="/contactUs" @click.native="closeSidebar">開發團隊</el-menu-item>
        </el-menu>
      </el-drawer>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      activeIndex: '/',
      sidebarVisible: false,
      isMobile: false,
    };
  },
  created() {
    this.handleResize();
    window.addEventListener('resize', this.handleResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    toggleSidebar() {
      this.sidebarVisible = !this.sidebarVisible;
    },
    handleResize() {
      this.isMobile = window.innerWidth < 768; // 假設小於 768px 為手機屏幕
    },
    closeSidebar() {
      this.sidebarVisible = false;
    },
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

.menu-container {
  white-space: nowrap; /* 防止内容换行 */
  max-width: 100%; /* 限制最大宽度，避免影响布局 */
}

.el-menu-demo {
  /* width: 1px; */
  margin: 0px;
  padding: 0px;
}
/* .el-menu {
  overflow: hidden;
  justify-content: center;
} */
/* @media (max-width: 768px) {
  .el-menu {
    overflow-x: scroll;
    justify-content: flex-start;
  }
} */
.hamburger-menu {
  cursor: pointer;
  display: none;
}

@media (max-width: 768px) {
  .el-menu-demo {
    display: none;
  }
  .hamburger-menu {
    display: block;
    font-weight: bold;
    color: #2F2620;
    font-size: 1rem;
  }
  .el-menu {
    display: block;
  }
}
</style>
