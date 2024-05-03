<!-- eslint-disable max-len -->
<template>
  <div class="page-container">
    <div class="predict-container">
      <div class="page-title">{{ pageText[$route.params.mode].title }}</div>
      <div class="shadow-none p-2 mb-2 rounded quote">{{ pageText[$route.params.mode].instruction }}</div>
      <div v-loading="isLoading">
        <router-view @resultUpdate="updateResult" ref="groupForm"/>
      </div>
      <div class="shadow-none p-2 mb-2">{{ pageText[$route.params.mode].note }}</div>
      <el-row :gutter="20">
        <div class="btn-block display-control-big">
          <el-col :span="12">
          <div class="predict-btn" style="background-color:#5A4D30; float:right;" @click="clearAllStatement()">全部清除</div>
        </el-col>
        <el-col :span="12" class="d-inline-flex align-items-center">
          <div class="predict-btn"  style="background-color:#F3BB5C" @click="startPredict()">申請預測</div>
          <div class="ml-2">
            <el-tooltip placement="right" effect="light" class="tooltip-base-box">
              <template #content>
                <div v-if="(isLoading || isTalking) && interpreterContent.length === 0">
                  正在生成結果解讀中....<b-spinner class="spinner ml-1" variant="secondary" label="Spinning"></b-spinner>
                </div>

                <div v-if="interpreterContent.length > 0">
                  <le-preview ref="md-preview" :is-md="true" :value="interpreterContent" :hljs-css="hljsCss"></le-preview>
                </div>
              </template>
              <el-button>
                <img class="icon-func mx-2" src="../../../static/info.png">
                結果解讀
                <b-spinner v-if="isLoading || isTalking" class="spinner ml-1" variant="secondary" label="Spinning"></b-spinner>
              </el-button>
            </el-tooltip>
          </div>
        </el-col>
        </div>

        <div class="btn-block display-control-small">
          <el-col :span="24" class="d-inline-flex align-items-center justify-content-center">
          <div class="predict-btn mx-1" style="background-color:#5A4D30; float:right;" @click="clearAllStatement()">全部清除</div>
          <div class="predict-btn mx-1"  style="background-color:#F3BB5C" @click="startPredict()">申請預測</div>
        </el-col>
        <el-col :span="24" class="my-2 d-inline-flex align-items-center justify-content-center">
          <el-tooltip placement="right" effect="light" class="tooltip-base-box">
              <template #content>
                <div v-if="(isLoading || isTalking) && interpreterContent.length === 0">
                  正在生成結果解讀中....<b-spinner class="spinner ml-1" variant="secondary" label="Spinning"></b-spinner>
                </div>

                <div v-if="interpreterContent.length > 0">
                  <le-preview ref="md-preview" :is-md="true" :value="interpreterContent" :hljs-css="hljsCss"></le-preview>
                </div>
              </template>
              <el-button>
                <img class="icon-func mx-2" src="../../../static/info.png">
                結果解讀
                <b-spinner v-if="isLoading || isTalking" class="spinner ml-1" variant="secondary" label="Spinning"></b-spinner>
              </el-button>
            </el-tooltip>
        </el-col>
        </div>


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
            v-if="isModeKeyLengthTwo"
            class="predictResult"
            :predict_result="predict_result[$route.params.mode]"
            :elapsedTime="elapsedTime"
            :isLoading="isLoading"
            :errorPrompt="errorPrompt"
            :errorCode="errorCode"
          />
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PredictResult from '../Sub/predictResult';
import OpenCC from 'opencc-js';

export default {
  name: 'UserPredict',
  components: {
    PredictResult,
  },
  data() {
    return {
      hljsCss: 'agate',
      isInterpretering: false,
      modelUsed: {
        mode1: ['L1', 'L2'],
        mode2: ['S1', 'S2'],
        mode3: ['C1', 'C2'],
      },
      interpreterContent: '',
      isTalking: false,
      result: {
        mode1: {
          data: {
            AA: [{ Sentence: '', Feature: [] }],
            AD: [{ Sentence: '', Feature: [] }],
            RA: [{ Sentence: '', Feature: [] }],
            RD: [{ Sentence: '', Feature: [] }],
          },
        },
        mode2: {
          data: {
            AA: [{ Sentence: '', Feature: [] }],
            AD: [{ Sentence: '', Feature: [] }],
            RA: [{ Sentence: '', Feature: [] }],
            RD: [{ Sentence: '', Feature: [] }],
          },
        },
        mode3: {
          data: {
            AA: [{ Sentence: '', Feature: [] }],
            AD: [{ Sentence: '', Feature: [] }],
            RA: [{ Sentence: '', Feature: [] }],
            RD: [{ Sentence: '', Feature: [] }],
          },
        },
      },
      showButton: false,
      ID: '',
      ground_truth: '',
      predict_result: { mode1: { Applicant: 0, Respondent: 0, Both: 0 }, mode2: { Applicant: 0, Respondent: 0, Both: 0 }, mode3: { Applicant: 0, Respondent: 0, Both: 0 } },
      elapsedTime: 0,
      isLoading: false,
      // isStartPredict: false,
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
        { label: '親子感情', value: '親子感情', desc: '親子彼此互動的模式是否親密，子女是否有信賴/依附關係或害怕相處' },
        { label: '意願能力', value: '意願能力', desc: '是否有積極(或消極)撫養的意願，相關撫養規劃與適合的親職能力' },
        { label: '父母經濟', value: '父母經濟', desc: '收入是否穩定且足以負擔子女養育所需，是否過度負債影響生計' },
        { label: '支持系統', value: '支持系統', desc: '其他親友是否能協助子女的生活照顧或父母的經濟支持' },
        { label: '父母生活', value: '父母生活', desc: '居家環境、是否有足夠空間或生活作習是否合適撫養子女' },
        { label: '主要照顧', value: '主要照顧', desc: '過往長期照顧且了解子女的生活情形，包括當前照顧的狀態是否應繼續' },
        { label: '子女年齡', value: '子女年齡', desc: '未成年子女的年紀是否幼小需要特別照顧，還是足以清楚表達意願。' },
        { label: '人格發展', value: '人格發展', desc: '對子女未來成長的影響(如能否穩定就學或有價值觀偏差)' },
        { label: '父母健康', value: '父母健康', desc: '心理或身體是否有不良狀況而不適任為子女照顧者' },
        { label: '父母職業', value: '父母職業', desc: '工作性質對子女照顧的影響(如常有夜班或出差的情形)' },
        { label: '子女意願', value: '子女意願', desc: '希望與雙親中哪一位共同生活，包括意願或態度' },
        { label: '友善父母', value: '友善父母', desc: '是否在子女面前誹謗對方，或阻擾對方與子女維持親子關係(含會面交往)' },
        { label: '父母品行', value: '父母品行', desc: '是否有不良嗜好、家庭暴力、精神虐待、吸毒或入監的紀錄' },
      ],
      featuresGroup: { 有利: {
        親子感情: '親子彼此互動的模式親密，子女對當事人有信賴/依附關係。',
        意願能力: '當事人有積極撫養的意願，並且有相關撫養規劃與適合的親職能力。',
        父母經濟: '當事人收入穩定且足以負擔子女養育所需。',
        支持系統: '當事人有其他親友能協助子女的生活照顧或父母的經濟支持。',
        父母生活: '當事人的居家環境有足夠空間以及其生活作習適合撫養子女。',
        主要照顧: '當事人在過往，長期照顧子女且了解子女的生活情形，當前照顧的狀態應繼續。',
        子女年齡: '當事人的未成年子女的年紀幼小還不足以清楚表達意願，需要特別照顧。',
        人格發展: '當事人對子女未來成長有良好的影響。',
        父母健康: '當事人的心理或身體沒有不良狀況，身心適任為子女照顧者。',
        父母職業: '當事人的工作性質對子女照顧沒有不良的影響(如沒有夜班或出差的情形)。',
        子女意願: '當事人的子女可清楚表達包括意願或態度，並表示希望與當事人共同生活。',
        友善父母: '當事人並未在子女面前誹謗對方，也沒有阻擾對方與子女維持親子關係(含會面交往)。',
        父母品行: '當事人沒有不良嗜好、家庭暴力、精神虐待、吸毒或入監的紀錄。',
      },
      不利: {
        親子感情: '親子彼此互動的模式並不親密，子女害怕與當事人相處。',
        意願能力: '當事人對撫養的意願充滿消極的態度，也沒有相關撫養規劃與適合的親職能力。',
        父母經濟: '當事人收入不穩定且不足以負擔子女養育所需，且其過度負債影響生計。',
        支持系統: '當事人沒有其他親友能協助子女的生活照顧或父母的經濟支持。',
        父母生活: '當事人的居家環境、沒有足夠空間或生活作習並不適合撫養子女。',
        主要照顧: '當事人並不了解子女的生活情形，當前照顧的狀態不應繼續。',
        子女年齡: '當事人的未成年子女的年紀並沒有幼小需要特別照顧，其足以清楚表達意願。',
        人格發展: '當事人對子女未來成長造成負面影響(如未能穩定就學或有價值觀偏差)。',
        父母健康: '當事人的心理或身體有不良狀況而不適任為子女照顧者。',
        父母職業: '當事人的工作性質對子女照顧有不良的影響(如常有夜班或出差的情形)。',
        子女意願: '孩子表示不希望與當事人共同生活。。',
        友善父母: '當事人曾在子女面前誹謗對方，或阻擾對方與子女維持親子關係(含會面交往)。',
        父母品行: '當事人有不良嗜好、家庭暴力、精神虐待、吸毒或入監的紀錄。',
      },
      },
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
    };
  },
  computed: {
    isModeKeyLengthTwo() {
      // 确保 predict_result 和 $route.params.mode 是存在的
      const mode = this.$route.params.mode;
      const result = this.predict_result[mode];
      if (result) {
        return Object.keys(result).length === 2;
      }
      return false; // 如果 result 不存在，返回 false
    },
  },
  methods: {
    getTestCase() {
      axios({
        method: 'get',
        // url: `${this.$api}/api/predict`,
        url: `${this.$api}/api/get-testcase`,
      }).then((res) => {
        console.log('res.data:', res.data);
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
    clearInputForm() {
      if (this.$refs.groupForm.$refs.inputForm) {
        for (let i = 0; i < this.$refs.groupForm.$refs.inputForm.length; i += 1) {
          this.$refs.groupForm.$refs.inputForm[i].clearAll();
        }
      }
    },
    clearSelectForm() {
      if (this.$refs.groupForm.$refs.selectForm) {
        console.log('>>Clear');
        for (let i = 0; i < this.$refs.groupForm.$refs.selectForm.length; i += 1) {
          this.$refs.groupForm.$refs.selectForm[i].clearAll();
        }
      }
    },
    clearAllStatement() {
      console.log('clearAllStatement', this.$refs.groupForm.$refs);
      this.result[this.$route.params.mode].data = {
        AA: [{ Sentence: '', Feature: [] }],
        AD: [{ Sentence: '', Feature: [] }],
        RA: [{ Sentence: '', Feature: [] }],
        RD: [{ Sentence: '', Feature: [] }],
      };
      if (this.$route.params.mode === 'mode1') {
        this.clearSelectForm();
      } else if (this.$route.params.mode === 'mode2') {
        this.clearInputForm();
      } else if (this.$route.params.mode === 'mode3') {
        this.clearSelectForm();
        this.clearInputForm();
      }
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
    prepareMode1InterpreterInput(result) {
      const returnResult = { AA: '', AD: '', RA: '', RD: '' };

      // Assuming 'result' is a previously defined object
      Object.keys(result).forEach((key) => {
        result[key].Feature.forEach((item) => {
          if (!key.includes('D')) {
            // Favorable case
            returnResult[key] += this.featuresGroup['有利'][item];
          } else {
            // Unfavorable case
            returnResult[key] += this.featuresGroup['不利'][item];
          }
        });
      });

      return returnResult;
    },
    prepareMode2InterpreterInput(result) {
      const returnResult = { AA: result.AA.Sentence, AD: result.AD.Sentence, RA: result.RA.Sentence, RD: result.RD.Sentence };
      return returnResult;
    },
    prepareMode3InterpreterInput(result) {
      const returnResult = { AA: result.AA.Sentence, AD: result.AD.Sentence, RA: result.RA.Sentence, RD: result.RD.Sentence };

      // Assuming 'result' is a previously defined object
      Object.keys(result).forEach((key) => {
        result[key].Feature.forEach((item) => {
          if (!key.includes('D')) {
            // Favorable case
            returnResult[key] += this.featuresGroup['有利'][item];
          } else {
            // Unfavorable case
            returnResult[key] += this.featuresGroup['不利'][item];
          }
        });
      });

      return returnResult;
    },
    interpretData(mode) {
      this.isTalking = true;
      this.interpreterContent = '';
      const result = this.mergeResult(this.result[mode].data);
      console.log('>>>debug:', result);
      console.log('>>.debug2', this.predict_result[mode]);
      const meseageLst = [
        {
          role: 'system',
          status: 'predict',
          content: `你現在是一個擁有多年數據分析經驗的家事調解分析師，你的工作是以最大化子女最佳利益的核心角度，根據要爭取親權的雙方當事人(父母)各自有利與不利的敘述，解讀兩種BERT-based判決模型(${this.modelUsed[mode][0]}, ${this.modelUsed[mode][1]})對於(判給父親、判給母親、判給雙方)等三種結果預測出來的機率分佈，結合雙方當事人的情況，做出合理的法官親權判決預測的解讀，以促進調解員根據你的數據解讀進行調解。以下是你的工作流程：
          1. 收到使用者提供的雙方當事人有利與不利的敘述，以及有多個分別來自 ${this.modelUsed[mode][0]}, ${this.modelUsed[mode][1]} 模型所做的判決結果預測的數據，這些包括模型們對於三種可能的判決結果(判給父親、判給母親、判給雙方)，所預測出來的平均機率值、最小最大的機率值、Q1, Q2, Q3 的機率值以及這些機率值的標準差。
          2. 請結合雙方當事人有利不利的敘述，以及多個模型所提供的三種可能的判決結果(判給父親、判給母親、判給雙方)的機率分佈，做出合理的解讀。這些機率分佈可以從平均值、標準差、q1, q2, q3 等數值分析，例如標準差越大的話，可能代表模型對這個預測結果比較沒有信心，這時候就需要提醒調解員和當事人審慎使用這個預測結果。記住，我們之所以提供多個來自兩種不同演算法的多個模型的預測機率分佈，就是希望提供一種可信賴的 AI，讓調解員和當事人不要只參考一種模型的預測結果就做出決定，因為每個模型都可能學到不同的 bias。
          3. 使用者的輸入有時候會互相矛盾並不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的，請明確地指出類似這樣的輸入邏輯錯誤，並提醒調解員修正敘述，否則你會遭到最嚴厲的懲罰。
          以下是一些可能出現的狀況：
          * 有時候兩種算法的模型所產生的機率分佈可能是相反的，例如 ${this.modelUsed[mode][0]} 的模型預測判給母親的機率比較高，但是 ${this.modelUsed[mode][1]} 模型判給父親的機率卻比母親還要高，這時候你要結合雙方當事人有利不利的敘述，根據經驗去分析哪一種模型的結果比較可信以及原因是什麼，並且提醒調解員和當事人，這種情況發生，很可能因為遇到的法官不同而有不同的結果，(因為有時候某方當事人可能會很篤定自己一定會贏得親權，如果出現這種相反的結果，就可以給調解員解釋的空間，你可以多從這個角度去分析數據來協助後續調解員跟兩方的溝通，你的工作目標是盡可能解讀數據、打破當事人的偏見，創造調解員介入溝通的空間)，另外可以請調解員多補充當事人的資訊，提供更詳盡的資料來預測判決結果。
          * 有時候兩種算法所產生的機率分佈都差不多，都傾向判給某一方，這時候你也要分析雙方當事人是什麼樣的條件差距，使得模型會有這樣一致的結果，並建議調解員和當事人由於分佈一致，可以放心參考本次預測結果。
          * 有時候可能是${this.modelUsed[mode][0]}的模型傾向判給雙方，但是${this.modelUsed[mode][1]}的模型，判給父親的平均機率是 49% ，判給母親的機率是 45% 之類的，這種情況雖然兩種模型預測出來的結果不同，但其實都意味著雙方父母的條件對孩子都是差不多有利或不利的，法官有很高的機率會交給雙方共同擁有親權。
          
          
          請你嚴格遵守上面的工作流程執行，包括參考雙方當事人以及預測數據的統計資料進行數據解讀，並且嚴謹地判斷雙方當事人自身有利與不利敘述的邏輯合理性、是否會互相矛盾，在錯誤時馬上指出，否則你會遭到罰款！
          `,
        },
        {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：孩子對當事人有一定程度的依賴感及安全感存在。例如孩子會直接對當事人撒嬌求助，並且得到安撫。
          對母親不利的敘述：
          對父親有利的敘述：當事人有穩定及較高的經濟狀況，可以為孩子提供更充足的教育和生活資源。父親表現出對孩子的關懷，定期通過通話了解孩子的日常生活和學習情況，顯示其對與孩子保持聯繫的高度意願。 
          對父親不利的敘述：當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。
          在開始分析預測結果前，請先判斷使用者的輸入是否出現矛盾不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的。一旦你懷疑使用者的輸入出現矛盾，請馬上明確地指出，並提醒調解員有這個狀況，請他適當地修正雙方的敘述。
          接下來，以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. ${this.modelUsed[mode][0]}模型：
            *判給父親: [平均機率：12.438500921548421, 最小機率：0, 最大機率：99.83, Q1:0.07, Q2:0.56, Q3:4.59, 標準差:27.92]
            *判給母親: [平均機率：45.331100512521516, 最小機率：0.01, 最大機率：100, Q1:1.06, Q2:19.87, Q3:98.12, 標準差:45.28]
            *判給雙方: [平均機率：42.230399545115084, 最小機率：0, 最大機率：99.98, Q1:1.41, Q2:19.75, Q3:92.97, 標準差:43.31]
          2. ${this.modelUsed[mode][1]}模型：
            *判給父親: [平均機率：18.312848778841726, 最小機率：0, 最大機率：90.1, Q1:1.39, Q2:11.02, Q3:24.63, 標準差:22.33]
            *判給母親: [平均機率：51.317591493110136, 最小機率：0.02, 最大機率：99.48, Q1:17.15, Q2:54.37, Q3:85.47, 標準差:34.89]
            *判給雙方: [平均機率：30.369559255583834, 最小機率：0.35, 最大機率：99.12, Q1:5.81, Q2:24.61, Q3:43.36, 標準差:28.41]
            請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員促進雙方當事人的溝通。如果你懷疑當事人的敘述之間出現矛盾之處，請在最後再次指出，並提醒調解員做出修正。
          `,
        },
        {
          role: 'assistant',
          status: 'predict',
          content: '在您的輸入中，父親有利的部分提到他有穩定的經濟狀況，但是在父親不利的敘述中又提到他目前未有工作收入或收入不穩定，顯然在同一個當事人（父親）身上出現兩種互相矛盾的敘述。請您修正關於父親的敘述，或是補充更多資訊後再次進行判決結果預測。針對本次的預測結果，請審慎參考。',
        },
        {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。母親阿霞歷來是孩子的主要照顧者，孩子與母親建立了深厚的感情依附關係，並且對孩子的日常起居提供了充分的照顧。母親已規劃具體且階段性的未來教養計畫，突顯其對孩子教育和情感發展的長期承諾。 對母親不利的敘述：當事人目前無穩定工作和收入來源，經濟狀況可能影響其提供孩子更廣泛的教育和生活資源的能力。母親缺乏較高的教育背景，且在台灣沒有其他親友可以協助照顧孩子，這可能對其提供孩子全面支持造成困難。 對父親有利的敘述：當事人有穩定及較高的經濟狀況，可以為孩子提供更充足的教育和生活資源。父親表現出對孩子的關懷，定期通過通話了解孩子的日常生活和學習情況，顯示其對與孩子保持聯繫的高度意願。 對父親不利的敘述：當事人過去曾有將孩子獨留家中的情形，沒有充分注意孩子的日常需要，這可能對孩子的安全形成風險。儘管有積極的態度，但目前對於如何具體教養孩子仍缺乏明確的規劃和準備，這可能影響他作為主要照顧者的能力。
          在開始分析預測結果前，請先判斷使用者的輸入是否出現矛盾不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的。一旦你懷疑使用者的輸入出現矛盾，請馬上明確地指出，並提醒調解員有這個狀況，請他適當地修正雙方的敘述。
          接下來，以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. ${this.modelUsed[mode][0]}模型：
            *判給父親: [平均機率：12.438500921548421, 最小機率：0, 最大機率：99.83, Q1:0.07, Q2:0.56, Q3:4.59, 標準差:27.92]
            *判給母親: [平均機率：45.331100512521516, 最小機率：0.01, 最大機率：100, Q1:1.06, Q2:19.87, Q3:98.12, 標準差:45.28]
            *判給雙方: [平均機率：42.230399545115084, 最小機率：0, 最大機率：99.98, Q1:1.41, Q2:19.75, Q3:92.97, 標準差:43.31]
          2. ${this.modelUsed[mode][1]}模型：
            *判給父親: [平均機率：18.312848778841726, 最小機率：0, 最大機率：90.1, Q1:1.39, Q2:11.02, Q3:24.63, 標準差:22.33]
            *判給母親: [平均機率：51.317591493110136, 最小機率：0.02, 最大機率：99.48, Q1:17.15, Q2:54.37, Q3:85.47, 標準差:34.89]
            *判給雙方: [平均機率：30.369559255583834, 最小機率：0.35, 最大機率：99.12, Q1:5.81, Q2:24.61, Q3:43.36, 標準差:28.41]
            請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員促進雙方當事人的溝通。如果你懷疑當事人的敘述之間出現矛盾之處，請在最後再次指出，並提醒調解員做出修正。
          `,
        },
        {
          role: 'assistant',
          status: 'predict',
          content: `鑑於兩個模型的數據，結合當事人情況，以下是我的建議：
          1. 母親方案的可能性高：兩個模型都顯示判給母親的機率相對較高，這與她作為主要照顧者的事實相符。但調解員應注意她的經濟和教育狀況，可能需要提供額外支持或資源。
          2. 考慮共同親權的可能性：如果法官認為父親能改善對孩子的照顧方式，共同親權也可能是一個適合的選擇，特別是因為兩個模型在許多情況下都給予了不低的機率。
          3. 積極溝通和信息補充：鑑於標準差較大，表明模型預測存在不確定性，建議調解員在實際操作中積極收集更多具體信息，以做出最符合孩子最佳利益的決策。`,
        },
        {
          role: 'user',
          status: 'predict',
          content: '',
        },
      ];
      if (mode === 'mode1') {
        const inputSentence = this.prepareMode1InterpreterInput(result);
        meseageLst[meseageLst.length - 1] = {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：${inputSentence.RA} 
          對母親不利的敘述：${inputSentence.RD} 
          對父親有利的敘述：${inputSentence.AA}  
          對父親不利的敘述：${inputSentence.AD} 
          在開始分析預測結果前，請先判斷使用者的輸入是否出現矛盾不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的。一旦你懷疑使用者的輸入出現矛盾，請馬上明確地指出，並提醒調解員有這個狀況，請他適當地修正雙方的敘述。
          接下來，以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. ${this.modelUsed[mode][0]} 模型：
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Both.std}]
          2. ${this.modelUsed[mode][1]} 模型：
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Both.std}]
          
          請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員促進雙方當事人的溝通。如果你懷疑當事人的敘述之間出現矛盾之處，請在最後再次指出，並提醒調解員做出修正。
          `,
        };
      } else if (mode === 'mode2') {
        const inputSentence = this.prepareMode2InterpreterInput(result);
        meseageLst[meseageLst.length - 1] = {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：${inputSentence.RA} 
          對母親不利的敘述：${inputSentence.RD} 
          對父親有利的敘述：${inputSentence.AA}  
          對父親不利的敘述：${inputSentence.AD} 
          以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. S1模型：
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Both.std}]
          2. S2
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Both.std}]
          
          使用者的輸入有時候會互相矛盾並不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的，請明確地指出類似這樣的輸入邏輯錯誤，並提醒調解員修正敘述，否則你會遭到最嚴厲的懲罰。
          請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員調解當事人。
          `,
        };
      } else {
        const inputSentence = this.prepareMode3InterpreterInput(result);
        meseageLst[meseageLst.length - 1] = {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：${inputSentence.RA} 
          對母親不利的敘述：${inputSentence.RD} 
          對父親有利的敘述：${inputSentence.AA}  
          對父親不利的敘述：${inputSentence.AD} 
          以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. S1模型：
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][0]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][0]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][0]].Both.std}]
          2. S2
            *判給父親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Applicant.std}]
            *判給母親: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.avg_prob}, 最小機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.min}, 最大機率：${this.predict_result[mode][this.modelUsed[mode][1]].Both.max}, Q1:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q1}, Q2:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q2}, Q3:${this.predict_result[mode][this.modelUsed[mode][1]].Both.q3}, 標準差:${this.predict_result[mode][this.modelUsed[mode][1]].Both.std}]
          
          使用者的輸入有時候會互相矛盾並不合理，可能包含父親母親他們有利與不利的陳述會彼此矛盾，例如母親有利的地方提到「孩子與當事人親近信任」，但是在母親不利的地方又提到「孩子非常害怕與當事人相處」這就是明顯矛盾的地方；又或是父親有利的部分寫「當事人有正當工作，經濟能力尚足以支付本身及孩子生活所需，可提供孩子穩定及安全的生活。」，但是不利的地方又寫：「當事人目前未有工作收入或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。」明顯是互相矛盾的，請明確地指出類似這樣的輸入邏輯錯誤，並提醒調解員修正敘述，否則你會遭到最嚴厲的懲罰。
          請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員調解當事人。
          `,
        };
      }

      console.log('>>>msg list:', meseageLst);

      this.chat(meseageLst).then((response) => {
        if (response) {
          const reader = response.body.getReader();
          const status = response.status;
          this.readStream(reader, status);
        }
      });
    },
    convertToTraditional(simplifiedText) {
      const converter = OpenCC.Converter({ from: 'cn', to: 'tw' });
      const traditionalText = converter(simplifiedText);
      return traditionalText;
    },
    async readStream(reader, status) {
      console.log('>>>Enter readerStream()');
      const partialLine = '';
      const decoder = new TextDecoder('utf-8'); // 假设你在函数中使用了解码器

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const decodedText = this.convertToTraditional(decoder.decode(value, { stream: true }));

        if (status !== 200) {
          this.interpreterContent += decodedText;
          return;
        }

        const chunk = partialLine + decodedText;
        this.interpreterContent += chunk;
      }

      this.isTalking = false;
    },
    async chat(messageList) {
      console.log('>>>enter chat...');
      try {
        const response = await fetch(`${this.$api}/api/send-messages`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ model: 'gpt-4-turbo', messages: messageList, stage: 'do-predict' }),
        });
        console.log('>>>Start to fetch');
        return response;
      } catch (error) {
        console.error('Error:', error);
        this.isTalking = false;
      }
    },
    startPredict() {
      console.log('>>>>>start predict ==> raw result:', this.result[this.$route.params.mode].data);
      let result = this.mergeResult(this.result[this.$route.params.mode].data);
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
          url: `${this.$api}/api/intermediate-predict`,
          // url: `/api/intermediate-predict`,
          data: result,
        }).then((res) => {
          console.log('res.data:', res.data);
          this.predict_result[this.$route.params.mode] = res.data;
          // this.isStartPredict = true;
          this.isLoading = false;
          this.interpretData(this.$route.params.mode);
        }).catch((error) => {
          console.log('>>Error:', error);
          alert(`Oops! 看來出現了一些問題，請稍候再嘗試或是通知管理員！\n 錯誤如下：${error}`);
          this.isLoading = false;
        });
      } else {
        // this.isStartPredict = false;
        this.isLoading = false;
      }
      // eslint-disable-next-line no-alert
    },
  },
  created() {
    this.checkUrl();
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      if (to.params.mode) {
        vm.interpreterContent = ''; // 清空变量
      }
    });
  },
  beforeRouteUpdate(to, from, next) {
    if (to.params.mode !== from.params.mode) {
      this.interpreterContent = ''; // 清空变量
    }
    next();
  },
  watch: {
    result: {
      handler(val) {
        // do stuff
        // this.isStartPredict = false;
        this.isLoading = false;
        this.predict_result[this.$route.params.mode] = { Applicant: 0, Respondent: 0, Both: 0 };
        this.interpreterContent = '';
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

.interpretor-btn {
  background: #EBE9EB;
  border: 1px solid rgba(173, 173, 173, 0.76);
  color: #333;
  &:hover {
    opacity: 0.7;
  }
}

.icon-func {
  width: 1.2rem;
}
.spinner {
  width: 1rem;
  height: 1rem;
}

@media (max-width: 768px) {
  .predict-interpreter-block {
    display: flex;
    flex-direction: column;  /* 小屏幕上垂直排列 */
  }
}

@media (min-width: 769px) {
  .predict-interpreter-block {
    display: flex;
    flex-direction: row;  /* 大屏幕上水平排列 */
  }
}

.display-control-big {
  display: none;
}
.display-control-small {
  display: block;
}

@media (min-width: 768px) {
  .display-control-big {
    display: block;
  }
  .display-control-small {
  display: none;
}
}


</style>

<style lang="scss">

  #le-markdown-body .markdown-body {
    color: #333;
    font-size: 0.9rem !important;
  }

  .el-tooltip__popper.is-light {
    font-size: 0.9rem;
    max-width: 50%;
    padding: 1.5rem;
    color: #333;
    line-height: 1.5;
    background: #EBE9EB !important;
    max-height: 80vh;
    overflow-y: scroll;
    background: #EBE9EB !important;
    border: 1px solid #9a9a9a !important;
  }

</style>

