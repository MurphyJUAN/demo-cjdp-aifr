<!-- eslint-disable max-len -->
<template>
  <div class="page-container">
    <div class="predict-container">
      <div class="page-title">{{ pageText[$route.params.mode].title }}</div>
      <div class="shadow-none p-2 mb-2 rounded quote">{{ pageText[$route.params.mode].instruction }}</div>
      <div v-loading="isLoading">
        <router-view @resultUpdate="updateResult" @updatePrePredict="updatePrePredict" ref="groupForm"/>
      </div>
      <div class="shadow-none p-2 mb-2">{{ pageText[$route.params.mode].note }}</div>
      <el-row :gutter="20">
        <el-col :span="12">
          <div class="predict-btn" style="background-color:#5A4D30; float:right;" @click="clearAllStatement()">全部清除</div>
        </el-col>
        <el-col :span="12">
          <div class="predict-btn" style="background-color:#F3BB5C" @click="startPredict()">申請預測</div>
        </el-col>
        <el-col :span="24" class="justify-content-center d-flex mt-2" v-if="showButton">
          <div class="random-btn" @click="getTestCase()">
            <img class="shuffle-icon mr-2" src="../../../static/shuffle.png" />
            <span>隨機挑選案例</span>
          </div>
        </el-col>
        <el-col v-if="showButton" class="justify-content-center text-align-center">
          <p>Label:{{ ground_truth }}</p>
          <p>ID: {{ ID }}</p>
          <p>AA: {{ result.data.AA }}</p>
          <p>AD: {{ result.data.AD }}</p>
          <p>RA: {{ result.data.RA }}</p>
          <p>RD: {{ result.data.RD }}</p>
        </el-col>
        <el-col :span="24">
          <PredictResult
            v-if="isStartPredict"
            class="predictResult"
            :predict_result="predict_result"
            :elapsedTime="elapsedTime"
            :isLoading="isLoading"
            :errorPrompt="errorPrompt"
            :errorCode="errorCode"
            :maxResult="maxResult"
          />
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PredictResult from '../Sub/predictResult';

export default {
  name: 'UserPredict',
  components: {
    PredictResult,
  },
  data() {
    return {
      showButton: false,
      ID: '',
      ground_truth: '',
      predict_result: { Applicant: 0, Respondent: 0, Both: 0 },
      elapsedTime: 0,
      maxResult: 0,
      isLoading: false,
      isStartPredict: false,
      errorPrompt: false,
      errorCode: new Error(),
      pageText: {
        mode1: {
          title: '模式一：選項輸入',
          instruction: '使用者需要勾選對於爭取親權的有利或不利因素選項，讓AI模型作親權酌定判決預測。使用者可從表單中勾選13項參考因素中相符的(可複選)來作輸入資料。此因素的排列順序是依過往親權酌定案件中最常出現的依次來排，僅為方便使用者選擇，與重要性無關，亦不必完全選出。本模式的優點是可快速勾選，缺點是需判斷分類。準確度：75%-77%。',
          note: '提醒：本系統目前提供兩種AI模型預測，若結果差異過大可能代表此個案不容易有效預測，請再嘗試提供更細緻的描述，重新預測。兩個模型的原理與比較請見技術說明分頁。',
        },
        mode2: {
          title: '模式二：文字輸入',
          instruction: '使用者需對於爭取親權的有利或不利的相關理由作文字輸入，讓AI模型作親權酌定判決預測。使用者可先從輸入框中的範例文字來選擇最接近的作輸入資料，然後調整成最接近使用者個案的狀況描述。為避免誤導，每個輸入框描述的主詞儘量都用「當事人」。本模式的優點是可直接文字輸入不分類，缺點是輸入需時較久不易完整。準確度：83%-88%。',
          note: '提醒：本系統目前提供兩種AI模型預測，若結果差異過大可能代表此個案不容易有效預測，請再嘗試提供更細緻的描述，重新預測。兩個模型的原理與比較請見技術說明分頁。',
        },
        mode3: {
          title: '模式三：選項加文字輸入',
          instruction: '使用者需要「同時」勾選因素選項並輸入相關的文字敘述，讓AI模型作親權酌定判決預測。使用者可從表單中勾選13項參考因素中相符的(可複選)來作輸入資料或範例文字中選擇合適的填入再修改(亦可自行填入文字)。本模式的優點是準確度最高(特別是對共同親權)，缺點是輸入需時最久且需要判斷分類。準確度：86%-90%。',
          note: '提醒：本系統目前提供兩種AI模型預測，若結果差異過大可能代表此個案不容易有效預測，請再嘗試提供更細緻的描述，重新預測。兩個模型的原理與比較請見技術說明分頁。',
        },
      },
      resultConfig: [
        { title: 'The statements favorable to the party(you)', title_f: 'The factors favorable to the party(you)', type: 'A', key: 'AA', dialog: false },
        { title: 'The statements unfavorable to the party(you)', title_f: 'The factors unfavorable to the party(you)', type: 'D', key: 'AD', dialog: false },
        { title: 'The statements favorable to the other party', title_f: 'The factors favorable to the other party', type: 'A', key: 'RA', dialog: false },
        { title: 'The statements unfavorable to the other party', title_f: 'The factors unfavorable to the other party', type: 'D', key: 'RD', dialog: false },
      ],
      features: [
        { label: '親子感情 Parent-Child Affection', value: '親子感情' },
        { label: '意願能力 Parent\'s WIllingness and Capability', value: '意願能力' },
        { label: '父母經濟 Parent\'s Financial Status', value: '父母經濟' },
        { label: '支持系統 Supporting System', value: '支持系統' },
        { label: '父母生活 Parent\'s Living Condition', value: '父母生活' },
        { label: '主要照顧 Primary Caregiver', value: '主要照顧' },
        { label: '子女年齡 Child\'s Age', value: '子女年齡' },
        { label: '人格發展 Child\'s Development', value: '人格發展' },
        { label: '父母健康 Parent\'s Health Satus', value: '父母健康' },
        { label: '父母職業 Parent\'s Occupation', value: '父母職業' },
        { label: '子女意願 Child\'s Willingness', value: '子女意願' },
        { label: '友善父母 Parent\'s Friendliness to the Other', value: '友善父母' },
        { label: '父母品行 Parent\'s Character', value: '父母品行' },
      ],
      sentencesExample: {
        A: [
          {
            type: '經濟工作情況',
            item: [{ label: "當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。(The party has a legitimate job and sufficient financial capability to provide for themselves and their children's living needs, ensuring a stable and secure life for their offspring.)",
              value: '當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。' }],
          },
          {
            type: '孩童個人意願',
            item: [{ label: '當孩子對於與家庭成員間互動，何者能給予其安全、滿足之心理環境及生活照顧，已有判斷能力。有表達與當事人共同生活之意願。(The child has the ability to make judgments about which family members can provide a safe, satisfying psychological environment and take care of their daily needs. The child has expressed a willingness to live with the party.)',
              value: '當孩子對於與家庭成員間互動，何者能給予其安全、滿足之心理環境及生活照顧，已有判斷能力。有表達與當事人共同生活之意願。' }],
          },
          {
            type: '平日相處關係',
            item: [{ label: '孩子對當事人有一定程度的依賴感及安全感存在。例如孩子會直接對當事人撒嬌求助，並且得到安撫。(The child has a certain degree of dependence and sense of security towards the party, as evidenced by the child seeking comfort and assistance from the party and being soothed by them.)', value: '孩子對當事人有一定程度的依賴感及安全感存在。例如孩子會直接對當事人撒嬌求助，並且得到安撫。' }],
          },
          {
            type: '主要照顧者',
            item: [{ label: '當事人目前為孩子之主要照顧者，並能提供穩定生活及正向發展，並無受不當照顧情形，與當事人互動情形亦良好。(The party is currently the primary caregiver for the child, and is able to provide a stable and positive environment for their development. There is no indication of any improper care, and the interaction between the party and the child is good.)', value: '當事人目前為孩子之主要照顧者，並能提供穩定生活及正向發展，並無受不當照顧情形，與當事人互動情形亦良好。' }],
          },
          {
            type: '居住環境評估',
            item: [{ label: '當事人住處的社區環境足以提供食衣住行育樂的活動安排，而內部居家環境的設備完善，環境寬敞且乾淨整潔，合適孩子居住。(The community environment where the party resides is sufficient to provide for the basic necessities of life, including food, clothing, shelter, and recreational activities. The home itself is well-equipped, spacious, clean, and suitable for the child to live in.)', value: '當事人住處的社區環境足以提供食衣住行育樂的活動安排，而內部居家環境的設備完善，環境寬敞且乾淨整潔，合適孩子居住。' }],
          },
          {
            type: '親友支持系統',
            item: [{ label: "當事人的家人親戚亦住在附近或同住，可以協助支援孩子的照顧。孩子與其互動亦自然和諧。(The party's family members and relatives also live nearby or together, and can provide support and assistance with the care of the child. The interaction between the child and the party's family members and relatives is natural and harmonious.)", value: '當事人的家人親戚亦住在附近或同住，可以協助支援孩子的照顧。孩子與其互動亦自然和諧。' }],
          },
          {
            type: '過往陪伴經驗',
            item: [{ label: '當事人能夠具體陳述對孩子之教育理念及教養態度，且皆會於休假及空閒時，陪伴子女外出遊玩，培養親子互動。(The party is able to articulate their educational philosophy and parenting attitudes regarding the child, and they spend their free time and vacations accompanying their child for outdoor activities, nurturing parent-child interaction.)', value: '當事人能夠具體陳述對孩子之教育理念及教養態度，且皆會於休假及空閒時，陪伴子女外出遊玩，培養親子互動。' }],
          },
          {
            type: '友善父母觀念',
            item: [{ label: '當事人願意讓對方探視孩子，繼續維繫親子關係。(The party is willing to allow the other party to visit the child and maintain a parent-child relationship.)', value: '當事人願意讓對方探視孩子，繼續維繫親子關係。' }],
          },
          {
            type: '其他相關描述',
            item: [{ label: '當事人爭取撫養孩子親權之意願積極，動機是希望陪伴孩子在較好的環境中成長。(The party is actively seeking custody of the child with the motivation of providing a better environment for the child to grow up in.)', value: '當事人爭取撫養孩子親權之意願積極，動機是希望陪伴孩子在較好的環境中成長。' },
              { label: "孩子現仍處於嬰幼階段，亟需母親的關愛照顧，而當事人長期與其共同生活，對其人格特質、身心發展狀況及生活需求甚為瞭解。(The child is still in infancy and early childhood and requires the care and nurturing of a mother, and the party has been living with the child long-term, thus having a deep understanding of the child's personality traits, physical and mental development, as well as their daily needs.)", value: '孩子現仍處於嬰幼階段，亟需母親的關愛照顧，而當事人長期與其共同生活，對其人格特質、身心發展狀況及生活需求甚為瞭解。' }],
          },
        ],
        D: [
          {
            type: '經濟工作情況',
            item: [{ label: '當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。(The party involved currently has no job income or unstable income, and their living expenses rely on assistance from family members. It is uncertain whether they can support the financial needs of raising a child.)', value: '當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。' }],
          },
          {
            type: '孩童個人意願',
            item: [{ label: '孩子年紀已經夠大，已能了解家庭成員互動的關係，意願上比較不希望與當事人同住。(The child is old enough to understand the relationships between family members, and is less willing to live with the party involved.)', value: '孩子年紀已經夠大，已能了解家庭成員互動的關係，意願上比較不希望與當事人同住。' }],
          },
          {
            type: '平日相處關係',
            item: [{ label: "孩童對當事人於雙方婚姻存續期間之諸多作為感到嫌惡，並因當事人離異時造成心靈傷害，而與之關係疏離、緊張。(The child feels disgust towards the party involved for their various actions during the marriage, and experiences emotional damage due to the party's divorce, causing a strained and distant relationship between them.)", value: '孩童對當事人於雙方婚姻存續期間之諸多作為感到嫌惡，並因當事人離異時造成心靈傷害，而與之關係疏離、緊張。' }],
          },
          {
            type: '主要照顧者',
            item: [{ label: "當事人目前並非與孩子同住，或者並非孩子生活的主要照顧者，對其個性、生活所需上了解可能不足。(The party involved currently does not live with the child or is not the primary caregiver of the child, so they may have insufficient understanding of the child's personality and needs.)", value: '當事人目前並非與孩子同住，或者並非孩子生活的主要照顧者，對其個性、生活所需上了解可能不足。' }],
          },
          {
            type: '居住環境評估',
            item: [{ label: "當事人的居住地點附近環境複雜，且屋內並無孩子獨立的生活空間，居家環境不太適合孩子成長。(The environment near the party involved's residence is complicated, and there is no independent living space for the child inside the house, so the home environment is not very suitable for the child's growth.)", value: '當事人的居住地點附近環境複雜，且屋內並無孩子獨立的失活空間，居家環境不太適合孩子成長。' }],
          },
          {
            type: '親友支持系統',
            item: [{ label: "當事人的其他親戚朋友並未同住或少有往來，與孩子的關係陌生，無法提供足夠的支持系統。(The party involved's other relatives and friends do not live together or have little contact, and their relationship with the child is unfamiliar, so they cannot provide sufficient support system.)", value: '當事人的其他親戚朋友並未同住或少有往來，與孩子的關係陌生，無法提供足夠的支持系統。' }],
          },
          {
            type: '過往陪伴經驗',
            item: [{ label: "當事人過往在家庭生活中因為工作或個性，比較少陪伴孩子與之相處，亦不太了解其生活狀況。孩子與之單獨相處會有焦慮。(In the past, the party involved had less time to accompany and interact with the child in their family life due to work or personality, and they also have limited understanding of the child's living conditions. The child feels anxious when alone with them.)", value: '當事人過往在家庭生活中因為工作或個性，比較少陪伴孩子與之相處，亦不太了解其生活狀況。孩子與之單獨相處會有焦慮。' }],
          },
          {
            type: '友善父母觀念',
            item: [{ label: '當事人不願意或阻撓對方探視孩子或任何接觸。(The party involved is unwilling or obstructs the other party from visiting the child or having any contact.)', value: '當事人不願意或阻撓對方探視孩子或任何接觸。' }],
          },
          {
            type: '其他相關描述',
            item: [{ label: "當事人若單獨撫養孩子，因為工作關係，可能沒有時間管教，會繼續放任其偏差之行為，不利於孩子的成長與發展。(If the party involved were to single-handedly raise the child, due to work-related reasons, they may not have enough time to discipline the child and may continue to let them engage in deviant behaviors, which is not conducive to the child's growth and development.)", value: '當事人若單獨撫養孩子，因為工作關係，可能沒有時間管教，會繼續放任其偏差之行為，不利於孩子的成長與發展。' },
              { label: "當事人工作的時間不穩定，長需要夜間輪班工作。孩子現尚幼小，故配合當事人活動尚可，但日後恐會影響到就學及生活作息。(The party involved's work schedule is unstable and often requires night shifts. While the child is still young and can adjust to the party involved's schedule, it may affect the child's education and daily routine in the future.)", value: '當事人工作的時間不穩定，長需要夜間輪班工作。孩子現尚幼小，故配合當事人活動尚可，但日後恐會影響到就學及生活作息。' }],
          },
        ],
      },
      result: {
        data: {
          AA: { Sentence: '', Feature: [] },
          AD: { Sentence: '', Feature: [] },
          RA: { Sentence: '', Feature: [] },
          RD: { Sentence: '', Feature: [] },
        },
      },
      prePredict: false,
    };
  },
  methods: {
    getTestCase() {
      axios({
        method: 'get',
        // url: `${this.$api}/api/predict`,
        url: `${this.$api}/api/get-testcase`,
      }).then((res) => {
        console.log('res.data:', res.data);
        // predict_result: { Applicant: 0, Respondent: 0, Both: 0 }
        this.updateResult({ data: res.data.data });
        this.ground_truth = res.data.result;
        this.ID = res.data.ID;
      });
    },
    checkUrl() {
      // 獲取當前頁面的 URL
      this.showButton = this.$route.query.test === 'true';
    },
    updateResult(val) {
      this.result = val;
      console.log('result:', this.result);
    },
    addStatement(resultKey, statement) {
      this.isStartPredict = false;
      this.isLoading = false;
      this.maxResult = 0;
      if (this.checkStatement(resultKey, statement)) {
        this.result.data[resultKey].Sentence = this.result.data[resultKey].Sentence.replace(statement, '');
      } else {
        this.result.data[resultKey].Sentence += statement;
      }
    },
    checkStatement(resultKey, statement) {
      if (this.result.data[resultKey].Sentence.indexOf(statement) >= 0) return true;
      return false;
    },
    clearAllStatement() {
      console.log(this.$refs.groupForm);
      this.$refs.groupForm.clearAllStatement();
    },
    checkContainChinese(str) {
      return /[\u4E00-\u9FA5]+/g.test(str);
    },
    checkInputValid(data) {
      let isContainAdvantageValid = false;
      let isLenValid = false;
      let isLanguageValid = true;
      if (((data.AA.Sentence.length > 0) || (data.AA.Feature.length > 0)) && ((data.RA.Sentence.length > 0) || (data.RA.Feature.length > 0))) {
        isContainAdvantageValid = true;
      }
      Object.keys(data).forEach((key) => {
        if (data[key].Sentence.length > 0) {
          isLenValid = true;
          if (!this.checkContainChinese(data[key].Sentence)) {
            isLanguageValid = false;
          }
        }
        if (data[key].Feature.length > 0) {
          isLenValid = true;
        }
        return null;
      });
      if (!isContainAdvantageValid) {
        alert('雙方都需要輸入有利的因素選項或是文字敘述喔！');
        return false;
      }
      if (!isLenValid) {
        alert('你還沒選擇任何因素選項或是輸入任何文字敘述喔！');
        return false;
      }
      if (!isLanguageValid) {
        alert('我們目前只支援中文輸入！');
        return false;
      }


      return true;
    },
    findMaxResult(predictResult) {
      if (predictResult.Applicant > this.maxResult) {
        this.maxResult = predictResult.Applicant;
      }
      if (predictResult.Respondent > this.maxResult) {
        this.maxResult = predictResult.Respondent;
      }
      if (predictResult.Both > this.maxResult) {
        this.maxResult = predictResult.Both;
      }
    },
    mergeResult(inputData) {
      const outputData = {};
      Object.entries(inputData).forEach(([key, value]) => {
        const featuresSet = new Set();
        const sentences = [];
        console.log('key:', key, 'value:', value);

        value.forEach((item) => {
          if (item.Feature && item.Feature.length > 0) {
            item.Feature.forEach(feature => featuresSet.add(feature));
          }
          if (item.Sentence && item.Sentence.trim().length > 0) {
            sentences.push(item.Sentence.trim());
          }
        });

        outputData[key] = {
          Feature: Array.from(featuresSet),
          Sentence: sentences.join(' '),
        };
      });

      return outputData;
    },
    updatePrePredict(val) {
      this.prePredict = val;
    },
    startPredict() {
      // if (!this.prePredict) {
      //   this.$message({
      //     message: '請檢查是否皆已輸入因素與理由',
      //     type: 'warning',
      //   });
      //   return;
      // }
      console.log('>>>>>start predict ==> raw result:', this.result.data);
      let result = this.mergeResult(this.result.data);
      console.log('>>>>>start predict ==> merge result:', result);
      if (this.checkInputValid(result)) {
        this.isLoading = true;
        result = {
          model: this.$route.params.mode,
          data: result,
        };
        console.log('>>>>>start predict ==> provide result:', result);
        axios({
          method: 'post',
          // url: `${this.$api}/api/predict`,
          url: `${this.$api}/api/intermediate-predict`,
          data: result,
        }).then((res) => {
          console.log('res.data:', res.data);
          // predict_result: { Applicant: 0, Respondent: 0, Both: 0 }
          this.predict_result = res.data;
          this.findMaxResult(this.predict_result);
          this.isStartPredict = true;
          this.isLoading = false;
        });
      } else {
        this.isStartPredict = false;
        this.isLoading = false;
        this.maxResult = 0;
      }
      // eslint-disable-next-line no-alert
    },
  },
  created() {
    this.checkUrl();
  },
  watch: {
    result: {
      handler(val) {
        // do stuff
        this.isStartPredict = false;
        this.isLoading = false;
        this.maxResult = 0;
      },
      deep: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.page-title {
    font-size: 1.5rem;
    font-weight: bold;
    width: fit-content;
    margin: 0px 0 10px 0;
    padding: 0 5px;
}
.predict-container {
    background-color: #fff;
    border: 2px solid #F3BB5C;
    border-radius: 8px;
    margin: 10px;
    padding: 0; /* 小屏幕上没有padding */
}

/* 媒体查询（大屏幕） */
@media (min-width: 768px) { /* 768px 通常用于区分小屏幕和中等以上屏幕 */
    .predict-container {
        padding: 35px 40px; /* 大屏幕上增加padding */
        margin: 50px;
    }
}
.ins-1 {
    font-size: 1.2rem;
    font-weight: bold;
    padding-top: 15px;
}
.quote {
    background-color: rgba(90,77,88,0.12);
    text-align: center;
    font-size: 1rem;
    text-align: left;
    margin: 0;
}
.predict-btn {
    border-radius: 4px;
    color: #fff;
    font-size: 1.2rem;
    font-weight: bold;
    width: fit-content;
    text-align: center;
    padding: 10px 20px;
    cursor: pointer;
    transition: 0.4s;
    &:hover {
        opacity: 0.8;
    }
}
.statement-card {
  word-break: break-word;
  padding: 5px;
  margin-bottom: 5px;
  border: 1px solid #5A4D30;
  border-radius: 2px;
  cursor: pointer;
  transition: 0.4s;
  &:hover {
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  }
}
.isActive {
  background: #5A4D30;
  color: #fff;
}
.ins-3 {
  font-weight: bold
}
.predictResult {
  width: 100%;
}
.shuffle-icon {
  width: 1rem;
}
.random-btn {
 cursor: pointer;
 box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
 padding: 0.5rem;
 border-radius: 5px;
 background: rgba(223, 223, 223, 0.555);
 &:hover {
    background: rgb(194, 194, 194);
    color: white;
  }
}
</style>
