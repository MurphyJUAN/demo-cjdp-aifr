<!-- eslint-disable max-len -->
<template>
    <div class="ai_junior_award">
        <!-- Navbar -->
          <!-- 大螢幕 -->
          <b-navbar toggleable="lg" fixed="top" :class="{ navbarDefault: hasScrolled,  navbarTop: !hasScrolled}">
            <b-container>
              <b-navbar-nav>
                <b-nav-item href="/ai_junior_award">AIFRxAI Junior Award 2024</b-nav-item>
              </b-navbar-nav>
              <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
              <!-- <b-navbar-nav href="/ai_junior_award">AIFRxAI Junior Award 2024</b-navbar-nav> -->
              <b-collapse id="nav-collapse" is-nav >
                <b-navbar-nav class="ml-auto">
                  <b-nav-item href="/chatbot">首頁</b-nav-item>
                  <b-nav-item href="/chatbot-userPredict/mode1">模式一：選項</b-nav-item>
                  <b-nav-item href="/chatbot-userPredict/mode2">模式二：文字</b-nav-item>
                  <b-nav-item href="/chatbot-userPredict/mode3">模式三：選項加文字</b-nav-item>
                  <!-- <b-nav-item href="/predict-mode4">模式四：選項加文字(多模型)</b-nav-item> -->
                  <b-nav-item href="/chatbot-userDoc">使用說明</b-nav-item>
                  <b-nav-item href="/chatbot-techDoc">技術說明</b-nav-item>
                  <b-nav-item href="/chatbot-links">友善資源</b-nav-item>
                  <b-nav-item href="/chatbot-contactUs">開發團隊</b-nav-item>
                </b-navbar-nav>
              </b-collapse>
            </b-container>
          </b-navbar>


          <!-- <nav class="navbar navbar-default navbar-fixed-top navbar-top">
            <div class="container">
              <div class="navbar-header"><a class="navbar-brand" href="#front_page">PRINT</a></div>
              <div class="navbar-collapse collapse">
                <div class="nav navbar-nav navbar-right">
                  <li><a href="#section_ask">引言 INTRO</a></li>
                  <li><a href="#section_about">簡介 ABOUT</a></li>
                  <li><a href="#section_story">故事 STORY</a></li>
                  <li><a href="#section_future">未來 FUTURE</a></li>
                </div>
              </div>
            </div>
          </nav> -->
          <!-- 大螢幕 -->

        <!-- Navbar -->

        <!-- 首頁 -->

          <!-- 大螢幕 -->
        <header class="jumbotron_front_page" id="front_page">
          <div class="my_container">
            <div class="front_page_title_group" >
              <div data-0="transform: translateY(-50px)" data-600="transform: translateY(100px)">
                <div class="d-inline-flex">
                  <img src="../../../static/le-pfp.png" class="le-icon">
                  <h1 class="front_page_title">Le姐</h1>
                </div>
                <h1 class="front_page_title">家事商談好夥伴</h1>
              </div>
              <hr>
              <h4 class="front_page_title">結合&nbsp生成式AI&nbsp與&nbsp親權判決模型&nbsp解決親權難題</h4>
            </div>
          </div>
          <div class="start-block">
            <div class="ta-block">
              <img src="../../../static/user.png" class="icon-img">
              <h5>調解員</h5>
            </div>
            <div class="button-block">
              <b-button variant="warning" class="start-button"><a href="#intro-and-chatbot-section">開始使用&nbsp↓</a></b-button>
            </div>
          </div>
        </header>
          <!-- 大螢幕 -->

        <!-- 首頁 -->

        <!-- 說明文字 -->
          <!-- 大螢幕 -->
          <section id="intro-and-chatbot-section">
            isSummary: {{ isSummary }}
            {{ messageList }}
            summaryText: {{ summaryText }}
            <img src="../../../static/negotiate.png" class="background-img" data-300="transform: translateX(-200px)" data-700="transform: translateX(0px)">
            <b-container fluid>
              <b-row>
                <b-col class="intro-block" cols="5" data-300="opacity:0" data-700="opacity:1">
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

                <b-col cols="7">
                  <div class="chabot-container-block">
                    <div class="chatbot-container">
                      <div class="header d-flex px-3 align-items-center">
                        <div class="header-title d-inline-flex"><div class="circle mx-2"></div>Le姐</div>
                      </div>

                      <div ref="scrollContainer" class="conversation-container">
                          <div class="" v-for="item of messageList.filter((v) => v.role !== 'system')">
                              <div class="conversation-card px-4 py-3">
                                <div class="d-inline-flex">
                                  <img :src="roleAlias[item.role].src" class="icon mr-2">
                                  <div class="font-weight-bold">{{ roleAlias[item.role].name }}：</div>
                                </div>

                                <div>{{ item.content }}</div>
                                <div v-if="item.status === 'summary'">
                                  如果不需修改，請點擊按鈕：
                                  <button @click="handleStartPredict()">開始預測判決結果...</button>
                                </div>
                                <div v-if="item.status === 'predict'">
                                  <div class="justify-content-center mt-4" :span="24" :xs="24" :sm="24" :md="12" :lg="12" :xl="12" v-for="model in models" :key="model">
                                    <!-- <OnlyViolinPlot :predict_result="predict_result" :model_used="model"></OnlyViolinPlot> -->
                                    <violinPlotChat :predict_result="predict_result['mode2']" :model_used="model"></violinPlotChat>
                                  </div>
                                </div>

                              </div>
                          </div>
                      </div>

                      <div class="le-foot d-inline-flex w-100">
                        <div class="bottom-input">
                            <textarea rows="1" style="height:auto;" placeholder="請輸入..." v-model="inputMessageContent" @keydown.enter="handleEnter"
                            @compositionstart="compositionStart"
                            @compositionend="compositionEnd"> </textarea>
                        </div>
                          <div class="bottom-send">
                            <img src="../../../static/send.png" class="icon" @click="handleSendMessage()">
                          </div>
                      </div>

                    </div>
                  </div>
                </b-col>
              </b-row>
            </b-container>

          </section>

          <!-- 大螢幕 -->


        <!-- 說明文字 -->


        <!-- ChatBot -->


        <!-- ChatBot -->

    </div>

</template>

<script>
import skrollr from 'skrollr';
import axios from 'axios';
import violinPlotChat from '../sub/violinPlotChat.vue';

export default {

  name: 'aiJuniorAward',
  components: {
    violinPlotChat,
  },
  data() {
    return {
      models: ['S1', 'S2'],
      summaryText: null,
      predict_result: { mode1: { Applicant: 0, Respondent: 0, Both: 0 }, mode2: { Applicant: 0, Respondent: 0, Both: 0 }, mode3: { Applicant: 0, Respondent: 0, Both: 0 } },
      isLoading: false,
      isClicked: false,
      isComposing: false,
      isSummary: false,
      isTalking: false,
      inputMessageContent: '',
      hasScrolled: false,
      roleAlias: {
        assistant: { name: 'Le姐', src: '../../../static/le-pfp.png' },
        user: { name: 'You', src: '../../../static/user-pfp.png' },
      },
      messageList: [
        {
          role: 'system',
          status: 'noraml',
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
在總結summary完成之後，必須詢問使用者是否有需要補充或更正的部分，然後在後面加上 <SUMMARY> 的token，這樣我就知道你已經總結完成了。總結非常重要，只需要做一次，在雙方都問完之後，並且要「嚴格遵守」上面有利不利敘述的格式規範以及<SUMMARY>的token，不然你會被罰款！
  13. 如果使用者回覆他需要更改，就在他補充說明以及更改後再做一次總結的步驟，總結的形式跟第12步驟一樣， 開頭請都用「對母親(或父親)有利(或不利)的敘述：」並且參考這種判決書的專業用語，用這種writing style來歸納雙方的客觀條件。
在總結summary完成之後，必須詢問使用者是否有需要補充或更正的部分，然後在後面加上 <SUMMARY> 的token，這樣我就知道你已經總結完成了。總結非常重要，只需要做一次，在雙方都問完之後，並且要嚴格遵守上面有利不利敘述的格式規範以及<SUMMARY>的token，不然你會被罰款！ 如果使用者回覆不需要再調整或補充，你就回覆「謝謝您，接下來會開始進行判決結果預測，請稍等片刻...」必須一字不漏地仿照這個回覆，不要刪減或增加新的字。`,
        }, {
          role: 'assistant',
          status: 'noraml',
          content: '調解委員您好！我是Le姊，一個專門設計來協助處理家事調解相關問題的對話機器人。我可以使用適當的法律用語以及親權相關的法律概念，協助您逐步釐清當事人的情況，並提供親權判決結果預測與專業建議以及推薦適合當事人的的友善資源，以協助您促進雙方達成共識。當然，若在對話過程中，您的問題已超出我程式設計所涵蓋的範圍，我也會建議您直接尋求專業的法律諮詢。現在，你準備好開始對話了嗎？',
        },
        // Debug
        {
          role: 'assistant',
          status: 'summary',
          content: '對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。母親阿霞歷來是孩子的主要照顧者，孩子與母親建立了深厚的感情依附關係，並且對孩子的日常起居提供了充分的照顧。母親已規劃具體且階段性的未來教養計畫，突顯其對孩子教育和情感發展的長期承諾。 對母親不利的敘述：當事人目前無穩定工作和收入來源，經濟狀況可能影響其提供孩子更廣泛的教育和生活資源的能力。母親缺乏較高的教育背景，且在台灣沒有其他親友可以協助照顧孩子，這可能對其提供孩子全面支持造成困難。 對父親有利的敘述：當事人有穩定及較高的經濟狀況，可以為孩子提供更充足的教育和生活資源。父親表現出對孩子的關懷，定期通過通話了解孩子的日常生活和學習情況，顯示其對與孩子保持聯繫的高度意願。 對父親不利的敘述：當事人過去曾有將孩子獨留家中的情形，沒有充分注意孩子的日常需要，這可能對孩子的安全形成風險。儘管有積極的態度，但目前對於如何具體教養孩子仍缺乏明確的規劃和準備，這可能影響他作為主要照顧者的能力。 <SUMMARY>',
        },
      ],

    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    this.skrollrInstance = skrollr.init({
      smoothScrolling: true,
    });
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
    if (this.skrollrInstance) {
      this.skrollrInstance.destroy();
    }
  },
  created() {
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
    startPredict(result) {
      this.isLoading = true;
      console.log('>>>>>start predict ==> provide result:', result);
      // try {
      //   const response = await fetch(`${this.$api}/api/intermediate-predict`, {
      //     method: 'POST',
      //     headers: {
      //       'Content-Type': 'application/json',
      //     },
      //     body: JSON.stringify(result),
      //   });
      //   this.isLoading = false;
      //   this.isSummary = false;
      //   this.isClicked = false;
      //   return response;
      // } catch (error) {
      //   console.log('>>Error:', error);
      //   alert(`Oops! 看來出現了一些問題，請稍候再嘗試或是通知管理員！\n 錯誤如下：${error}`);
      //   this.isLoading = false;
      //   this.isSummary = false;
      //   this.isClicked = false;
      // }
      axios({
        method: 'post',
        url: `${this.$api}/api/intermediate-predict`,
        data: result,
      }).then((res) => {
        console.log('res.data:', res.data);
        this.isLoading = false;
        this.isSummary = false;
        this.isClicked = false;
        this.predict_result.mode2 = res.data;
        this.messageList.push({
          role: 'assistant',
          status: 'predict',
          content: '以下是親權判決模型根據雙方當事人有利與不利的敘述，所做的判決結果預測：',
        });
        return res.data;
      }).catch((error) => {
        console.log('>>Error:', error);
        alert(`Oops! 看來出現了一些問題，請稍候再嘗試或是通知管理員！\n 錯誤如下：${error}`);
        this.isLoading = false;
        this.isSummary = false;
        this.isClicked = false;
      });
    },
    handleStartPredict() {
      this.isClicked = true;
      this.messageList.push({
        role: 'user',
        status: 'noraml',
        content: '你總結得很好，不需要更改，請開始進行判決結果預測。',
      });
      this.summaryText = this.messageList.reduce((lastFound, item) => {
        if (item.status === 'summary') {
          return item.content; // 如果找到符合条件的 item，更新 lastFound
        }
        return lastFound; // 否则保持 lastFound 不变
      }, null); // 初始值为 null，表示如果没有找到任何符合条件的元素，结果为 null
      if (this.summaryText) {
        const result = this.extractStatements(this.summaryText);
        console.log('>>>Extract Result:', result);
        // 開始預測
        const returnData = this.startPredict(result);
      } else {
        this.messageList.push({
          role: 'assistant',
          status: 'noraml',
          content: '目前還沒有取得雙方當事人的詳細敘述，無法做判決結果預測，你是否可以再跟我補充一些雙方當事人的訊息呢？',
        });
      }
    },
    handleEnter(event) {
      if (!this.isComposing && !this.isTalking) {
        this.handleSendMessage();
        event.preventDefault(); // 阻止默认行为，如换行
      }
    },
    compositionStart() {
      this.isComposing = true;
    },
    compositionEnd() {
      this.isComposing = false;
    },
    handleScroll() {
      // 这里设置当页面滚动超过一定距离（比如 100px）时，改变 hasScrolled 的值
      this.hasScrolled = window.scrollY > 0;
    },
    clearMessageContent() {
      this.inputMessageContent = '';
    },
    appendLastMessageContent(content) {
      // 这个方法用来将消息内容添加到 messageList，你可能还需要实现其他逻辑
      this.messageList[this.messageList.length - 1].content += content;
    },
    changeLastMessageStatus(status) {
      this.messageList[this.messageList.length - 1].status = status;
    },
    extractStatements(oldText) {
      const text = oldText.replace('<SUMMARY>', '');

      // 定義標籤
      const labels = [
        '對母親有利的敘述：',
        '對母親不利的敘述：',
        '對父親有利的敘述：',
        '對父親不利的敘述：',
      ];

      // 初始化結果對象
      const results = {};

      // 抽取每個標籤後的文本
      labels.forEach((label, index) => {
        const start = text.indexOf(label) + label.length;
        const end = index < labels.length - 1 ? text.indexOf(labels[index + 1]) : text.length;
        results[label] = text.substring(start, end).trim();
      });

      const returnResult = { model: 'mode2', data: { AA: { Feature: [], Sentence: results['對父親有利的敘述：'] }, AD: { Feature: [], Sentence: results['對父親不利的敘述：'] }, RA: { Feature: [], Sentence: results['對母親有利的敘述：'] }, RD: { Feature: [], Sentence: results['對母親不利的敘述：'] } } };
      return returnResult;
    },
    async readStream(reader, status) {
      console.log('>>>Enter readerStream()');
      const partialLine = '';
      const decoder = new TextDecoder('utf-8'); // 假设你在函数中使用了解码器

      while (true) {
        const { value, done } = await reader.read();
        console.log('>>>value, done', value, done);
        if (done) break;

        const decodedText = decoder.decode(value, { stream: true });

        console.log('>>>decodedText', decodedText);

        if (status !== 200) {
          this.appendLastMessageContent(decodedText);
          return;
        }

        const chunk = partialLine + decodedText;
        this.appendLastMessageContent(chunk);
      }
      // 檢查是否正在做 summary
      if (this.messageList[this.messageList.length - 1].content.includes('<SUMMARY>')) {
        this.isSummary = true;
        this.changeLastMessageStatus('summary');
      }
    },
    async chat(messageList) {
      console.log('>>>enter chat...');
      try {
        const response = await fetch(`${this.$api}/api/send-messages`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ model: 'gpt-4-turbo', messages: messageList }),
        });
        console.log('>>>Start to fetch');
        return response;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    sendChatMessage(content = this.inputMessageContent) {
      try {
        this.isTalking = true;
        this.messageList.push({ role: 'user', status: 'normal', content });
        this.clearMessageContent();
        this.messageList.push({ role: 'assistant', status: 'normal', content: '' });
        // this.chat(this.messageList, this.getAPIKey());

        this.chat(this.messageList).then((response) => {
          console.log('>>>response', response.body, response.status);
          if (response) {
            const reader = response.body.getReader();
            const status = response.status;
            this.readStream(reader, status);
          }
        });
      } catch (error) {
        this.appendLastMessageContent(error);
        this.isTalking = false;
      } finally {
        this.isTalking = false;
      }
    },
    handleSendMessage() {
      this.inputMessageContent = this.inputMessageContent.trim();
      if (!this.inputMessageContent.length) return;
      this.sendChatMessage(this.inputMessageContent);
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

@charset "UTF-8";
* {
  font-family: 宋體-繁;
}

html, body {
  padding: 0;
  margin: 0;
  background: white !important;
}


.ai_junior_award {
  padding: 0;
  margin: 0;
  background: white !important;
  position: relative;
}
header.jumbotron_front_page {
  background-image: url(../../../static/Le姐_cut.png);
  background-size: cover;
  width: 100%;
  height: 100vh;
  background-attachment: fixed;
  position: relative;
}

.start-block{
  position: absolute; /* 使用絕對定位 */
  left: 20%; /* 與右邊界對齊 */
  bottom: 15%; /* 與底部對齊 */
  display: inline-block; /* 讓容器的寬度自適應內容 */
  text-align: center;
}

.my_container {
  position: absolute; /* 使用絕對定位 */
  left: 10%; /* 與右邊界對齊 */
  bottom: 50%; /* 與底部對齊 */
  display: inline-block; /* 讓容器的寬度自適應內容 */
}

.front_page_title_group {
  color: white;
  font-weight: bold;
  text-align: left;
}

 hr {
  transform: translateX(-150%);       /* 從右側開始定位 */
  border: 2px solid #ff6e3a;
  width: 25%;
}

.le-icon {
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 50%; /* 這會使圖片變成圓形 */
  border: 3px solid #ff6e3a; /* 白色邊框，3px 寬 */
  margin-right: 1rem;
}

.icon-img {
  width: 5rem;
  margin-bottom: 1rem;
  opacity: 0.5;

}

.ta-block {
  border: 1px solid rgba(white, 0.5);
  border-radius: 10px;
  padding: 1rem 2rem;
  color: rgba(white, 0.5);
}
.button-block {
  margin-top: 1rem;
}

.start-button {
  background: #ff6e3a;
  font-weight: bold;
  width: 10rem;
  border-radius: 20px;

}
.start-button a {
  color: white;
}

header h4 {
  color: rgba(white, 0.8);
}

#intro-and-chatbot-section {
  background: #FF6F39;
  width: 100%;
  min-height: 100vh;
  position: relative;
  padding: 60px 2rem 0px 2rem;
}

.text-bold {
    font-weight: bold;
    font-style: italic;
}

.intro-block {
  color: #333333;
  padding-right: 50px;
}

.background-img {
  width: 30rem;
  position: absolute;
  bottom: 0;
  left: 0;
  opacity: 0.5;
}

.chatbot-container {
  width: 100%;
  height: 100%;
  background: #F0E9FE;
  opacity: 0.5;
  box-shadow: 10px 10px 20px 0 rgba(0, 0, 0, 0.5);
  position: relative;
  border-radius: 50px;
}

.chabot-container-block {
  width: 100%;
  height: calc(100vh - 85px);
  padding-left: 50px;
  position: relative;
}
.brand-title {
  color: white;
}
.circle {
    width: 5px;
    height: 5px;
    border-radius: 100%;
    background: #D2E854;
    margin: auto;
}


.navbarDefault {
  background-color: #F8F8F8;
  border-bottom: 1px solid #F8F8F8;
  color: #777;
  a {
    color: #fff;
    transition: 0.5s;
    &:hover {
      color: black;
    }
  }
}

.navbarTop {
  background-color: transparent !important;
  border-bottom: 1px solid #e7e7e7 !important;
  color: white !important;
  a {
    color: white !important;
    transition: 0.5s !important;
    &:hover {
      color: #FF6F39 !important;
    }
  }
}

.header {
  width: 100%;
  height: 45px;
  background: #F9F9F9;
  // color: white;
  font-weight: bold;
  justify-content: space-between;
  border-bottom: 1px solid #E5E8E9;
  font-size: 1rem;
  border-radius: 50px 50px 0px 0px;
}

.conversation-container {
    max-height: calc(100vh - 85px - 50px - 60px);
    overflow-y: scroll;
}

.icon {
  width: 2rem;
}

.conversation-card {
  background: white;
  margin: 1rem;
  border-radius: 10px;
  border: 1px solid white;
  // box-shadow: 5px 5px 10px 0 rgba(0, 0, 0, 0.2);
}

.bottom-input {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5px 5px;
}
.bottom-input > textarea {
    width: 100%;
    height: 100%;
    border:  1px solid white;
    border-radius: 5px;
    background: transparent;
    padding: 0.5rem;
}
.bottom-send{
    // width: 100%;
    // height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    // height: 100%;  /* 确保列有足够的高度进行居中对齐 */
    // border: 1px solid rgb(117, 197, 241);
    padding: 5px;
    // background: rgb(117, 197, 241);
    // border-radius: 5px;
}
.le-foot{
    width: 100%;
    position: absolute;
    bottom: 0;
    height: 60px;
    padding: 1.5rem;
}

.navbar-toggler {
  background: #F8F8F8;
}


</style>

