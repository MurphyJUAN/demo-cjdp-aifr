<template>
    <div class="page-container">
        <div class="Home-title">友善資源連結</div>
        <div class="d-flex flex-row mb-3 flex-wrap">
          <div v-for="link in links" :key="link.name">
            <a :href="link.src" target="_blank">
                <div class="link-block">{{link.name}}</div>
            </a>
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Links',
  data() {
    return {
      links: [
        {
          name: '婚姻諮商服務',
          src: '',
        },
        {
          name: '法律諮詢服務',
          src: '',
        },
        {
          name: '孩童照顧服務',
          src: '',
        },
        {
          name: '就業輔導服務',
          src: '',
        },
        {
          name: '社區支援服務',
          src: '',
        },
        {
          name: '警政便民服務',
          src: '',
        },
        {
          name: '戶政便民服務',
          src: '',
        },
        {
          name: '新住民服務',
          src: '',
        },
      ],
    };
  },
  props: {
  },
  methods: {
  },
};
</script>

<style lang="scss" scoped>
.link-block {
    padding: 10px;
    color: white;
    border-radius: 12px;
    background-color: #7B4F2F;
    text-align: center;
    font-weight: bold;
    font-size: 1.4rem;
    margin: 20px;
    transition: 0.4s;
    width: 12rem;
    &:hover {
        text-decoration: none;
        background-color: #F3BB5C;
        color: #FFF;
    }
}
a {
    text-decoration: none;
}
</style>

