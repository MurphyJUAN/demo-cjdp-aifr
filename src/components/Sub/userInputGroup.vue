<template>
  <el-row justify="space-between" :gutter="1">
    <el-col :xs="24" :sm="12" v-for="(colConfigs, idx) in resultConfig" :key="idx">
      <div class="p-3 w-100" v-for="config in colConfigs" :key="config.title" :class="idx==0?'brown-divider':''">
        <div v-if="$route.params.mode == 'mode1'" class="ins-1">對{{config.title}}的因素選項</div>
        <div v-if="$route.params.mode == 'mode2'" class="ins-1">對{{config.title}}的理由文字</div>
        <div v-if="$route.params.mode == 'mode3'" class="ins-1">對{{config.title}}的因素與理由</div>

        <div v-if="$route.params.mode == 'mode1'">
          <select-features :configKey="config.key" @featureUpdate="updateFeature" ref="selectForm"></select-features>
        </div>

        <div v-if="$route.params.mode == 'mode2'">
          <input-description :configKey="config.key" @descriptionUpdate="updateDescription" ref="inputForm"></input-description>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import selectFeatures from './selectFeatures';
import inputDescription from './inputDescription';

export default {
  name: 'UserInputGroup',
  components: {
    'select-features': selectFeatures,
    'input-description': inputDescription,
  },
  props: {
  },
  data() {
    return {
      resultConfig: [
        [
          { title: '父親有利', type: 'A', key: 'AA', dialog: false },
          { title: '父親不利', type: 'D', key: 'AD', dialog: false },
        ],
        [
          { title: '母親有利', type: 'A', key: 'RA', dialog: false },
          { title: '母親不利', type: 'D', key: 'RD', dialog: false },
        ]
      ],
      result: {
        data: {
          AA: { Sentence: '', Feature: [] },
          AD: { Sentence: '', Feature: [] },
          RA: { Sentence: '', Feature: [] },
          RD: { Sentence: '', Feature: [] },
        },
      }
    };
  },
  watch: {
    result: {
      handler(val) {
        this.$emit('resultUpdate', val)
      },
      deep: true,
    },
  },
  methods: {
    updateFeature(val) {
      console.log('updateFeature', val)
      this.result.data[val.key].Feature = []
      for(let i=0;i<val.val.value.length;i++) {
        this.result.data[val.key].Feature.push(val.val.value[i].label)
      }
      console.log(this.result)
    },
    updateDescription(val) {
      console.log('updateDescription', val)
      this.result.data[val.key].Sentence = val.val
    },
    clearAllStatement() {
      this.result.data = {
        AA: { Sentence: '', Feature: [] },
        AD: { Sentence: '', Feature: [] },
        RA: { Sentence: '', Feature: [] },
        RD: { Sentence: '', Feature: [] },
      };
      this.$refs.selectForm.clearAll()
      this.$refs.inputForm.clearAll()
    },
  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
.brown-divider {
  border-right: 1px solid #5A4D30;
}
.ins-1 {
    font-size: 1.2rem;
    font-weight: bold;
    padding-top: 15px;
}
.example-btn {
    border-radius: 4px;
    background-color: #5A4D30;
    width: 100%;
    height: 100%;
    color: #fff;
    font-weight: bold;
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
</style>
