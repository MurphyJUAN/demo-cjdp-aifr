<template>
  <section id="predict-result">
    <div id="btn-det">
      <div class="w-100 justify-content-center"></div>
    </div>
    <div class="d-none d-md-block" style="z-index: 100">
      <div class="w-100 justify-content-center mt-4" style="z-index: 100">Here are the predicted results from our model:</div>
      <div class="d-inline-flex w-100 justify-content-center mt-4" style="z-index: 100">
        <div>
          <p class="justify-content-center bold" style="text-align: center;">To the party(You):</p>
          <radial-progress-bar :diameter="180"
                       :completed-steps="Math.round(predict_result['Applicant'] * 100) / 100"
                       :total-steps="100"
                       :strokeWidth=20
                       :innerStrokeWidth=10
                       >
            <p style="text-align: center;" :style= "[predict_result['Applicant'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">{{Math.round(predict_result['Applicant'] * 100) / 100}}% </p>
          </radial-progress-bar>
        </div>


        <div class="ml-6">
          <p class="justify-content-center bold" style="text-align: center;">To Both:</p>
          <radial-progress-bar :diameter="180"
                       :completed-steps="Math.round(predict_result['Both'] * 100) / 100"
                       :total-steps="100"
                       :strokeWidth=20
                       :innerStrokeWidth=10
                       startColor=#42FCFF
                       stopColor=#6A37E1>
            <p style="text-align: center;" :style= "[predict_result['Both'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">{{Math.round(predict_result['Both'] * 100) / 100}}% </p>
          </radial-progress-bar>
        </div>

        <div class="ml-6">
          <p class="justify-content-center bold" style="text-align: center;">To the other party:</p>
          <radial-progress-bar :diameter="180"
                       :completed-steps="Math.round(predict_result['Respondent'] * 100) / 100"
                       :total-steps="100"
                       :strokeWidth=20
                       :innerStrokeWidth=10
                       startColor=#F9BC67
                       stopColor=#A44404>
            <p style="text-align: center;" :style= "[predict_result['Respondent'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">{{Math.round(predict_result['Respondent'] * 100) / 100}}% </p>
          </radial-progress-bar>
        </div>


        <!-- <h5 :style= "[predict_result['Applicant'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">Custody awarded to the party(you): {{Math.round(predict_result['Applicant'] * 100) / 100}}%</h5>
        <h5 class="ml-3" :style= "[predict_result['Respondent'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">Custody awarded to the other party: {{Math.round(predict_result['Respondent']*100) / 100}}%</h5>
        <h5 class="ml-3" :style= "[predict_result['Both'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">Custody awarded to both： {{Math.round(predict_result['Both']*100) / 100}}%</h5> -->
      </div>
      <!-- <div v-if="isLoading">Calculating... {{elapsedTime}} seconds have elapsed.</div> -->
      <div v-if="errorPrompt">{{errorCode}}</div>
      <h6 class="mt-2">(We suggest trying different phrasing or enlisting the help of an impartial third party for input. If you have any feedback or suggestions, please feel free to email us.)</h6>
    </div>
    <div class="d-md-none" style="z-index: 100">
      <div class="w-100 justify-content-center mt-4" style="z-index: 100">
        <h5 :style= "[predict_result['Applicant'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">
          Custody awarded to the party(you): {{Math.round(predict_result['Applicant']*100) / 100}}%
        </h5>
        <h5 class="ml-3 mt-3" :style= "[predict_result['Respondent'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">
          Custody awarded to the other party: {{Math.round(predict_result['Respondent']*100) / 100}}%
        </h5>
        <h5 class="ml-3 mt-3" :style= "[predict_result['Both'] == maxResult ? {'color': '#FF5C59', 'font-weight': 'bold', 'text-decoration': 'underline'} : {'color': 'black', 'font-weight': 'normal', 'text-decoration': 'none'}]">
          Custody awarded to both： {{Math.round(predict_result['Both']*100) / 100}}%
        </h5>
      </div>
      <!-- <div v-if="isLoading">Calculating... {{elapsedTime}} seconds have elapsed.</div> -->
      <div v-if="errorPrompt">{{errorCode}}</div>
      <h6 class="mt-2">(We suggest trying different phrasing or enlisting the help of an impartial third party for input. If you have any feedback or suggestions, please feel free to email us.)</h6>
    </div>
  </section>
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
