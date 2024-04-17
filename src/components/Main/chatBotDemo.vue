<!-- eslint-disable max-len -->
<template>
    <div class="page-container">
        <div class="content-container mt-2">
            <b-row>
                <b-col cols="7" class="chatbot-intro-block">
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

                <b-col cols="5" class="chabot-container-block">
                    <div class="chatbot-container">
                    <div class="header d-flex px-3 align-items-center">
                        <div class="header-title d-inline-flex"><div class="circle mx-2"></div>Le姐 | 家事商談好夥伴</div>

                        <!-- <div class="d-flex">
                            <img class="title-icon mx-1" src="../../../static/moon.png">
                            <img class="title-icon mx-1" src="../../../static/drop.png">
                            <img class="title-icon mx-1" src="../../../static/refresh.png">
                            <img class="title-icon mx-1" src="../../../static/log-in.png">
                        </div> -->
                    </div>

                    <div ref="scrollContainer" class="conversation-container">
                        <!-- <div class="le-talk-block b-w">hi</div> -->
                        <div class="" v-for="item of messageList.filter((v) => v.role !== 'system')">
                            <div class="conversation-card px-4 py-3">
                                <div class="font-weight-bold">{{ roleAlias[item.role] }}：</div>
                                <div>{{ item.content }}</div>
                            </div>
                        </div>
                    </div>

                    <b-row class="le-foot d-inline-flex w-100">
                        <b-col cols="10" class="bottom-input">
                            <input placeholder="請輸入..." v-model="inputMessageContent" @keydown.enter="isTalking || handleSendMessage()">
                        </b-col>
                        <b-col cols="2" class="bottom-send">
                            <b-button variant="outline-primary" class="" @click="handleSendMessage()">送出</b-button>
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
      apiKey: '',
      inputMessageContent: '',
      isTalking: false,
      roleAlias: {
        assistant: 'Le姐',
        user: 'You',
      },
      messageList: [
        {
          role: 'system',
          content: `我會給你一個劇本，你扮演一個叫做 "Le姐" 的角色，接下來我說什麼，你就參考劇本中對應我說的話的下一句回覆我就可以了，要一字不漏的參考劇本。劇本如下: 
          [
            "我": "調解員",
            "Le姐": "請你用文字描述當事人的孩子的基本情況。（例如：性別、年齡、生活起居等等。",
            "我": "雙方當事人有一個小孩－小於，女性，目前九歲就讀台中光明國小三年級，身心狀況良好，平時上下課之餘會參加學校的韻律舞社團，喜歡跳舞和跑步。",
            "Le姐": "了解！那麼小於平時在家中的主要照顧者是誰呢？",
            "我": "媽媽",
            "Le姐": "好的。請你用文字描述母親的基本情況。（例如：教育背景、身心健康、經濟狀況等等",
            "我": "媽媽阿霞之前在市場賣水果，工作時間為上午8時30分至下午5時30分，周休2日。月收入約3萬5千元。在半年前辭職，現在待業在家，沒有收入。阿霞身體健康，之前下班回家就以照護並陪伴孩子為主，住所的生活機能便利，距離幼兒園、公園、學區均車程5分鐘。平常是阿霞負責接送小孩上下學及照顧小孩的三餐起居，孩子相當信任並依賴母親的陪伴，過去孩子出現挑食、罵髒話、沈迷電玩不寫功課的情況，她也能給予孩子適當的訓誡或教導。",
            "Le姐": "你好像忘記提到什麼，可能再補充.... 是否母親有其他親人可以協助照顧小孩？",
            "我": "喔，原本是有母親和弟弟一家可以幫忙照顧小孩，但是去年她弟弟帶著母親一起移民美國了，所以目前沒有親友在台灣。",
            "Le姐": "了解。接下來請你描述母親照顧孩子的情形與孩子目前受扶養的情形。(可以從食衣住行育樂描述）",
            "我": "阿霞照顧孩子的生活起居，負責對孩子進行言行管教、三餐飲食以及就醫等等，除了上班時會把孩子交給學校及補習班，其他時間均由阿霞照料。孩子與阿霞感情互動極佳，阿霞平時也會陪伴孩子玩耍讀書，到運動公園散步。",
            "Le姐": "阿霞目前對孩子小於有怎麼樣的教養計畫呢？",
            "我": "媽媽目前的規劃可以這樣說，就是要確保孩子們在不同階段，能學到適合他們的東西。比如說，在學齡前，不光看重身體健康，情感互動的培養也很關鍵。到了幼稚園，則是特別注重同儕間的相處。到了小學，是在加強小孩的責任心培養，因為這是解決問題的關鍵。將來上了國中，我希望孩子們能全面發展，而到了高中，我更是期望小孩有著積極正面的態度去面對接踵而來的課業難題。",
            "Le姐": "接下來，請你用文字描述父親的基本情況。（例如：教育背景、身心健康、財產與經濟狀況等等",
            "我": "父親阿明目前和母親阿霞和孩子小於是分居的狀況",
            "Le姐": "那麼當事人(父親)的母親是否身心健康，是否能夠支援當事人一起照顧小孩呢？當事人和其共同居住的母親相處情況如何呢？",
            "我": "阿明他媽媽今年六十五歲，雖然有高血壓的問題，但是平常吃藥控制的很好，生活都能自理，阿明上班的時候由他媽媽陪伴小孩是沒什麼問題的，只是老人家只會說台語不會講國語，和小於之間的溝通不是很順暢，但阿明和他媽媽相處得還不錯，家庭氛圍還可以。",
            "Le姐": "謝謝你的補充。接下來請你描述父親照顧孩子的情形與孩子目前受扶養的情形。(可以從食衣住行育樂描述",
            "我": "基本上，每天或隔天爸爸就會打電話過來關心小孩，問問小於在學校的狀況、聊聊天這樣，非常希望小於可以過去他那邊跟他一起生活，小孩也沒有排斥和爸爸相處。但是之前他們還一起住的時候，他常常因為出去跟外面的兄弟一起玩彩券，把小孩自己丟在家，對於小於的一些生活習慣的問題也不太在乎，但是有表示自己願意學習如何教養孩子。",
            "Le姐": "那阿明目前對孩子小於有怎麼樣的教養計畫呢？",
            "我": "目前他還沒有很詳細的規劃，打算是讓小於轉學到新竹住家附近的公立小學，之後就念學區分配的國中和高中，也可以直接把小孩直接送到國外寄宿學校。",
            "Le姐": "謝謝你對雙方當事人的仔細描述。以下是我針對上面資訊所整理的對雙方當事人有利與不利的敘述：
對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。
對母親不利的敘述：當事人在台灣並無其他友人能協助照顧孩子，支持系統薄弱。
對父親有利的敘述：當事人具有高度監護意願，平日會與小孩聯繫並關心其生活狀況，且有親人可協助照顧孩子。當事人願意具有基本的教養能力。有穩定工作及收入，能滿足基本生活所需，經濟能力穩定。
對父親不利的敘述：當事人時常會玩彩券而未能善盡照顧孩子之責任。
請問關於雙方當事人的情況，您是否還有需要補充修改的部分呢？
",
            "我": "無",
            "Le姐": "根據雙方當事人有利與不利的條件，我提供本系統的 AI 親權預測模型預測的法官判決結果如下：
            為了增加系統的可信賴度，我們提供兩種不同模型-S1與S2模型的預測結果，由上述的結果可以得知，S1與S2兩個模型所預測的結果都顯示判給雙方的平均機率是最高的，至少有達到60%以上。S1模型認為判給父親與母親的機率都偏低，但S2模型則顯示判給母親的平均機率雖然低於判給雙方，但其機率分布與後者仍有相當大的重疊區域。這顯示至少在S2模型中，判給母親的機率與判給雙方的機率差異可能沒有那麼大，不過也可能會因為法官有不同的看法做為考量。所以比較合理的解讀是，父親想要單獨贏得親權的機率不大，最有可能的是雙方共同擔任孩子的主要照顧者。
關於這個預測結果，您是否有想要進一步詢問的問題呢？
",
            "我": "有！這個圖怎麼看？為什麼有三坨胖胖的圖形？這代表什麼？我要怎麼跟當事人解釋呢？",
            "Le姐": "這個圖表是violin plot，用來展示和比較數據的分佈情況。想像這每一個'胖胖的圖形'，或者我們叫它小提琴形狀，都代表一組數據的分佈。這三個小提琴形狀，就是我們集成多個模型他們對三個不同結果（判給父親／母親／雙方）可能的預測。每個小提琴的寬度，在不同的數據點高度不一，這表示在那個特定的值上，數據集中的程度。寬度越大，表示更多數據聚集在這個值；寬度越小，則表示數據在這個值上較少。所以，這個'胖胖的'部分，就代表數據最集中的區域。",
            "我": "我懂了！",
            "Le姐": "太好了！ 那麼接下來，您是否需要我針對雙方當事人的狀況提供一些建議呢？",
            "我": "是",
            "Le姐": "因為根據雙方當事人的情況，法官有很大的可能會希望兩邊一同扶養孩子，所以我推薦可以利用下列家事商談服務，兩邊理性溝通雙方可能的合作方式，儘早取得共識，下面是家事商談服務的友善連結：
衛福部社家署的家事商談服務：https://www.sfaa.gov.tw/SFAA/Pages/Detail.aspx?nodeid=1518&pid=12945
兒福聯盟的家事商談服務：https://www.children.org.tw/goodbye/service/288
針對離婚安排尋求共識、解決衝突的合作過程。由專業中立的協談者協助雙方尋求衝突解決方案，做出關於子女生活、探視、教養、居住及財務分配等各項安排，建立雙方教養子女的共識，以節省司法裁判所需的時間與金錢成本，提高履行協議的意願。

另外針對阿霞目前待業的狀況，我也整理並提供下面政府和民間提供的就業輔導服務的友善資源，您可以在之後對當事人的服務中，視情況提供給阿霞參考喔：
台中市就業服務處：
https://www.eso.taichung.gov.tw/1374013/Normalnodelist
台中市失業給付：
https://www.eso.taichung.gov.tw/1374024/Lpsimplelist
"]`,
        }, {
          role: 'assistant',
          content: `您好！我是Le姊，一個專門設計來協助處理家事法相關問題的對話機器人。我可以幫助您了解親權相關的法律概念，使用適當的法律用語，透過逐步引導的方式理解您所碰到的情況，提供專業建議及推薦合適的友善資源。當然，若在對話過程中，您的問題已超出我程式設計所涵蓋的範圍，我也會建議您直接尋求專業的法律諮詢。現在，就讓我們開始進行對話吧！
請問您是家事調解員還是目前正在考慮或申請離婚的當事人呢？
`,
        },
      ],
    };
  },
  created() {
    // this.openai = new OpenAI.Api({
    //   apiKey: 'YOUR_API_KEY', // 从环境变量或安全存储获取
    // });
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
    // async chat(messageList, apiKey) {
    //   console.log('>>>enter chat...');
    //   try {
    //     const response = await fetch('https://api.openai.com/v1/chat/completions', {
    //       method: 'POST',
    //       headers: {
    //         'Content-Type': 'application/json',
    //         Authorization: `Bearer ${apiKey}`,
    //       },
    //       body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: messageList, stream: true }),
    //     });

    //     const reader = response.body.getReader();
    //     let completeContent = '';
    //     let accumulatedJson = '';
    //     let startPosFound = false;

    //     while (true) {
    //       const { done, value } = await reader.read();
    //       if (done) break;

    //       let textChunk = new TextDecoder('utf-8').decode(value, { stream: true });

    //       // Removing any non-JSON prefix like "data:"
    //       if (!startPosFound) {
    //         const startPos = textChunk.indexOf('{');
    //         if (startPos !== -1) {
    //           textChunk = textChunk.substring(startPos);
    //           startPosFound = true;
    //         } else {
    //           continue; // Skip this iteration if start of JSON not found yet
    //         }
    //       }

    //       accumulatedJson += textChunk;

    //       // Check if we have a complete JSON object
    //       try {
    //         const json = JSON.parse(accumulatedJson);
    //         const message = json.choices[0]?.delta?.content || '';
    //         if (message) {
    //           completeContent += message;
    //           this.$set(this.messageList, this.messageList.length - 1, {
    //             role: 'assistant',
    //             content: completeContent,
    //           });

    //           // Reset for next JSON object
    //           accumulatedJson = '';
    //           startPosFound = false;
    //         }
    //       } catch (error) {
    //         console.error('Continuing to accumulate JSON...', error);
    //         // Do not reset accumulatedJson here as more data might be needed to complete the JSON
    //       }
    //     }
    //   } catch (error) {
    //     console.error('Error:', error);
    //   }
    // },
    async chat(messageList, apiKey) {
      console.log('>>>enter chat...');
      try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${apiKey}`,
          },
          body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: messageList, stream: true }),
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
        if (this.messageList.length === 2) {
          this.messageList.pop();
        }
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
    overflow-y: scroll;
}
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
.bottom-input > input {
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
</style>

