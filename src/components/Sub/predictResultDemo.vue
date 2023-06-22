<!-- eslint-disable max-len -->
<template>

    <div id="predict-result" class="text-center">
        <el-row justify="space-around align-center" type="flex">
            <div class="violin-plot" ref="violinPlot">
                <ViolinPlot :predict_result="predict_result"></ViolinPlot>
            </div>
            <div>
                <!-- Summary -->
                {{  }}
                <div class="summary-card" ref="summaryCard">
                    <div class="content-container">
                        <div class="summary-sub-title mb-1">MOST LIKELY OUTCOME & CONFIDENCE LEVEL</div>
                        <div class="summary-main-title mb-3">Custody Granted To:
                            <span v-if="predict_result.granted === 'plaintiff'">聲請方(Plaintiff)</span>
                            <span v-if="predict_result.granted === 'defendant'">相對方(Defendant)</span>
                            <span v-if="predict_result.granted === 'both'">雙方(Both)</span></div>
                            <div class="progress-bar mb-2">
                            <div class="progress-bar-inner" :style="innerBarStyles"></div>
                        </div>
                    </div>

                    <el-row class="icon-text">
                        <img v-if="predict_result.confidence[this.predict_result.granted] >= maxConfidence" class="icon-face" src="../../../static/smile.png" />
                        <img v-if="predict_result.confidence[this.predict_result.granted] < maxConfidence &&
                        predict_result.confidence[this.predict_result.granted] >= minConfidence" class="icon-face" src="../../../static/neutral-face.png" />
                        <img v-if="predict_result.confidence[this.predict_result.granted] < minConfidence" class="icon-face" src="../../../static/sad.png" />
                        <span class="ml-2 confidence-text" style="color: #46A759" v-if="predict_result.confidence[this.predict_result.granted] >= maxConfidence">High Confidence: <span class="confidence-num">{{ predict_result.confidence[this.predict_result.granted]}}%</span></span>
                        <span class="ml-2 confidence-text" style="color: #FFA11D" v-if="predict_result.confidence[this.predict_result.granted] < maxConfidence &&
                        predict_result.confidence[this.predict_result.granted] >= minConfidence">Moderate Confidence: <span class="confidence-num">{{ predict_result.confidence[this.predict_result.granted]}}%</span></span>
                        <span class="ml-2 confidence-text" style="color: #D5494F" v-if="predict_result.confidence[this.predict_result.granted] < minConfidence">Low Confidence: <span class="confidence-num">{{ predict_result.confidence[this.predict_result.granted]}}%</span></span>

                    </el-row>
                </div>
            </div>
        </el-row>


      <!-- <div style="z-index: 100">
        <div class="p-10 justify-content-center mt-4 mx-20" style="z-index: 100">
          <el-row :gutter="10">
            <el-col :offset="6" :span="6">父親贏得親權的機率(%)</el-col>
            <el-col :span="6">雙方共享親權的機率(%)</el-col>
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
        <div v-if="errorPrompt">{{errorCode}}</div>
      </div> -->
    </div>
  </template>

<script>
// import VueApexCharts from 'vue-apexcharts';
import RadialProgressBar from 'vue-radial-progress';
import ViolinPlot from '../Sub/violinPlot';

export default {
  components: {
    RadialProgressBar,
    ViolinPlot,
    // VueApexCharts,
  },
  name: 'PredictResultDemo',
  data() {
    return {
      maxConfidence: 77.88,
      minConfidence: 30.11,
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
  methods: {
  },
  computed: {
    innerBarStyles() {
      let backgroundColor = '#46A759';
      if (this.predict_result.confidence[this.predict_result.granted] < this.minConfidence) {
        backgroundColor = '#D5494F';
      } else if (this.predict_result.confidence[this.predict_result.granted] < this.maxConfidence) {
        backgroundColor = '#FFA11D';
      }

      return {
        width: `${this.predict_result.confidence[this.predict_result.granted]}%`,
        backgroundColor,
      };
    },
  },
  mounted() {
    this.$nextTick(() => {
      const violinPlotHeight = this.$refs.violinPlot.offsetHeight;
      const summaryCard = this.$refs.summaryCard;
      summaryCard.style.height = `${violinPlotHeight}*0.8px`;
    });
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

  .summary {
    display: grid;
    align-items: center;
    justify-content: center; /* 水平置中，如需 */
    height: 100%; /* 需要有高度才能使垂直置中生效 */
  }

  .green {
    margin-top: 1rem;
    width: 0.8rem;
    height: 0.8rem;
    background-color:green;
    border-radius: 100%;
  }
  .red {
    margin-top: 1rem;
    width: 0.8rem;
    height: 0.8rem;
    background-color:red;
    border-radius: 100%;
  }
.align-center {
    align-items: center;
}
.summary-card {
    background: white;
    height: 300px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius: 10px;
    text-align: left;
    display: flex;
    flex-direction: column; /* 如果你的内容是垂直堆叠的 */
    align-items: flex-start; /* 对齐到左侧 */
    justify-content: center;
}
.content-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    // align-items: center;
    width: 100%; /* 宽度为100%来确保内容的居中 */
}

.summary-sub-title {
    color: #737373;
}

.summary-main-title {
    font-weight: bold;
    font-size: 1.3rem;
}

.progress-bar {
  width: 100%;
  background-color: #f3f3f3;
  border-radius: 5px;
}

.progress-bar-inner {
  height: 20px;
  border-radius: 5px;
}

.icon-face {
    width: 1rem;
    height: 1rem;
}

.confidence-text {
    font-weight: bold;
}

.confidence-num {
    font-size: 3.5rem;
}
  </style>

