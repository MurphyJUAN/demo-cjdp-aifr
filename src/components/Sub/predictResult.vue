<!-- eslint-disable max-len -->
<template>
  <div id="predict-result" class="text-center">
    <div style="z-index: 100" class="w-100">

      <el-row>
        <el-col class="justify-content-center mt-4" :span="24" :xs="24" :sm="24" :md="12" :lg="12" :xl="12" v-for="model in modelUsed[$route.params.mode]" :key="model">
          <!-- <OnlyViolinPlot :predict_result="predict_result" :model_used="model"></OnlyViolinPlot> -->
          <violinPlotMain :predict_result="predict_result" :model_used="model"></violinPlotMain>
        </el-col>
        <!-- <el-col :span="14">
          <div class="p-10 justify-content-center mt-4 mx-20" style="z-index: 100">
            <el-row :gutter="10">
              <el-col :offset="6" :span="6">父親贏得親權的機率(%)</el-col>
              <el-col :span="6">雙方共享親權的機率(%)*</el-col>
              <el-col :span="6">母親贏得親權的機率(%)</el-col>
            </el-row>
            <el-row v-for="model in modelUsed[$route.params.mode]" :key="model" :gutter="10">
              <el-col :span="6">AI模型-{{ model }}</el-col>
              <div v-if="predict_result[model]">
                <el-col :span="6">{{Math.round(predict_result[model]['Applicant']['avg_prob']*100) / 100}} ±{{ predict_result[model]['Applicant']['std'] }}</el-col>
                <el-col :span="6">{{Math.round(predict_result[model]['Both']['avg_prob']*100) / 100}} ±{{ predict_result[model]['Both']['std'] }}</el-col>
                <el-col :span="6">{{Math.round(predict_result[model]['Respondent']['avg_prob']*100) / 100}} ±{{ predict_result[model]['Respondent']['std'] }}</el-col>
              </div>
            </el-row>

          </div>
        </el-col> -->

      </el-row>
      <el-row class="p-10 justify-content-center text-center mt-4 mx-20">
        <div>為了避免使用者過度解讀AI預測的結果，本系統以小提琴圖(Violin Plot)來呈現親權判決預測結果，展示多達100組AI預測結果的機率分布狀態。點數越密集的區域代表越有可能的機率值，小提琴圖也越寬，反之亦然。</div>
        <div>雙方共享親權的結果在不同模型可能差異較大，(*) 可參考<a href="/techDoc">「技術說明</a>」中的「五、模型限制(以判給雙方的情形為例)</div>
      </el-row>

      <!-- <div v-if="isLoading">Calculating... {{elapsedTime}} seconds have elapsed.</div> -->
      <div v-if="errorPrompt">{{errorCode}}</div>
    </div>
  </div>
</template>

<script>
import RadialProgressBar from 'vue-radial-progress';
// import BoxPlot from '../Sub/boxPlot';
import violinPlotMain from './violinPlotMain.vue';

export default {
  components: {
    RadialProgressBar,
    violinPlotMain,
  },
  name: 'PredictResult',
  data() {
    return {
      completedSteps: 5,
      totalSteps: 10,
      modelUsed: {
        mode1: ['L1', 'L2'],
        mode2: ['S1', 'S2'],
        mode3: ['C1', 'C2'],
      },
    };
  },
  props: {
    predict_result: Object,
    elapsedTime: Number,
    isLoading: Boolean,
    errorPrompt: Boolean,
    errorCode: Error,
  },
};
</script>

<style lang="scss" scoped>
.btn {
  color: white;
  background-color: #802a2a;
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
.bold {
  font-weight: bold;
}

.ml-6 {
  margin-left: 10%;
}
</style>
