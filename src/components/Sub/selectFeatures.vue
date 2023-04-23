<template>
  <div>
    <div>可複選</div>
    <multiselect v-model="result" :options="features" :multiple="true" :close-on-select="false" :clear-on-select="false" placeholder="請選擇因素" label="label" track-by="value">
    </multiselect>
  </div>
</template>

<script>
export default {
  name: "CheckboxGroup",
  data() {
    return {
      result: [],
      features: [
        { label: '親子感情', value: '親子感情' },
        { label: '意願能力', value: '意願能力' },
        { label: '父母經濟', value: '父母經濟' },
        { label: '支持系統', value: '支持系統' },
        { label: '父母生活', value: '父母生活' },
        { label: '主要照顧', value: '主要照顧' },
        { label: '子女年齡', value: '子女年齡' },
        { label: '人格發展', value: '人格發展' },
        { label: '父母健康', value: '父母健康' },
        { label: '父母職業', value: '父母職業' },
        { label: '子女意願', value: '子女意願' },
        { label: '友善父母', value: '友善父母' },
        { label: '父母品行', value: '父母品行' },
      ],
    };
  },
  props: {
    configKey: String
  },
  watch: {
    result: {
      handler(val) {
        this.$emit('featureUpdate', { key: this.configKey, value: val})
      },
      deep: true,
    },
  },
  methods: {
    clearAll() {
      this.result = []
    }
  }
};
</script>

<style lang="scss" scoped>
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
