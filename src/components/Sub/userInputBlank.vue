<template>
  <div class="mt-3">
    <div id="btn-det">
      <div class="d-inline-flex w-100 justify-content-center">
        <div @click="addInputBlank()" style="z-index:100">
          <a class="btn-lg btn-default add-btn" href="javascript:void(0)">新增欄位</a>
        </div>
      </div>
    </div>
    <ul class="data-inner-box mt-3 ml-n4 pl-0 pr-2" :ref="'data-inner-box' + inputBlankId" style="z-index:100">
      <ol reversed>
        <li v-for="(content, index) in userDescriptionList" :key="'hehe'+index">

          <div class="w-100 d-inline-flex" style="margin-top: 10px">
            <resizable-textarea :outerElement="getOuterElement('data-inner-box' + inputBlankId)">
              <textarea
                class="w-100 reasoningText form-control"
                :id="'hehe'+index"
                v-model="userDescriptionList[userDescriptionList.length - index - 1].content"
              ></textarea>
            </resizable-textarea>
            <p class="cancel-btn" @click="cleanInputBlank(index)">X</p>

          </div>

        </li>
      </ol>
    </ul>
  </div>
</template>

<script>

import resizableTextarea from './resizableTextarea';

export default {
  name: 'userInputBlank',
  data() {
    return {
      addBlankCount: 0,
    };
  },
  components: {
    'resizable-textarea': resizableTextarea,
  },
  props: {
    userDescriptionList: Array,
    inputBlankId: Number,
  },
  methods: {
    cleanInputBlank(index) {
      const removedItem = this.userDescriptionList.splice(
        this.userDescriptionList.length - index - 1,
        1,
      );
      // console.log(removedItem[0]);
      if (removedItem[0].groupIndex === 'user') {
        this.addBlankCount = this.addBlankCount - 1;
      }
      // this.$set(this.descriptionList, this.descriptionList.length - index - 1,'');
      // console.log(this.descriptionList);
      this.$emit('setDescriptionLists', this.userDescriptionList, removedItem);
      // console.log(this.addBlankCount);
    },
    addInputBlank() {
      if (this.addBlankCount < 3) {
        this.addBlankCount = this.addBlankCount + 1;
        const record = {
          content: '',
          groupIndex: 'user',
          checkboxIndex: 'none',
        };
        if (this.userDescriptionList.length < 15) {
          this.userDescriptionList.push(record);
          // this.descriptionList.unshift(scope);
        }
        this.$emit('setDescriptionLists', this.userDescriptionList, record);
        // console.log(this.userDescriptionList);
      }
      // console.log(this.addBlankCount);
    },
    getOuterElement(id) {
      // console.log(this.$refs[id]);
      return this.$refs[id];
    }
  },
};
</script>

<style lang="scss" scoped>
.data-inner-box {
  max-height: 300px;
  overflow: auto;
}
.reasoningText {
  vertical-align: top;
  background-color: transparent;
  height: auto;
  @media (min-width: 1800px) {
    font-size: 1.5rem;
  }
}
.cancel-btn {
  line-height: 55px;
  margin-left: 10px;
  color: gray;
  cursor: pointer;
}
.add-btn {
  color: white;
  background-color: gray;
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
</style>
