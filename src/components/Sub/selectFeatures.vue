<template>
  <div class="pb-2">
    <div v-if="allowMultiple">可複選</div>
    <multiselect v-model="result" :options="features" :multiple="allowMultiple" :close-on-select="false" :clear-on-select="false" placeholder="請選擇因素" label="label" track-by="value" :searchable="false">
      <template slot="singleLabel" slot-scope="props"><span class="option__desc"><span class="option__title">{{ props.option.label}}</span></span></template>
      <template slot="option" slot-scope="props">
        <el-tooltip class="item" effect="dark" :content="props.option.desc" placement="top-end">
          <div class="option__title">{{ props.option.label }}<i class="el-icon-question"></i></div>
        </el-tooltip>
      </template>
    </multiselect>
  </div>
</template>

<script>
export default {
  name: 'SelectFeatures',
  data() {
    return {
      result: [],
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
    };
  },
  props: {
    configKey: Object,
    rowIdx: Number,
    allowMultiple: Boolean,
  },
  watch: {
    result: {
      handler(val) {
        this.$emit('featureUpdate', { key: this.configKey.key, rowIdx: this.rowIdx, value: val });
      },
      deep: true,
    },
  },
  methods: {
    clearAll() {
      this.result = [];
    },
  },
};
</script>

<style lang="scss" scoped>
.multiselect * {
  font-size: 1rem !important;
}
// .multiselect__content {
//   font-size: 1rem;
// }
.option__title {
  // font-size: 1rem;
  padding-right: 50px;
}
.container {
  @media (min-width: 1400px) {
    max-width: 1200px;
  }
  @media (min-width: 1000px) and (max-width: 1400px) {
    max-width: 900px;
  }
  @media (max-width: 1000px) {
    max-width: 700px;
  }
}

.column-container {
  @media (max-width: 768px) {
    max-width: 95%;
  }
}
.check-common-sentence {
  max-height: 400px;
  overflow-y: auto;
  overflow-x: hidden;
  border: solid 1px;
  border-color: lightgray;
}
.category-title {
  text-align: left;
  @media (min-width: 500px) {
    margin-left: 10%;
    min-width: 0px;
  }
  @media (max-width: 400px) {
    margin-left: -10%;
    min-width: 0px;
  }
  font-weight: 500;
  font-size: 20px;
}
.checkbox-box {
  width: 10%;
}
.checkbox-content {
  min-width: 70%;
  max-width: 70%;
  line-height: 40px;
  margin-left: 10%;
  @media (max-width: 400px) {
    margin-left: -20%;
    min-width: 0px;
    max-width: 90%;
  }
  li {
    text-align: left;
    font-size: 20px;
  }
}

// input[type="checkbox"] {
//   zoom: 180%;
// }

.custom-control-label::before,
.custom-control-label::after {
  top: 0.5rem;
  width: 1.5rem;
  height: 1.5rem;
}
</style>
