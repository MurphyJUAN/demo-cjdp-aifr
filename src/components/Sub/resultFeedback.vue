<template>
  <section id="ResultFeedback">
    <div id="btn-det">
      <div class="d-inline-flex w-100 justify-content-center">
        <h4 style="z-index: 100">步驟四</h4>
        <div class="ml-4" style="z-index:100">
          <a class="btn-lg btn-default btn" href="javascript:void(0)">結果合理</a>
        </div>
        <div class="ml-4" style="z-index:100">
          <a class="btn-lg btn-default btn" href="javascript:void(0)">結果不合理</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'resultFeedback',
  props: {
    mainIntro: '',
    guide: '',
    isHome: false,
  },
};
</script>

<style lang="scss" scoped>
.container {
  @media (min-width: 1800px) {
    max-width: 2000px;
  }
}
.btn {
  color: white;
  background-color: gray;
  padding: 15px;
  letter-spacing: 2px;
  border-radius: 0px;
  border: none;
  font-weight: 800;
  font-size: 15px;
  transition: background-color 0.2s ease-in-out;
  &:hover {
    background: #d8235e;
  }
}
</style>
