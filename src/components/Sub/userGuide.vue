<template>
  <div id="container-guide" class="Home-intro" style="z-index: 100;">
    <div id="guide">
        <h6 class="user-instruction">
          <div v-html="guide"></div>
        </h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'userGuide',
  props: {
    mainIntro: '',
    guide: '',
    isHome: false,
  },
};
</script>

<style lang="scss" scoped>

.Home-intro {
  overflow-y: auto;
  overflow-x: hidden;
  padding-bottom: 20px;
}

#guide {
  border-radius: 12px;
  padding: 20px;
  background-color: rgba(243,187,92,.08);
  border: 2px solid #cfbf84;
}

#container-guide {
  width: 100%;
}
.description {
  letter-spacing: 4px;
  line-height: 30px;
}
.user-instruction-title {
  text-align: left;
}

.user-instruction {
  font-size: 1.2rem;
  z-index: 100;
  line-height: 30px;
  text-align: left;
}
.home-description {
  letter-spacing: 4px;
  line-height: 35px;
  padding: 15px;
  font-size: 1.1rem;
}
.home-user-instruction {
  z-index: 100;
  line-height: 35px;
  letter-spacing: 4px;
  // margin-left: 50%;
  // transform: translateX(-50%);
  text-align: left;
  margin-top: 20px;
  font-size: 1.05rem;
}
.home-user-instruction-title {
  margin-top: 20px;
}
.user-instruction-title {
  text-align: left;
}
</style>
