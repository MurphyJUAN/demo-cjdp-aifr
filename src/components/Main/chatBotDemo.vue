<!-- eslint-disable max-len -->
<template>
    <div class="chatbot-container">
        <div class="header d-flex px-3 align-items-center">
            <div class="header-title d-inline-flex"><div class="circle mx-2"></div>Le姐 | 家事商談機器人</div>
            <div class="d-flex">
                <img class="title-icon mx-1" src="../../../static/moon.png">
                <img class="title-icon mx-1" src="../../../static/drop.png">
                <img class="title-icon mx-1" src="../../../static/refresh.png">
                <img class="title-icon mx-1" src="../../../static/log-in.png">
            </div>
        </div>

        <div class="conversation-container">
            <div class="le-talk-block b-w">hi</div>
        </div>

        <div class="le-foot d-inline-flex">
            <div class="b-w bottom-input"></div>
            <div class="b-w bottom-send"></div>
        </div>

    </div>
</template>

<script>

export default {
  name: 'chatbotDemo',
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

.chatbot-container {
    margin: auto;
    width: 440px;
    height: 900px;
    max-height: 900px;
    overflow-y: scroll;
    background: #062043;
    position: relative;
}
.header {
    height: 45px;
    background: #EB7D01;
    color: white;
    font-weight: bold;
    justify-content: space-between;
}
.circle {
    width: 5px;
    height: 5px;
    border-radius: 100%;
    background: #D2E854;
    margin: auto;
}
.title-icon {
    width: 1rem;
}
.le-foot{
    height: 72px;
    width: 440px;
    padding: 1rem;
    padding-top: 0.5rem;
    color: white;
    position: absolute;
    bottom: 0;
    border: 1px solid white;
    justify-content: space-between;
}
.b-w {
    background: white;
}
.bottom-input {
    width: 344px;
    height: 48px;
}
.bottom-send{
    width:48px;
    height: 48px;
}
.le-talk-block {
    width: 426px;
    padding: 1.5rem;
}

</style>

