<!-- eslint-disable max-len -->
<template>
  <div id="predict-result" class="text-center">
    <div style="z-index: 100">
      <div class="p-10 justify-content-center mt-4 mx-20" style="z-index: 100">
        <el-row :gutter="10">
          <el-col :offset="6" :span="6">父親贏得親權的機率</el-col>
          <el-col :span="6">雙方共享親權的機率</el-col>
          <el-col :span="6">母親贏得親權的機率</el-col>
        </el-row>
        <el-row v-for="model in modelUsed[$route.params.mode]" :key="model" :gutter="10">
          <el-col :span="6">AI模型-{{ model }}</el-col>
          <div v-if="predict_result[model]">
            <el-col :span="6">{{Math.round(predict_result[model]['Applicant']*100) / 100}}%</el-col>
            <el-col :span="6">{{Math.round(predict_result[model]['Both']*100) / 100}}%</el-col>
            <el-col :span="6">{{Math.round(predict_result[model]['Respondent']*100) / 100}}%</el-col>
          </div>
        </el-row>
      </div>
      <!-- <div v-if="isLoading">Calculating... {{elapsedTime}} seconds have elapsed.</div> -->
      <div v-if="errorPrompt">{{errorCode}}</div>
    </div>
  </div>
</template>

<script>
import RadialProgressBar from 'vue-radial-progress';

export default {
  components: {
    RadialProgressBar,
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
    maxResult: Number,
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
