<template>
  <div class="pb-2">
    <el-row :gutter="2">
      <el-col :span="6">
        <div v-if="warnState.feature" class="warn-text">*因素不得為空</div>
        <el-tooltip class="item" effect="dark" :content="getFeatureDesc(result.feature)" placement="top-start">
          <div class="feature-name">{{ result.feature }}
            <!-- <i class="el-icon-question"></i> -->
          </div>
        </el-tooltip>
        <el-dialog title="新增因素與理由" :visible.sync="dialogState" width="85%">
          <el-row :gutter="20">
            <el-col :lg="8" :sm="12" :xs="24" v-for="feature in features" :key="feature.value">
              <div class='statement-card' @click="addInput({feature: feature.value, sentence: sentencesExample[configKey.type][feature.value]?sentencesExample[configKey.type][feature.value]:'' })">
                <el-tooltip class="item" effect="dark" :content="feature.desc" placement="top-start">
                  <div class="feature-name orange-text">{{ feature.value }}
                    <i class="el-icon-question"></i>
                  </div>
                </el-tooltip>
                <div class="tiny-title">理由範例文字</div>
                <div class="example-text">{{ sentencesExample[configKey.type][feature.value]?sentencesExample[configKey.type][feature.value]:'' }}</div>
              </div>
            </el-col>
          </el-row>
        </el-dialog>
        <el-button type="primary" icon="el-icon-edit" size="mini" @click="dialogState=true">選擇因素與<br>理由範例</el-button>
      </el-col>
      <el-col :span="18">
        <div v-if="warnState.sentence" class="warn-text">*理由不得為空</div>
        <textarea class="form-control border-secondary" rows="3" v-model="result.sentence"></textarea>
      </el-col>
    </el-row>
</div>
</template>

<script>
export default {
  name: 'InputDescription',
  data() {
    return {
      result: {
        feature: this.initialFeature,
        sentence: this.initialSentence,
      },
      dialogState: false,
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
      sentencesExample: {
        A: {
          親子感情: '孩子習慣由當事人照顧生活及一起行動，表現出對其依賴與信任，互動緊密。',
          意願能力: '當事人爭取孩子監護權之態度十分積極且堅定，且有足夠的親職能力提供教育及生活規劃。',
          父母經濟: '當事人具有正當的工作且有穩定之經濟基礎，生活開銷支應無虞。',
          支持系統: '當事人的家人皆為友善之親屬，可以在有需要的時候協助照顧孩子的生活起居。',
          父母生活: '當事人住家空間足夠安排孩子自己的房間，而住家距離學區及鬧區約5分鐘車程可及，生活機能便利，應適宜孩子居住。',
          主要照顧: '孩子自幼即與當事人同住，由當事人擔任其主要生活照顧者，目前生活平順，應減少不必要的變動。',
          子女年齡: '孩子尚屬年幼，應極需有細心關照之需要，較適合由當事人長期照顧。',
          人格發展: '孩子年齡已漸入青春期階段，開始發展形塑自己之人格與想法，在人格發展上亟需家人關心與引導，由當事人擔任親權人更為適切。',
          父母健康: '當事人健康狀況良好正常，無重大傷病，可親自負擔孩子之生活照顧。',
          父母職業: '當事人有穩定工作與收入來源，亦可於工作時間外照顧未成年子女。',
          子女意願: '孩子年齡已達青少年階段，可清楚表達自己的意思，希望能與當事人同住。',
          友善父母: '當事人願意讓對方繼續探望孩子，維繫親子關係，對孩子的成長較為有利。',
          父母品行: '當事人的品性與素行並無不當紀錄。',
        },
        D: {
          親子感情: '孩子對當事人平日的言行感到不舒服，單獨與之相處有疏離或緊張的關係。',
          意願能力: '當事人雖表示有爭取監護權的意願，但是尚未有完整的撫養規劃，教養方面的能力尚嫌不足。',
          父母經濟: '當事人目前尚未有工作或收入不穩定，生活支出仰賴家人協助，不確定能否支持養育孩子的經濟需求。',
          支持系統: '孩子與當事人的同居者原生家庭關係不佳，若獨自養育恐無法有足夠的支持系統協助。',
          父母生活: '當事人的居住地點附近環境複雜，且屋內並無孩子獨立的失活空間，居家環境不太適合孩子成長。',
          主要照顧: '當事人目前並非與孩子同住，或者並非孩子生活的主要照顧者，對其個性、生活所需上了解可能不足。',
          子女年齡: '孩子尚屬年幼，需要更多細心關照，恐不利當事人長期照顧。',
          人格發展: '孩子年齡已漸入青春期階段，開始發展形塑自己之人格與想法，在人格發展上亟需家人關心與引導，當事人顯然較缺乏合適之溝通技巧，較不利於親職輔導。',
          父母健康: '當事人近年有重大傷病，對負擔孩子之生活照顧恐有疑慮。',
          父母職業: '當事人雖有穩定工作，但常常需要加班或外地出差，對於照顧未成年子女恐有不足之處。',
          子女意願: '孩子年齡已達青少年階段，可清楚表達自己的意思，較不願意與當事人同住。',
          友善父母: '當事人曾將孩子帶回後，不願孩子與對方會面交往，對孩子的成長確有不利之處。',
          父母品行: '當事人曾有不當管教行為，且因涉傷害罪而素行不良，恐影響孩子之健全人格與品行發展。',
        },
      },
    };
  },
  props: {
    configKey: Object,
    rowIdx: Number,
    initialFeature: String,
    initialSentence: String,
  },
  watch: {
    result: {
      handler(val) {
        this.$emit('descriptionUpdate', { key: this.configKey.key, rowIdx: this.rowIdx, value: val.sentence });
        this.$emit('featureUpdate', { key: this.configKey.key, rowIdx: this.rowIdx, value: this.features.filter(feature => feature.value === val.feature) });
      },
      deep: true,
    },
  },
  create() {
    this.dialogState = true;
  },
  computed: {
    warnState() {
      const obj = {
        feature: false,
        sentence: false,
      };
      if (this.result.feature == '') {
        obj.feature = true;
      }
      if (this.result.sentence == '') {
        obj.sentence = true;
      }
      return obj;
    },
  },
  methods: {
    getFeatureDesc(feature) {
      const featureObj = this.features.find(element => element.value == feature);
      if (featureObj) {
        return featureObj.desc;
      }

      return '';
    },
    addInput(data) {
      this.result = {
        feature: data.feature,
        sentence: data.sentence,
      };
      this.dialogState = false;
    },
    clearAll() {
      this.result = {
        feature: '',
        description: '',
      };
    },
  },
};
</script>

<style lang="scss" scoped>
.warn-text {
  font-size: 0.6rem;
  color:#ff4444;
}
.tiny-title {
  font-size: 0.6rem;
  color:#424242;
}
.feature-name {
  font-size: 1rem;
  font-weight: bold;
  height: 1rem;
  margin: 5px 0 15px 0;
  cursor: pointer;
  width: fit-content;
}
.feature-name:hover {
  color: #f1b245;
}
.orange-text {
  color: #F3BB5C;
}
.example-text {
  color: #000;
}
.form-control {
  height: 5rem !important;
}
.statement-card {
  word-break: break-word;
  padding: 10px;
  margin-bottom: 10px;
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
</style>
