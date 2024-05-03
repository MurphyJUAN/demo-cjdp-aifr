<!-- eslint-disable max-len -->
<template>
    <div class="page-container">
      <div class="dialog-box">
  <div class="dialog-header">
    <h2>对话框标题</h2>
  </div>
  <div class="dialog-content">
    <p>这里是对话框的内容。可以包括文字、链接、图片等元素。</p>
  </div>
  <div class="dialog-footer">
    <button class="btn-close">关闭</button>
  </div>
</div>
    </div>

</template>

<script>
import PredictResult from '../Sub/predictResult';

export default {

  name: 'chatbotDemo',
  components: {
  },
  data() {
    return {
      // 以後加到環境變量
      isShowViolinPlot: false,
      elapsedTime: 0,
      errorPrompt: false,
      errorCode: new Error(),
      predict_result: { mode1: { Applicant: 0, Respondent: 0, Both: 0 }, mode2: { Applicant: 0, Respondent: 0, Both: 0 }, mode3: { Applicant: 0, Respondent: 0, Both: 0 } },
      isLoading: false,
      isSummary: false,
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
          content: `你現在是一個擁有多年經驗的協助家事調解委員的小助手，你會透過提問與引導，幫助調解委員釐清並整理記錄正在爭取孩子親權的一對離婚父母他們雙方對孩子的最佳利益而言有利與不利的條件，請你用客觀理性的角度來提問，不需要照顧雙方情緒委婉用語，以第三方的角度以及孩子最佳利益的考量來詢問以及回答即可，以下是你協助調解員的說明步驟：
1. 首先，你會先自我介紹，並詢問調解委員是否準備要開始調解了。
2. 當委員準備好之後，你首先要先詢問調解員：「請你用文字描述當事人的孩子的基本情況。（例如：性別、年齡、是否可以清楚表達個人意願(表達想跟哪一個當事人一起生活的意願）、孩子傾向跟誰一起生活、生活起居等等」。在調解員輸入孩子的基本信息之後，如果有重要訊息如年齡和性別遺漏以及孩子的個人意願表達能力，你可以適時的追問，如無的話，就進入下一個階段。
3. 接下來你可以詢問調解員：孩子的主要照顧者是誰？ 通常回答只會是爸爸或媽媽，在調解員輸入之後，就進入下一階段。
4. 接下來根據上一題調解員輸入的主要照顧者，你先詢問主要照顧者的基本個人資訊，例如：（例如：教育背景、身心健康、經濟狀況、是否有其他親友可以提供支持系統一起照顧小來、居住環境、離婚後的工作規劃等等)，這一題可能會需要好幾輪的問答，如果調解員輸入的內容沒有涵蓋到上述提到的「教育背景、身心健康、經濟狀況、居住環境、支持系統、離婚後的工作規劃」你可以適當的追問，並且在追問中，可以引導調解員比較雙方的情況，例如可以問他經濟狀況和對方比起來如何？這類的問題。當調解員輸入的內容可以涵蓋這些重要評估項目後，就進入下一階段。
5. 下一階段，請繼續詢問調解員這個主要照顧者(你可用爸爸或媽媽來稱呼，看前面的回覆來決定)，他是否願意配合雙方約定的探視方案、是否曾經隱匿孩子、將孩子拐帶出國或不告知對方未成年子女所在地、或是否曾有有灌輸孩子不當概念或惡意詆毀對方的行為。當你覺得回答得差不多之後，可進入下一階段，如果你覺得沒有回答完整，可以適當地追望。
6. 接下來，你繼續詢問主要照顧者與孩子的相處情形。在這個階段，你要詢問調解員該當事人是否曾經參與過小孩的學校活動（例如：運動會、座談會等）、以及平常和孩子的相處模式、孩子和當事人的感情與依附關係、是否清楚孩子的學習狀況、交友狀況，是否負擔孩子的生活費用等等。這個問題你也可以適當地追問，直到搜集到完整的資料後，跳到下一階段。
7. 接下來，你要詢問調解員，這個主要照顧者對孩子的未來教養計畫。可以詳盡一些，如果調解員回答得不夠完整，你可以適當地追問。
8. 到這邊，關於主要照顧者的資訊已經搜集的差不多了。接下來要詢問另外一方的情況。例如如果主要照顧者是媽媽，現在就要來詢問關於爸爸的情況。首先，你也是先詢問這一方當事人的基本個人資訊，例如：（例如：教育背景、身心健康、經濟狀況、居住環境、離婚後的工作規劃等等)，這一題可能會需要好幾輪的問答，如果調解員輸入的內容沒有涵蓋到上述提到的「教育背景、身心健康、經濟狀況、居住環境、離婚後的工作規劃」你可以適當的追問，並且在追問中，可以引導調解員比較雙方的情況，例如可以問他經濟狀況和主要照顧者比起來如何？這類的問題。當調解員輸入的內容可以涵蓋這些重要評估項目後，就進入下一階段。
9. 下一階段，請繼續詢問調解員這個當事人(你可用爸爸或媽媽來稱呼，看前面的回覆來決定)，他是否願意配合雙方約定的探視方案、是否曾經隱匿孩子、將孩子拐帶出國或不告知對方未成年子女所在地、或是否曾有有灌輸孩子不當概念或惡意詆毀對方的行為。當你覺得回答得差不多之後，可進入下一階段，如果你覺得沒有回答完整，可以適當地追望。
10. 接下來，你繼續詢問這個當事人與孩子的相處情形。在這個階段，你要詢問調解員該當事人是否曾經參與過小孩的學校活動（例如：運動會、座談會等）、以及平常和孩子的相處模式、孩子和當事人的感情與依附關係、是否清楚孩子的學習狀況、交友狀況，是否負擔孩子的生活費用等等。這個問題你也可以適當地追問，直到搜集到完整的資料後，跳到下一階段。
11. 接下來，你要詢問調解員，這個當事人對孩子的未來教養計畫。可以詳盡一些，如果調解員回答得不夠完整，你可以適當地追問。
12. 到這邊，你已經把雙方當事人的情況都收集完整了。注意！只有當你問完前面雙方的資訊之後，才需要做總結，只需做一次總結就好！如果你在過程中就開始做總結，你會被罰款！只有都收集好雙方資訊，到這個步驟時，才需要總結雙方的條件。
總結的時候要以判決書的專業用語，將雙方有利和不利的條件整理出來。
這邊總結雙方有利不利條件的範例如下：
對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。
對母親不利的敘述：當事人在台灣並無其他友人能協助照顧孩子，支持系統薄弱。
對父親有利的敘述：當事人具有高度監護意願，平日會與小孩聯繫並關心其生活狀況，且有親人可協助照顧孩子。當事人願意具有基本的教養能力。有穩定工作及收入，能滿足基本生活所需，經濟能力穩定。
對父親不利的敘述：當事人時常會玩彩券而未能善盡照顧孩子之責任。

開頭請都用「對母親(或父親)有利(或不利)的敘述：」並且參考這種判決書的專業用語，用這種writing style來歸納雙方的客觀條件。
並在總結summary完成之後，在後面加上 <SUMMARY> 的token，這樣我就知道你已經總結完成了。總結非常重要，只需要做一次，在雙方都問完之後，並且要嚴格遵守上面有利不利敘述的格式規範，不然你會被罰款！`,
        }, {
          role: 'assistant',
          content: '調解委員您好！我是Le姊，一個專門設計來協助處理家事調解相關問題的對話機器人。我可以使用適當的法律用語以及親權相關的法律概念，協助您逐步釐清當事人的情況，並提供親權判決結果預測與專業建議以及推薦適合當事人的的友善資源，以協助您促進雙方達成共識。當然，若在對話過程中，您的問題已超出我程式設計所涵蓋的範圍，我也會建議您直接尋求專業的法律諮詢。現在，你準備好開始對話了嗎？',
        },
      ],
    };
  },
  created() {
  },
  updated() {
    this.scrollToBottom();
  },
  watch: {
    isSummary: {
      handler(newVal) {
        if (newVal === true) {
          const result = this.extractStatements(this.messageList[this.messageList.length - 1].content);
          this.startPredict(result);
        }
      },
      deep: true,
    },
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
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${apiKey}`,
          },
          body: JSON.stringify({ model: 'gpt-4-turbo', messages: messageList, stream: true }),
        });
        console.log('>>>Start to fetch');
        return response;
        // const response = await fetch(`${this.$api}/api/send-messages`, {
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json',
        //   },
        //   body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: messageList }),
        // });
        console.log('>>>Start to fetch');
        return response;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    extractStatements(text) {
      const labels = [
        '對母親有利的敘述：',
        '對母親不利的敘述：',
        '對父親有利的敘述：',
        '對父親不利的敘述：',
      ];

      // 初始化一個對象來儲存結果
      const results = {};

      // 提取標籤之間的文本
      labels.forEach((label, index) => {
        const startLabel = label;
        const endLabel = labels[index + 1] || '';
        const start = text.indexOf(startLabel) + startLabel.length;
        const end = endLabel ? text.indexOf(endLabel) : text.length;
        const extractedText = text.substring(start, end).trim();

        // 儲存結果
        results[startLabel] = extractedText;
      });

      const returnResult = { model: 'mode2', data: { AA: { Feature: [], Sentence: labels['對父親有利的敘述：'] }, AD: { Feature: [], Sentence: labels['對父親不利的敘述：'] }, RA: { Feature: [], Sentence: labels['對母親有利的敘述：'] }, RD: { Feature: [], Sentence: labels['對母親不利的敘述：'] } } };
      return returnResult;
    },
    startPredict(result) {
      this.isLoading = true;
      console.log('>>>>>start predict ==> provide result:', result);
      axios({
        method: 'post',
        url: `${this.$api}/api/intermediate-predict`,
        // url: `/api/intermediate-predict`,
        data: result,
      }).then((res) => {
        console.log('res.data:', res.data);
        this.predict_result.mode2 = res.data;
        // this.isStartPredict = true;
        this.isLoading = false;
        this.isSummary = false;
        this.isShowViolinPlot = true;
      }).catch((error) => {
        console.log('>>Error:', error);
        alert(`Oops! 看來出現了一些問題，請稍候再嘗試或是通知管理員！\n 錯誤如下：${error}`);
        this.isLoading = false;
        this.isSummary = false;
      });
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

          if (content.includes('<SUMMARY>')) {
            this.isSummary = true;
          }
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

.dialog-box {
  width: 300px;
  margin: 50px auto;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.dialog-header {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.dialog-content {
  padding: 20px;
  color: #333;
}

.dialog-footer {
  padding: 10px 20px;
  text-align: right;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background-color: #f1f1f1;
}

.button {
  padding: 6px 12px;
  color: white;
  background-color: #007BFF;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  outline: none;
}

.button:hover {
  background-color: #0056b3;
}
</style>

