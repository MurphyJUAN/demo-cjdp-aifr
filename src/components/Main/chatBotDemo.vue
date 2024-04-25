<!-- eslint-disable max-len -->
<template>
    <div class="page-container">
        <div class="content-container mt-2">
            <b-row>
                <b-col md="7" cols="12" class="chatbot-intro-block">
                    <!-- {{ messageList }} -->
                    <h6>一、說明</h6>
                    <p>透過家事調解員與「Le（Legel）姊家事商談好夥伴」的合作，GPT4模型會為當事人整理出符合民法第1055-1條子女最佳利益的條件，進而以親權判決模型進行獲得親權判決的預測分析，讓家事商談服務，從法庭走入家庭，促進雙方調解成功達成共識，陪伴無助的當事人解開離婚法庭上的搶子難題。</p>
                    <h6>[親權酌定法條：民法第 1055-1 條]</h6>
                    <div class="text-bold">
                        <p>法院為前條裁判時，應依子女之最佳利益，審酌一切情狀，尤應注意下列事項：</p>
                        <p>一、子女之年齡、性別、人數及健康情形。</p>
                        <p>二、子女之意願及人格發展之需要。</p>
                        <p>三、父母之年齡、職業、品行、健康情形、經濟能力及生活狀況。</p>
                        <p>四、父母保護教養子女之意願及態度。</p>
                        <p>五、父母子女間或未成年子女與其他共同生活之人間之感情狀況。</p>
                        <p>六、父母之一方是否有妨礙他方對未成年子女權利義務行使負擔之行為。</p>
                        <p>七、各族群之傳統習俗、文化及價值觀。</p>
                        <p>前項子女最佳利益之審酌，法院除得參考社工人員之訪視報告或家事調查官之調查報告外，並得依囑託警察機關、稅捐機關、金融機構、學校及其他有關機關、團體或具有相關專業知識之適當人士就特定事項調查之結果認定之。</p>
                    </div>

                    <p>如果調解員已熟悉本套系統，可直接點選模式一、二、三，逕行為當事人輸入雙方資訊以獲得判決結果預測。</p>

                </b-col>

                <b-col md="5" cols="12" class="chabot-container-block">
                    <div class="chatbot-container">
                    <div class="header d-flex px-3 align-items-center">
                        <div class="header-title d-inline-flex"><div class="circle mx-2"></div>Le姐</div>
                    </div>

                    <div ref="scrollContainer" class="conversation-container">
                        <!-- <div class="le-talk-block b-w">hi</div> -->
                        <div class="" v-for="item of messageList.filter((v) => v.role !== 'system')">
                            <div class="conversation-card px-4 py-3">
                              <div class="d-inline-flex">
                                <img :src="roleAlias[item.role].src" class="icon mr-2">
                                <div class="font-weight-bold">{{ roleAlias[item.role].name }}：</div>
                              </div>

                                <div>{{ item.content }}</div>
                            </div>
                        </div>
                    </div>

                    <b-row class="le-foot d-inline-flex w-100">
                        <b-col cols="11" class="bottom-input">
                            <textarea rows="1" style="height:auto;" placeholder="請輸入..." v-model="inputMessageContent" @keydown.enter="isTalking || handleSendMessage()"> </textarea>
                        </b-col>
                        <b-col cols="1" class="bottom-send">
                          <img src="../../../static/send.png" class="icon" @click="handleSendMessage()">
                        </b-col>
                    </b-row>

                    </div>
                </b-col>
            </b-row>

        </div>
    </div>

</template>

<script>

export default {

  name: 'chatbotDemo',
  components: {
  },
  data() {
    return {
      // 以後加到環境變量
      apiKey: '',
      inputMessageContent: '',
      isTalking: false,
      roleAlias: {
        assistant: { name: 'Le姐', src: '../../../static/le-pfp.png' },
        user: { name: 'You', src: '../../../static/user-pfp.png' },
      },
      messageList: [
        {
          role: 'system',
          content: '',
        }, {
          role: 'assistant',
          content: '調解委員您好！我是Le姊，一個專門設計來協助處理家事調解相關問題的對話機器人。我可以使用適當的法律用語以及親權相關的法律概念，協助您逐步釐清當事人的情況，並提供親權判決結果預測與專業建議以及推薦適合當事人的的友善資源，以協助您促進雙方達成共識。當然，若在對話過程中，您的問題已超出我程式設計所涵蓋的範圍，我也會建議您直接尋求專業的法律諮詢。現在，你準備好開始對話了嗎？',
        },
      ],
    };
  },
  created() {
    // this.openai = new OpenAI.Api({
    //   apiKey: 'YOUR_API_KEY', // 从环境变量或安全存储获取
    // });
    console.log('key>>>', this.apiKey);
  },
  updated() {
    this.scrollToBottom();
  },
  methods: {
    scrollToBottom() {
      const container = this.$refs.scrollContainer;
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    },
    getAPIKey() {
      if (this.apiKey) return this.apiKey;
      // const aesAPIKey = localStorage.getItem("apiKey") ?? "";
      // apiKey = cryptoJS.AES.decrypt(aesAPIKey, getSecretKey()).toString(
      //     cryptoJS.enc.Utf8
      // );
      return this.apiKey;
    },
    clearMessageContent() {
      this.inputMessageContent = '';
    },
    appendLastMessageContent(content) {
      // 这个方法用来将消息内容添加到 messageList，你可能还需要实现其他逻辑
      this.messageList[this.messageList.length - 1].content += content;
    },
    async chat(messageList, apiKey) {
      console.log('>>>enter chat...');
      try {
        // const response = await fetch('https://api.openai.com/v1/chat/completions', {
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json',
        //     Authorization: `Bearer ${apiKey}`,
        //   },
        //   body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: messageList, stream: true }),
        // });
        // console.log('>>>Start to fetch');
        // return response;
        const response = await fetch('/api/send-messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: messageList }),
        });
        console.log('>>>Start to fetch');
        return response;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async readStream(reader, status) {
      let partialLine = '';
      const decoder = new TextDecoder('utf-8'); // 假设你在函数中使用了解码器

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const decodedText = decoder.decode(value, { stream: true });

        if (status !== 200) {
          const json = JSON.parse(decodedText);
          const content = json.error ? json.error.message : decodedText;
          // TODO
          this.appendLastMessageContent(content.replace(/undefined/g, ''));
          return;
        }

        const chunk = partialLine + decodedText;
        const newLines = chunk.split(/\r?\n/);

        partialLine = newLines.pop() || '';

        for (const line of newLines) {
          if (line.length === 0 || line.startsWith(':')) continue;
          if (line === 'data: [DONE]') return;

          const json = JSON.parse(line.substring(6));
          const content = json.choices ? json.choices[0].delta.content : json.error.message;
          // TODO
          this.appendLastMessageContent(content.replace(/undefined/g, ''));
        }
      }
    },
    sendChatMessage(content = this.inputMessageContent) {
      try {
        this.isTalking = true;
        // # TODO: 這個有必要嗎？
        // if (this.messageList.length === 2) {
        //   this.messageList.pop();
        // }
        this.messageList.push({ role: 'user', content });
        this.clearMessageContent();
        this.messageList.push({ role: 'assistant', content: '' });
        console.log('>>>Before chat...');
        // this.chat(this.messageList, this.getAPIKey());

        this.chat(this.messageList, this.getAPIKey()).then((response) => {
          if (response) {
            const reader = response.body.getReader();
            const status = response.status;
            this.readStream(reader, status);
          }
        });
      } catch (error) {
        this.appendLastMessageContent(error);
      } finally {
        this.isTalking = false;
      }
    },
    handleSendMessage() {
      if (!this.inputMessageContent.length) return;
      this.sendChatMessage();
      this.clearMessageContent();
    },
  },
};
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
@import "vue-select/src/scss/vue-select.scss";
@import "~bootstrap/scss/_functions";
@import "~bootstrap/scss/_variables";
@import "~bootstrap/scss/mixins/_breakpoints";


.chatbot-intro-block {
    background: #F9F9F9;
    max-height: 80vh;
}
// @media (max-width: 767.98px) { /* Bootstrap 的md断点以下 */
//     .chatbot-intro-block {
//         padding: 0;
//     }
//     .col-12 {
//       padding: 0;
//     }
//     .content-container {
//       padding: 0;
//     }
// }
.page-container {
    width: calc( 95% - 40px );
    max-width: 2000px;
    margin: auto;
}
.content-container {
    background-color: #fff;
    border: 2px solid #F3BB5C;
    border-radius: 8px;
    padding: 0px 20px;
    margin-bottom: 50px;
}

.chatbot-container {
    margin: auto;
    width: 100%;
    height: 80vh;
    max-height: 80vh;
    overflow-y: scroll;
    position: relative;
}

.conversation-container {
    max-height: calc(80vh - 72px - 50px);
    overflow-y: scroll;
}
.header {
    height: 45px;
    background: #F9F9F9;
    // color: white;
    font-weight: bold;
    justify-content: space-between;
    border-bottom: 1px solid #E5E8E9;
    font-size: 1rem;
}
// .header-title {
//     border-bottom: 1px solid gray;
// }
.circle {
    width: 5px;
    height: 5px;
    border-radius: 100%;
    background: #D2E854;
    margin: auto;
}
.title-icon {
    width: 1rem;
}
.le-foot{
    min-height: 72px;
    width: 100%;
    padding: 0.5rem;
    // border: 1px solid gray;
    // border-radius: 10px;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto; /* 关键在于这里，使元素水平居中 */
    background: #F9F9F9;
    // background-color: coral; /* 让文本框可见 */
    // justify-content: space-between;
}
.b-w {
    background: white;
}
.bottom-input {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.bottom-input > textarea {
    width: 100%;
    height: 100%;
    border:  1px solid #E5E7EB;
    border-radius: 5px;
    background: transparent;
    padding: 0.5rem;
}
.bottom-send{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;  /* 确保列有足够的高度进行居中对齐 */
}
.le-talk-block {
    width: 100%;
    background: gray;
}

input:focus, textarea:focus, select:focus, button:focus {
    outline: none;
}

.btn-content {
  width: 100%;
  border-radius: 12px;
  border: 2px solid #cfbf84;
}
a {
  text-decoration: none !important;
}
.grid-content {
  border-radius: 4px;
  height: fit-content;
  margin: 1.3rem;
  padding: 0.8rem 2rem;
  text-align: left;
  font-size: 1rem;
  color: #000;
  transition: 0.4s;
  &:hover {
    opacity: 0.8;
    font-size: 1.1rem;
  }
}
.grid-content > strong {
  font-size: 1.2rem;
}
.grid-content > div {
  text-align: left;
}
.bg-white{
  background-color: rgba(243,187,92,0.08);
}
.bg-orange {
  background: #FFD286;
}
.bg-green {
  background: #E1E898;
}
.bg-pink {
  background: #FBCACA;
}
.text-bold {
    font-weight: bold;
    font-style: italic;
}
.icon {
  width: 2rem;
}
</style>

