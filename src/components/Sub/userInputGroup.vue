<template>
  <el-row justify="space-between" :gutter="5">
    <el-col :xs="24" :sm="12" v-for="(colConfigs, idx) in resultConfig" :key="idx">
      <div class="px-3 pb-2 w-100" v-for="config in colConfigs" :key="config.title" :class="idx==0?'brown-divider':''">
        <div v-if="$route.params.mode == 'mode1'" class="ins-1">對{{config.title}}的因素選項</div>
        <div v-if="$route.params.mode == 'mode2'" class="ins-1">對{{config.title}}的理由文字</div>
        <div v-if="$route.params.mode == 'mode3'" class="ins-1">對{{config.title}}的因素與理由</div>

        <div v-if="$route.params.mode == 'mode1'">
          <select-features :configKey="config" :rowIdx="0" :allowMultiple="true" @featureUpdate="updateFeature" ref="selectForm"></select-features>
        </div>

        <div v-if="$route.params.mode == 'mode2'">
          <input-description-m2 :configKey="config" :rowIdx="0" @descriptionUpdate="updateDescription" ref="inputForm"></input-description-m2>
        </div>

        <div v-if="$route.params.mode == 'mode3'">
          <div v-for="(inputRow, rowIdx) in result.data[config.key]" :key="inputRow.rowIdx">
            <el-row :gutter="5">
              <el-col :span="1">
                {{ rowIdx+1 }}.
              </el-col>
              <el-col :span="21" >
                <input-description-m3
                  :configKey="config"
                  :rowIdx="rowIdx"
                  @featureUpdate="updateFeature" 
                  @descriptionUpdate="updateDescription" 
                  v-on="$listeners"
                  ref="inputForm">
                </input-description-m3>
              </el-col>
              <el-col v-if="rowIdx == result.data[config.key].length-1" :span="2">
                <el-button type="danger" icon="el-icon-delete" circle @click="deleteInputRow(config.key, rowIdx)"></el-button>
              </el-col>
            </el-row>
          </div>
          <div>
          <el-row :gutter="1">
            <el-col :offset="1" :span="23">
              <el-button type="warning" @click="addInputRow(config.key)">新增因素與理由</el-button>
            </el-col>
          </el-row>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import selectFeatures from './selectFeatures';
import inputDescriptionM2 from './inputDescriptionM2';
import inputDescriptionM3 from './inputDescriptionM3';

export default {
  name: 'UserInputGroup',
  components: {
    'select-features': selectFeatures,
    'input-description-m2': inputDescriptionM2,
    'input-description-m3': inputDescriptionM3
  },
  props: {
    prePredict: Boolean
  },
  data() {
    return {
      resultConfig: [
        [
          { title: '父親有利', type: 'A', key: 'AA'},
          { title: '父親不利', type: 'D', key: 'AD'},
        ],
        [
          { title: '母親有利', type: 'A', key: 'RA'},
          { title: '母親不利', type: 'D', key: 'RD'},
        ]
      ],
      result: {
        data: {
          AA: [{ Sentence: '', Feature: [] }],
          AD: [{ Sentence: '', Feature: [] }],
          RA: [{ Sentence: '', Feature: [] }],
          RD: [{ Sentence: '', Feature: [] }],
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
    '$route.params.mode': {
      handler: function(mode) {
        delete this.result.data
        if (mode == 'mode3') {
          delete this.result.data
          this.result =  {
            data: {
              AA: [],
              AD: [],
              RA: [],
              RD: [],
            },
          }
        }
        else {
          this.result =  {
            data: {
              AA: [{ Sentence: '', Feature: [] }],
              AD: [{ Sentence: '', Feature: [] }],
              RA: [{ Sentence: '', Feature: [] }],
              RD: [{ Sentence: '', Feature: [] }],
            },
          }
        }
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    deleteInputRow(key, rowIdx) {
      let resultAry = JSON.parse(JSON.stringify(this.result.data[key]))
      if (rowIdx > -1) {
        resultAry.splice(rowIdx, 1)
      }
      this.$set(this.result.data, key, resultAry);
      console.log(rowIdx, this.result.data)
    },
    addInputRow(key) {
      this.result.data[key].push({ Sentence: '', Feature: [] })
    },
    updateFeature(val) {
      console.log('updateFeature', val)
      if (typeof val.value === 'object' && val.value !== null) {
        let features = []
        for(let i=0;i<val.value.length;i++) {
          features.push(val.value[i].label)
        }
        this.result.data[val.key][0].Feature = features
      }
      else {
        this.result.data[val.key][val.rowIdx].Feature = [val.value]
      }
    },
    updateDescription(val) {
      console.log('updateDescription', val)
      this.result.data[val.key][val.rowIdx].Sentence = val.value
    },
    clearAllStatement() {
      console.log('clearAllStatement')
      this.result.data = {
        AA: [{ Sentence: '', Feature: [] }],
        AD: [{ Sentence: '', Feature: [] }],
        RA: [{ Sentence: '', Feature: [] }],
        RD: [{ Sentence: '', Feature: [] }],
      };
      if (this.$refs.selectForm) {
        for (let i = 0; i < this.$refs.selectForm.length; i++) {
          this.$refs.selectForm[i].clearAll()
        }
      }
      if (this.$refs.inputForm) {
        for (let i = 0; i < this.$refs.inputForm.length; i++) {
          this.$refs.inputForm[i].clearAll()
        }
      }
    }
  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss" scoped>
.brown-divider {
  border-right: 1px solid #5A4D30;
}
@media screen and (max-width:768px) { 
  .brown-divider {
    border-right: 0px;
  }
}
.ins-1 {
    font-size: 1rem;
    font-weight: bold;
    padding: 10px 0;
}
</style>
