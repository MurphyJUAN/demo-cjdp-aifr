<template>
  <section id="supplementDescription">
    <!-- <loading
    loader="bars"
    :active.sync="isLoading"
    :can-cancel="true"
    :is-full-page="false" />-->
    <h4 class="px-2">步驟二：補充雙方有利或不利的文字敘述</h4>
    <h6>(請以「當事人」來作主詞，建議父母雙方有利或不利的描述句子的數目儘量相近)</h6>
    <div class="container mt-4" v-visible="true">
      <div class="d-inline-flex w-100 mt-3 row">
        <div class="a-advantage data-outer-box w-100 col-sm-6" style="z-index:100">
          <h4 class="data-title" style="z-index:100">父親之有利條件：</h4>
          <UserInputBlank
            v-on:setDescriptionLists="setAAList"
            :userDescriptionList="userDescriptionList.AA"
            :inputBlankId="1"
          />
        </div>
        <div class="b-advantage data-outer-box w-100 col-sm-6" style="z-index:100">
          <h4 class="data-title" style="z-index:100">母親之有利條件：</h4>
          <UserInputBlank
            v-on:setDescriptionLists="setRAList"
            :userDescriptionList="userDescriptionList.RA"
            :inputBlankId="2"
          />
        </div>
        <div class="a-disadvantage data-outer-box w-100 col-sm-6" style="z-index:100">
          <h4 class="data-title" style="z-index:100">父親之不利條件：</h4>
          <UserInputBlank
            v-on:setDescriptionLists="setADList"
            :userDescriptionList="userDescriptionList.AD"
            :inputBlankId="3"
          />
        </div>
        <div class="b-disadvantage data-outer-box w-100 col-sm-6" style="z-index:100">
          <h4 class="data-title" style="z-index:100">母親之不利條件：</h4>
          <UserInputBlank
            v-on:setDescriptionLists="setRDList"
            :userDescriptionList="userDescriptionList.RD"
            :inputBlankId="4"
          />
        </div>
      </div>
    </div>

    <div class="container" v-visible="visibleSec">
      <h3 class="pt-3" style="z-index:100">發生錯誤</h3>
    </div>
    <div style="z-index:100" v-visible="visible" class="w-100 d-inline-flex justify-content-center">
      <a
        class="btn-lg btn-default btn mr-4"
        @click="cleanAllUserSetting(true)"
        href="javascript:void(0)"
      >清除資料</a>
      <a
        class="btn-lg btn-default btn-navigate"
        @click="predictJudgement()"
        href="javascript:void(0)"
      >申請預測</a>
    </div>
  </section>
</template>

<script>
import Vue from 'vue';
import VueVisible from 'vue-visible';
import UserInputBlank from './userInputBlank';

Vue.use(VueVisible);

export default {
  name: 'SupplementDescription',
  components: {
    UserInputBlank,
  },
  data() {
    return {};
  },
  props: {
    userDescriptionList: Object,
    setAAList: Function,
    setRAList: Function,
    setADList: Function,
    setRDList: Function,
    cleanAllUserSetting: Function,
    predictJudgement: Function,
    visible: Boolean,
    visibleSec: Boolean,
  },
};
</script>

<style lang="scss" scoped>
.container {
  @media (min-width: 1800px) {
    max-width: 1500px;
  }
}
@media (min-width: 800px) {
  .a-advantage,
  .a-disadvantage {
    border-right: solid 1px #282f44;
  }

  .b-advantage,
  .b-disadvantage {
    border-left: solid 1px #282f44;
  }
}
.data-outer-box {
  padding: 10px;
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
.btn-navigate {
  color: white;
  background-color: rgb(226, 145, 60);
  padding: 15px;
  letter-spacing: 2px;
  border-radius: 0px;
  border: none;
  font-weight: 800;
  font-size: 15px;
  transition: background-color 0.2s ease-in-out;
  &:hover {
    background: rgb(74, 163, 175);
  }
}
</style>
