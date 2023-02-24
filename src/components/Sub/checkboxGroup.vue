<template>
  <section>
    <h4 class="px-2">步驟一：勾選描述雙方的常見文字</h4>
    <h6>(本選單文字僅供參考。可先點選幾項最接近的描述，再來修改文字即可)</h6>
    <div class="container mt-4 col-12" style="z-index: 100" id="container-checkbox">
      <div class="d-flex column-container pr-1" style="z-index:100">
        <div style="width: 75%"></div>
        <h5 style="width: 10%">父</h5>
        <h5 style="width: 10%">母</h5>
        <div style="width: 5%"></div>
      </div>
      <div class="check-common-sentence column-container" style="z-index:100">
        <ul>
          <div v-for="(item, idxOfItem) in checkboxSentences" :key="item.type + idxOfItem">
            <div class="category-title mt-3">{{item.type}}：</div>
            <div
              v-for="(innerItem, indexOfInnerItem) in item.item"
              :key="innerItem.content + indexOfInnerItem"
            >
              <div
                v-for="n in 2"
                :key="innerItem.content + indexOfInnerItem + n"
              >
                <div v-if="n === 1" class="d-inline-flex justify-content-around w-100">
                  <div style="width: 75%">
                    <div class="checkbox-content d-inline-flex justify-content-start">
                      <li>{{innerItem.content}}</li>
                    </div>
                  </div>

                  <div class="d-inline-flex justify-content-around" style="width: 10%">
                    <div class="checkbox-box custom-control custom-checkbox mr-3">
                      <div v-if="idxOfItem === 8 && indexOfInnerItem === 2" >
                        <input
                          class="custom-control-input"
                          :id="item.type + idxOfItem + indexOfInnerItem + 'Applicant'"
                          type="checkbox"
                          disabled
                        />
                        <label
                          class="custom-control-label"
                          :for="item.type + idxOfItem + indexOfInnerItem + 'Applicant'"
                        ></label>
                      </div>
                      <div v-else>
                        <input
                          class="custom-control-input"
                          :id="item.type + idxOfItem + indexOfInnerItem + 'Applicant'"
                          type="checkbox"
                          @change="setDescriptionData(idxOfItem, indexOfInnerItem)"
                          v-model="innerItem.applicantChecked"
                        />
                        <label
                          class="custom-control-label"
                          :for="item.type + idxOfItem + indexOfInnerItem + 'Applicant'"
                        ></label>
                      </div>
                    </div>
                  </div>
                  <div class="d-inline-flex justify-content-around" style="width: 10%">
                    <div class="checkbox-box custom-control custom-checkbox mr-3">
                      <input
                        class="custom-control-input"
                        :id="item.type + idxOfItem + indexOfInnerItem + 'Respondent'"
                        type="checkbox"
                        @change="setDescriptionData(idxOfItem, indexOfInnerItem)"
                        v-model="innerItem.respondentChecked"
                      />
                      <label
                        class="custom-control-label"
                        :for="item.type + idxOfItem + indexOfInnerItem + 'Respondent'"
                      ></label>
                    </div>
                  </div>

                  <div style="width: 5%"></div>
                </div>
                <div v-else><p></p></div>
              </div>
            </div>

          </div>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "CheckboxGroup",
  data() {
    return {};
  },
  props: {
    checkboxSentences: Array,
    setDescriptionData: Function
  }
};
</script>

<style lang="scss" scoped>

#container-checkbox {
  // border: solid 1px;
  // border-color: lightgray;
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
