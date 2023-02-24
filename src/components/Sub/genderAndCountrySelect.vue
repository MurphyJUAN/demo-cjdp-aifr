<template>
  <section id="basic-info">
    <h4 class="px-2">步驟一：勾選雙方的基本資料</h4>
    <h6>(此部分目前暫時不在訓練範圍，所以不會影響預測結果</h6>
    <div class="container mt-4">
      <div class="d-inline-flex w-100 mt-3 row justify-content-center">
        <div class="data-outer-box w-100 col-sm-6" style="z-index:100">
          <div class="mt-3 pl-4 pr-2" style="z-index:100">
            <div class="w-100 d-inline-flex">
              <h5 class="w-100">聲請方與相對方身份：</h5>
              <el-select
                class="w-100"
                v-model="genderValue"
                placeholder="請選擇身份"
                @change="sendGender()"
              >
                <el-option
                  v-for="item in genderOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                ></el-option>
              </el-select>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'GenderAndCountrySelect',
  data() {
    return {
      genderValue: '',
      genderOptions: [
        {
          value: 'a',
          label: '聲請方為女性，相對方為男性',
        },
        {
          value: 'b',
          label: '聲請方為男性，相對方為女性',
        },
      ],
    };
  },
  methods: {
    sendGender() {
      this.$emit('listenGenderCountry', this.genderValue);
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
