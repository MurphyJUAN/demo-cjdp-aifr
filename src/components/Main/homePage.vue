<!-- eslint-disable max-len -->
<template>
  <div class="home-content" id="Home">
    <ChatBotIntro />
  </div>
</template>

<script>
import ChatBotIntro from '../Sub/chatbotIntro.vue';

export default {

  name: 'homePage',
  components: {
    ChatBotIntro,
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
.home-content {
  width: 100%;
  max-width: 1680px;
  margin: auto;
  padding: 0px 2rem 0px 2rem;
  min-height: 100vh;
}

/* 媒体查询（大屏幕） */
@media (max-width: 768px) { /* 例如，使用 768px 作为小屏幕和大屏幕的分界点 */
  .home-content {
    padding: 0;
  }
}

html, body {
  padding: 0;
  margin: 0;
  background: white !important;
}

</style>
