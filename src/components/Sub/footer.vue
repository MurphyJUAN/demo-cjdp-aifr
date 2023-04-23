<template>
  <div>
    <footer class="footer">
      <div class="footer-inner">
        <el-row :gutter="20" justify="space-around">
            <el-col :span="12">
              <p style="line-height: 2rem">聯絡我們：custodyprediction@gmail.com</p>
            </el-col>
            <el-col :span="12">
              <div style="text-align: right"><a href="http://www.phys.nthu.edu.tw/~aicmt/index.html" target="_blank">清華大學AIFR研究群</a></div>
              <div style="text-align: right"><a href="https://nthuhssai.site.nthu.edu.tw/" target="_blank">清華大學人文社會AI應用與發展研究中心</a></div>
            </el-col>
          </el-row>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      backend: [],
      isLoading: false,
      errorPrompt: false,
      errorCode: '',
    };
  },
  props: {
    currentApi: Function,
  },
  methods: {
    getVersion() {
      if (this.backend.length === 0) {
        this.currentApi
          .get('/getVersion')
          .then((response) => {
            this.backend = response.data;
            console.log(this.backend);
          })
          .catch((error) => {
            this.isLoading = false;
            this.errorPrompt = true;
            this.errorCode = error;
            console.log(error);
          });
      }
      return this.backend.version;
    },
  },
};
</script>

<style lang="scss" scoped>
a {
  color: #000;
}
.footer {
  padding: 20px;
  color: #1f191b;
  background-color: #fff;
  position: relative;
  z-index: 99;
  @media (max-width: 768px) {
    height: 100%;
  }
}
.footer-inner {
  width: calc( 90% - 40px );
  margin: auto;
}
</style>
