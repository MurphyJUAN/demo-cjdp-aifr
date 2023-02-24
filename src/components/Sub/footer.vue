<template>
  <footer class="footer">
    <div class="row">
      <div class="col">
        <p class="mt-2">聯絡方式：custodyprediction@gmail.com</p>
      </div>
      <div class="col">
        <p class="mt-2">版本：v0.3.3 後端版本：{{getVersion()}}</p>
      </div>
    </div>
  </footer>
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
.footer {
  line-height: 35px;
  text-align: center;
  color: #1f191b;
  background-color: #fff;
  position: relative;
  z-index: 99;
  @media (max-width: 768px) {
    height: 100%;
  }
}
</style>
