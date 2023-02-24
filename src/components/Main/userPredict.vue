<template>
  <div>
    <div class="jumbotron" id="Home">
      <div class="inner">
        <h1 class="py-3 Home-title" style="z-index:100">判決預測系統</h1>
        <UserGuide :guide="guide" :inHome="false" />

        <!-- <v-select :options="options"></v-select> -->
      </div>
    </div>
    <!-- <GenderAndCountrySelector v-on:listenGenderCountry="listenGenderCountry" /> -->
    <checkboxGroup :checkboxSentences="checkboxSentences" :setDescriptionData="setDescriptionData" />
    <SupplementDescription
      :userDescriptionList="userDescriptionList"
      :setAAList="setAAList"
      :setRAList="setRAList"
      :setADList="setADList"
      :setRDList="setRDList"
      :predictJudgement="predictJudgement"
      :visible="visible"
      :visibleSec="visibleSec"
      :cleanAllUserSetting="cleanAllUserSetting"
    />
    <PredictResult
      id="predictResult"
      :predict_result="predict_result"
      :elapsedTime="elapsedTime"
      :isLoading="isLoading"
      :errorPrompt="errorPrompt"
      :errorCode="errorCode"
    />
    <div class="back-top" v-if="backTop" @click="backToTop()">
      <i class="fas fa-chevron-up"></i>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueVisible from 'vue-visible';
import VueLoading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import UserGuide from '../Sub/userGuide';
import GenderAndCountrySelector from '../Sub/genderAndCountrySelect';
import CheckboxGroup from '../Sub/checkboxGroup';
import SupplementDescription from '../Sub/supplementDescription';
import PredictResult from '../Sub/predictResult';

Vue.use(VueVisible);

export default {
  name: 'userPredict',
  components: {
    loading: VueLoading,
    UserGuide,
    GenderAndCountrySelector,
    CheckboxGroup,
    SupplementDescription,
    PredictResult,
  },
  props: {
    currentApi: Function,
  },
  data() {
    const emptyDescriptionList = { AA: [], RA: [], AD: [], RD: [] };

    return {
      visible: true,
      visibleSec: false,
      backTop: false,
      isLoading: false,
      backend: [],
      isLoading: false,
      errorPrompt: false,
      errorCode: new Error(),
      emptyTestJudgement: emptyDescriptionList,
      testJudgement: {},
      userDescriptionList: JSON.parse(JSON.stringify(emptyDescriptionList)),
      predict_result: [],
      elapsedTime: 0,
      checkboxSentences: [
        {
          type: '經濟工作情況',
          item: [
            {
              content:
                '當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '孩童個人意願',
          item: [
            {
              content:
                '當孩子對於與家庭成員間互動，何者能給予其安全、滿足之心理環境及生活照顧，已有判斷能力。有表達與當事人共同生活之意願。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '孩子年紀已經夠大，已能了解家庭成員互動的關係，意願上比較不希望與當事人同住。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '平日相處關係',
          item: [
            {
              content:
                '孩童對當事人於雙方婚姻存續期間之諸多作為感到嫌惡，並因當事人離異時造成心靈傷害，而與之關係疏離、緊張。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '孩子對當事人有一定程度的依賴感及安全感存在。例如孩子會直接對當事人撒嬌求助，並且得到安撫。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '主要照顧者',
          item: [
            {
              content:
                '當事人目前為孩子之主要照顧者，並能提供穩定生活及正向發展，並無受不當照顧情形，與當事人互動情形亦良好。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人目前並非與孩子同住，或者並非孩子生活的主要照顧者，對其個性、生活所需上了解可能不足。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '居住環境評估',
          item: [
            {
              content:
                '當事人住處的社區環境足以提供食衣住行育樂的活動安排，而內部居家環境的設備完善，環境寬敞且乾淨整潔，合適孩子居住。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人的居住地點附近環境複雜，且屋內並無孩子獨立的失活空間，居家環境不太適合孩子成長。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '親友支持系統',
          item: [
            {
              content:
                '當事人的其他親戚朋友並未同住或少有往來，與孩子的關係陌生，無法提供足夠的支持系統。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人的家人親戚亦住在附近或同住，可以協助支援孩子的照顧。孩子與其互動亦自然和諧。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '過往陪伴經驗',
          item: [
            {
              content:
                '當事人能夠具體陳述對孩子之教育理念及教養態度，且皆會於休假及空閒時，陪伴子女外出遊玩，培養親子互動。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人過往在家庭生活中因為工作或個性，比較少陪伴孩子與之相處，亦不太了解其生活狀況。孩子與之單獨相處會有焦慮。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '友善父母觀念',
          item: [
            {
              content: '當事人願意讓對方探視孩子，繼續維繫親子關係。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content: '當事人不願意或阻撓對方探視孩子或任何接觸。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
        {
          type: '其他相關描述',
          item: [
            {
              content:
                '當事人爭取撫養孩子親權之意願積極，動機是希望陪伴孩子在較好的環境中成長。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人若單獨撫養孩子，因為工作關係，可能沒有時間管教，會繼續放任其偏差之行為，不利於孩子的成長與發展。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '孩子現仍處於嬰幼階段，亟需母親的關愛照顧，而當事人長期與其共同生活，對其人格特質、身心發展狀況及生活需求甚為瞭解。',
              attr: 'A',
              applicantChecked: false,
              respondentChecked: false,
            },
            {
              content:
                '當事人工作的時間不穩定，長需要夜間輪班工作。孩子現尚幼小，故配合當事人活動尚可，但日後恐會影響到就學及生活作息。',
              attr: 'D',
              applicantChecked: false,
              respondentChecked: false,
            },
          ],
        },
      ],
      genderValue: '',
      guide:
        '一、本判決預測系統假定雙方都是有意願爭取孩子的撫養權。請按以下步驟輸入相關資料，進行判決預測。<br>二、任何預測結果都可能因為輸入條件與訓練資料的限制而有所不足，所以僅以機率為參考，並<b>不具備任何法律效力，仍應<u>以法院的裁定為最後依據</u></b>。<br>三、本判決預測系統不會記錄任何輸入資料。<br>四、本系統仍持續改善中，歡迎提供給我們改善的意見，持續調整此系統。',
    };
  },
  methods: {
    backToTop() {
      const element = document.getElementById('appNavbar');
      element.scrollIntoView();
    },
    handleScroll() {
      // 改变元素#searchBar的top值
      const scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > 100) {
        this.backTop = true;
      } else {
        this.backTop = false;
      }
    },
    listenGenderCountry(genderValue) {
      this.genderValue = genderValue;
    },
    setAAList(descriptionList, removedItems) {
      this.userDescriptionList.AA = descriptionList;
      for (let i = 0; i < removedItems.length; i++) {
        // console.log(removedItems[i].checkboxIndex)
        if (removedItems[i].checkboxIndex !== 'none') {
          this.checkboxSentences[removedItems[i].groupIndex].item[
            removedItems[i].checkboxIndex
          ].applicantChecked = false;
        }
      }
    },
    setRAList(descriptionList, removedItems) {
      this.userDescriptionList.RA = descriptionList;
      for (let i = 0; i < removedItems.length; i++) {
        // console.log(removedItems[i].checkboxIndex)
        if (removedItems[i].checkboxIndex !== 'none') {
          this.checkboxSentences[removedItems[i].groupIndex].item[
            removedItems[i].checkboxIndex
          ].respondentChecked = false;
        }
      }
    },
    setADList(descriptionList, removedItems) {
      this.userDescriptionList.AD = descriptionList;
      for (let i = 0; i < removedItems.length; i++) {
        // console.log(removedItems[i].checkboxIndex)
        if (removedItems[i].checkboxIndex !== 'none') {
          this.checkboxSentences[removedItems[i].groupIndex].item[
            removedItems[i].checkboxIndex
          ].applicantChecked = false;
        }
      }
    },
    setRDList(descriptionList, removedItems) {
      this.userDescriptionList.RD = descriptionList;
      for (let i = 0; i < removedItems.length; i++) {
        // console.log(removedItems[i].checkboxIndex)
        if (removedItems[i].checkboxIndex !== 'none') {
          this.checkboxSentences[removedItems[i].groupIndex].item[
            removedItems[i].checkboxIndex
          ].respondentChecked = false;
        }
      }
    },
    setDescriptionData(groupIndex, checkboxIndex) {
      const item = this.checkboxSentences[groupIndex].item[checkboxIndex];
      const record = { content: item.content, groupIndex, checkboxIndex };

      // console.log(checkboxIndex);
      // console.log(item);
      // console.log(record);

      if (this.userDescriptionList.length === 0) {
        this.userDescriptionList = JSON.parse(
          JSON.stringify(this.emptyTestJudgement),
        );
      }

      if (item.attr === 'A') {
        for (var i = 0; i < this.userDescriptionList.AA.length; i++) {
          if (
            this.userDescriptionList.AA[i].groupIndex === groupIndex &&
            this.userDescriptionList.AA[i].checkboxIndex === checkboxIndex
          ) {
            break;
          }
        }
        if (item.applicantChecked) {
          if (i === this.userDescriptionList.AA.length) {
            this.userDescriptionList.AA.push(record);
          }
        } else if (i !== this.userDescriptionList.AA.length) {
          this.userDescriptionList.AA.splice(i, 1);
        }

        for (var i = 0; i < this.userDescriptionList.RA.length; i++) {
          if (
            this.userDescriptionList.RA[i].groupIndex === groupIndex &&
            this.userDescriptionList.RA[i].checkboxIndex === checkboxIndex
          ) {
            break;
          }
        }
        if (item.respondentChecked) {
          if (i === this.userDescriptionList.RA.length) {
            this.userDescriptionList.RA.push(record);
          }
        } else if (i !== this.userDescriptionList.RA.length) {
          this.userDescriptionList.RA.splice(i, 1);
        }
      } else if (item.attr === 'D') {
        for (var i = 0; i < this.userDescriptionList.AD.length; i++) {
          if (
            this.userDescriptionList.AD[i].groupIndex === groupIndex &&
            this.userDescriptionList.AD[i].checkboxIndex === checkboxIndex
          ) {
            break;
          }
        }
        if (item.applicantChecked) {
          if (i === this.userDescriptionList.AD.length) {
            this.userDescriptionList.AD.push(record);
          }
        } else if (i !== this.userDescriptionList.AD.length) {
          this.userDescriptionList.AD.splice(i, 1);
        }

        for (var i = 0; i < this.userDescriptionList.RD.length; i++) {
          if (
            this.userDescriptionList.RD[i].groupIndex === groupIndex &&
            this.userDescriptionList.RD[i].checkboxIndex === checkboxIndex
          ) {
            break;
          }
        }
        if (item.respondentChecked) {
          if (i === this.userDescriptionList.RD.length) {
            this.userDescriptionList.RD.push(record);
          }
        } else if (i !== this.userDescriptionList.RD.length) {
          this.userDescriptionList.RD.splice(i, 1);
        }
      }

      // console.log('userDescriptionList');
      // console.log(this.userDescriptionList);
    },
    prepareTestData() {
      this.predict_result = [];
      this.testJudgement = JSON.parse(JSON.stringify(this.emptyTestJudgement));

      // console.log(Object.entries(Object.keys(this.userDescriptionList)));
      for (const [index, key] of Object.entries(
        Object.keys(this.userDescriptionList),
      )) {
        // console.log(key);
        for (let i = 0; i < this.userDescriptionList[key].length; i++) {
          this.testJudgement[key].push(
            this.userDescriptionList[key][i].content,
          );
        }
      }

      console.log('testJudgement');
      console.log(this.testJudgement);
    },
    predictJudgement() {
      const element = document.getElementById('predictResult');
      element.scrollIntoView();
      // document.getElementById('btn-det').scrollIntoView(true);
      this.isLoading = true;
      this.visible = false;
      this.errorPrompt = false;
      // let interval_handle = null;
      let checkTimeoutHandle = null;
      let getTimeElapsedHandle = null;
      let cancelState = {isCanceled: false, counter: 0};

      const tStart = new Date().getTime();

      const getTimeElapsed = (startTime, period) =>
        setInterval(() => {
          const endTime = new Date().getTime();
          this.elapsedTime = (endTime - startTime) / 1000;
          // console.log(this.elapsedTime);
        }, period);

      let cancelCallback = () => {};

      let setCancelCallbackPromise = (cancelState) => {
          return new Promise((resolve, reject) => {
              // set cancelCallback when running this promise
              cancelCallback = (cancelState) => {
                  console.log("cancelCallback", cancelState.counter++);
                  console.log("cancelState.isCanceled", cancelState.isCanceled);
                  cancelState.isCanceled = true;
                  // pass cancel messages
                  return reject('Canceled');
              };
              if (cancelState.isCanceled === true){
                cancelCallback(cancelState);
              }
          })
      }

      const checkStatus = (random_id, period, message, setCancelCallbackPromise, cancelState) => {
        console.log(period, message);

        Promise.race([this.currentApi.post('/getStatus', {random_id}), setCancelCallbackPromise(cancelState)])
        // this.currentApi.post('/getStatus', {random_id})
        .then((response) => {
          console.log(response.data.random_id);
          console.log(response.data.messages);
          console.log(response.data.classes);

          for (const key in response.data.classes) {
            this.$set(
              this.predict_result,
              key,
              Math.round(response.data.classes[key] * 100),
            );
          };
          setTimeout(() => {
            checkStatus(random_id, period * 1.5, message, setCancelCallbackPromise, cancelState);
          }, period);
        })
        .catch((error) => {
          console.log(error)
        })
      }

      // const checkStatusWithInterval = (random_id, period, message, timeout) =>
      //   self_handle = setInterval(() => {
      //     console.log(period, message);
      //     Promise.race([this.currentApi.post('/getStatus', {random_id}), checkTimeoutPromise(500, timeout)])
      //       .then((response) => {
      //         console.log(response.data.random_id);
      //         console.log(response.data.messages);
      //         console.log(response.data.classes);
      //         clearInterval(self_handle)
      //         for (const key in response.data.classes) {
      //           this.$set(
      //             this.predict_result,
      //             key,
      //             Math.round(response.data.classes[key] * 100),
      //           );
      //         }
      //       })
      //       .catch((error) => {
      //         clearInterval(self_handle)
      //       });
      //   }, period);

      const checkTimeoutPromise = (period, timeout) => {
        return new Promise((resolve, reject) => {
          timeout = timeout / 1000;
          // 傳入 resolve 與 reject，表示資料成功與失敗
          checkTimeoutHandle = setInterval(() => {
            // console.log(this.elapsedTime);
            if ( this.elapsedTime >= timeout ){
              // console.log("debug");
              // clearInterval(getTimeElapsedHandle);
              clearInterval(checkTimeoutHandle)
              // 回傳失敗
              reject(new Error("timeout"));
            }
          }, period);
        });
      }

      // prepare test data from user input(just after check status timer)
      this.prepareTestData();

      // checkTimeHandle = checkTimeElapsed(tStart, 250);
      getTimeElapsedHandle = getTimeElapsed(tStart, 250);

      // send request and receive prediction result
      this.currentApi.get('/getRandomId')
        .then((response) => {
          // console.log("debug2");
          console.log(response.data);
          // interval_handle = checkStatusWithInterval(
          //   response.data.random_id,
          //   2000,
          //   'check status...',
          // );

          setTimeout(() => {
            checkStatus(
              response.data.random_id,
              1000,
              'check status...',
              setCancelCallbackPromise,
              cancelState
            );
          }, 0);

          return Promise.race([
            this.currentApi.post('/predictJudgement', {
              text: this.testJudgement,
              random_id: response.data.random_id,
            }), checkTimeoutPromise(500, 20000)
          ]);
        })
        .then((response) => {
          this.isLoading = false;
          this.visible = true;
          console.log(response.data);
          // const data = response.data.classes;
          // this.Applicant = Math.round(data.Applicant * 100);
          // this.Respondent = Math.round(data.Respondent * 100);
          // this.Both = Math.round(data.Both * 100);
          // this.predict_result = response.data.classes;
          // clearInterval(interval_handle);
          clearInterval(getTimeElapsedHandle);
          // clearInterval(checkTimeoutHandle);
          // cancelState.isCanceled = true;
          cancelCallback(cancelState);

          console.log(this.predict_result);
          for (const key in response.data.classes) {
            // console.log(key);
            this.predict_result[key] = Math.round(
              response.data.classes[key] * 100,
            );
          }
          // console.log(this.predict_result);
          // console.log(response.data.classes);
          // console.log(this.advantage, this.disadvantage, this.neutral);
          // const similarText = response.data.similar_text;
          // this.similar_text = similarText;
          // console.log(this.similar_text);
        })
        .catch((error) => {
          this.isLoading = false;
          this.visible = true;
          this.errorPrompt = true;
          this.errorCode = error;
          console.log(error);
          // clearInterval(interval_handle);
          clearInterval(getTimeElapsedHandle);
          // clearInterval(checkTimeoutHandle);
          // cancelState.isCanceled = true;
          cancelCallback(cancelState);
        });
    },
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
    cleanAllUserSetting(childIsReset) {
      const confirmResult = confirm('您確定要清除所有資訊了嗎？');
      const emptyDescriptionList = { AA: [], RA: [], AD: [], RD: [] };
      if (childIsReset && confirmResult) {
        this.testJudgement = {};
        this.userDescriptionList = JSON.parse(
          JSON.stringify(emptyDescriptionList),
        );
        this.predict_result = [];
        for (let i = 0; i < this.checkboxSentences.length; i += 1) {
          for (let j = 0; j < this.checkboxSentences[i].item.length; j += 1) {
            this.checkboxSentences[i].item[j].applicantChecked = false;
            this.checkboxSentences[i].item[j].respondentChecked = false;
          }
        }
      }
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
@import "vue-select/src/scss/vue-select.scss";
@import "~bootstrap/scss/_functions";
@import "~bootstrap/scss/_variables";
@import "~bootstrap/scss/mixins/_breakpoints";

* {
  position: relative;
  font-family: 微軟正黑體;
}

.web-body {
  overflow: hidden;
}

.container {
  @media (min-width: 1800px) {
    max-width: 1500px;
  }
}

.pinkCircle {
  position: absolute;
  width: 80vh;
  height: 80vh;
  z-index: 90;
  left: -20vh;
}
.blueCircle {
  position: absolute;
  width: 80vh;
  height: 80vh;
  z-index: 90;
  right: -20vh;
  top: 60vh;
}
.yellowBar {
  position: absolute;
  z-index: 90;
  height: 80vh;
  left: 20px;
  bottom: 30vh;
  transform: rotate(-45deg);
}
.purpleBar {
  position: absolute;
  z-index: 90;
  height: 80vh;
  right: 20px;
  bottom: 20vh;
  transform: rotate(-20deg);
}

ul {
  list-style-type: decimal;
  line-height: 35px;
  @media screen and (max-width: 700px) {
    padding-left: 0px;
    padding-right: 10px;
  }
}

.description {
  letter-spacing: 4px;
  line-height: 35px;
}

.test-number {
  color: gray;
  line-height: 30px;
}

.back-top {
  width: 60px;
  height: 60px;
  background-color: hsla(5, 76%, 62%, 0.8);
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  color: white;
  line-height: 60px;
  z-index:101;
}
.jumbotron {
  margin-bottom: 0px;
  padding-bottom: 0px;
  border-radius: 0px;
}

#only-sentence {
  @media (min-width: 500px) {
    max-width: 220px;
  }
  border-radius: 5px;
  border: solid 1px #bbbbbbad;
  padding: 10px;
  background-color: transparent;
  color: black;
}

input,
textarea {
  border-width: 1.5px;
  border-style: inset;
  border-color: gray;
}

li {
  text-align: left;
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

.navbar {
  background-color: #f7f7f7;
  box-shadow: 0 0 0.1em 0 rgba(0, 0, 0, 0.25);
  a {
    color: black;
    font-weight: 800;
    font-size: 50px;
  }
}

#Home {
  background-color: #f7f7f7;
  overflow: hidden;
  height: 100%;
  position: relative;
  color: black;
}

.Home-title {
  color: black;
}

section {
  position: relative;
  padding-top: 2rem;
  padding-bottom: 2rem;
  background-color: #f7f7f7;
  color: black;
}

.test-result {
  font-weight: 800;
}

.none-title {
  color: gray;
}
.user-instruction {
  z-index: 100;
  line-height: 35px;
  letter-spacing: 4px;
  // margin-left: 50%;
  // transform: translateX(-50%);
  text-align: left;
  margin-top: -25px;
}
</style>
