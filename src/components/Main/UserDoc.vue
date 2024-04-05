<!-- eslint-disable max-len -->
<template>
    <div class="d-flex w-100 justify-content-center">
        <!-- https://drive.google.com/file/d/10JUGp_skGvYRpaIhOzcKAT97nTIl2ooM/view?usp=sharing -->
        <vue-pdf-embed  class="pdf-container" :source="pdfSource" />
    </div>
  </template>

<script>
import VuePdfEmbed from 'vue-pdf-embed/dist/vue2-pdf-embed';

// either URL, Base64, binary, or document proxy
// const pdfSource = 'https://drive.google.com/file/d/10JUGp_skGvYRpaIhOzcKAT97nTIl2ooM/view?usp=sharing';

export default {
  name: 'UserDoc',
  components: {
    VuePdfEmbed,

  },
  data() {
    return {
      pdfSource: 'https://murphyjuan.github.io/demo-cjdp-aifr/static/AI%E8%BC%94%E5%8A%A9%E8%A6%AA%E6%AC%8A%E9%85%8C%E5%AE%9A%E9%A0%90%E6%B8%AC%E7%B3%BB%E7%B5%B1%E4%BD%BF%E7%94%A8%E8%AA%AA%E6%98%8Ev2.pdf',
    };
  },
};
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
.pdf-container {
    width: 100%; /* 在小屏幕上宽度为100% */
}
@media (min-width: 768px) { /* 这里的 768px 是一个示例断点，您可以根据需要调整 */
  .pdf-container {
    width: 80%; /* 在大屏幕上宽度为80% */
    height: auto; /* 高度自动 */
    transform: scale(0.75); /* 缩放比例为0.75 */
    transform-origin: top center; /* 变换原点在顶部中心 */
  }
}
</style>

