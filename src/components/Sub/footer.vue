<template>
  <div>
    <footer class="footer">
      <div class="footer-inner">
        <el-row :gutter="20" :justify="'space-around'" :align="'middle'">
            <el-col :span="12">
              <p>聯絡我們：custodyprediction@gmail.com</p>
            </el-col>
            <el-col :span="8">
              <div class="footer-link"><a href="http://www.phys.nthu.edu.tw/~aicmt/index.html" target="_blank">清華大學AIFR研究群</a></div>
              <div class="footer-link"><a href="https://nthuhssai.site.nthu.edu.tw/" target="_blank">清華大學人文社會AI應用與發展研究中心</a></div>
            </el-col>
            <el-col :span="4">
              <img src="/static/logo_nthu.png" width="200" height="40" class="d-inline-block align-top" alt="" loading="lazy" />
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
  font-size: 1rem;
}
.footer-inner {
  width: calc( 90% - 40px );
  margin: auto;
}
.footer-link {
  text-align: right;
  a {
    text-decoration: none;
    transition: 0.4s;
    &:hover {
      color: #F3BB5C;
    }
  }
}
</style>
