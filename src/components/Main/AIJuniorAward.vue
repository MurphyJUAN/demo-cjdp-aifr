<!-- eslint-disable max-len -->
<template>
    <div class="ai_junior_award">
        <!-- Navbar -->
          <!-- 大螢幕 -->
          <b-navbar class="navbar-default-large" toggleable="lg" fixed="top" :class="{ navbarDefault: hasScrolled,  navbarTop: !hasScrolled}">
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

          <!-- 大螢幕 -->
          <b-navbar class="navbar-default-small navbarDefault" toggleable="lg" fixed="top">
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

        <!-- Navbar -->

        <!-- 首頁 -->

          <!-- 大螢幕 -->
        <div class="navbar-default-large">
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

        </div>

          <!-- 大螢幕 -->
        <div class="navbar-default-small">
          <header class="jumbotron_front_page_small  px-5" id="front_page">
            <div class="my_container_small">
              <div class="front_page_title_group" >
                <div data-0="transform: translateY(-25px)" data-600="transform: translateY(70px)">
                  <div class="d-inline-flex">
                    <img src="../../../static/le-pfp.png" class="le-icon">
                    <h4 class="front_page_title">Le姐</h4>
                  </div>
                  <h4 class="front_page_title">家事商談好夥伴</h4>
                </div>
                <hr>
                <h5 class="front_page_title">結合&nbsp生成式AI&nbsp與&nbsp親權判決模型&nbsp解決親權難題</h5>
              </div>
            </div>
            <div class="start-block-small mt-2">
              <div class="ta-block">
                <img src="../../../static/user.png" class="icon-img">
                <h5>調解員</h5>
              </div>
              <div class="button-block">
                <b-button variant="warning" class="start-button"><a href="#intro-and-chatbot-section">開始使用&nbsp↓</a></b-button>
              </div>
            </div>
          </header>
        </div>

        <!-- 首頁 -->

        <!-- 說明文字 -->
          <!-- 大螢幕 -->
          <section id="intro-and-chatbot-section">
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

                <b-col cols="7" data-300="opacity:0" data-700="opacity:1">
                  <div class="chabot-container-block">
                    <div class="chatbot-container">
                      <div class="header d-flex px-3 align-items-center">
                        <div class="header-title d-inline-flex"><div class="circle mx-2"></div>Le姐</div>
                        <img class="icon" src="../../../static/edit.png" @click="exportPDF()">
                      </div>

                      <div ref="scrollContainer" class="conversation-container">
                          <div class="" v-for="item of messageList.filter((v) => v.role !== 'system')">
                              <div class="conversation-card px-4 py-3">
                                <div class="d-inline-flex">
                                  <img :src="roleAlias[item.role].src" class="icon mr-2 circle-icon">
                                  <div class="font-weight-bold">{{ roleAlias[item.role].name }}：</div>
                                </div>

                                <div v-if="item.status === 'predict'">
                                  <div class="justify-content-center mt-4" :span="24" :xs="24" :sm="24" :md="12" :lg="12" :xl="12" v-for="model in models" :key="model">
                                    <!-- <OnlyViolinPlot :predict_result="predict_result" :model_used="model"></OnlyViolinPlot> -->
                                    <violinPlotChat :predict_result="predict_result['mode2']" :model_used="model"></violinPlotChat>
                                  </div>
                                  <p></p>
                                </div>

                                <div>{{ item.content }}</div>

                                <div v-if="item.status === 'initial'" class="w-100 d-flex justify-content-end">
                                  <b-button class="function-btn" @click="handleInitialTalk()" variant="light">好</b-button>
                                </div>

                                <div v-if="item.status === 'summary'" class="w-100 d-flex justify-content-end">
                                  如果不需修改，請點擊按鈕：
                                  <b-button class="function-btn" @click="handleStartPredict()" variant="light">開始預測判決結果...</b-button>
                                </div>


                              </div>
                          </div>
                      </div>

                      <div class="le-foot d-inline-flex w-100">
                        <div class="bottom-input">
                            <textarea rows="1" style="height:auto;" placeholder="請輸入..."
                            :disabled="isTalking"
                             v-model="inputMessageContent" @keydown.enter="handleEnter"
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
import OpenCC from 'opencc-js';
import skrollr from 'skrollr';
import axios from 'axios';
import violinPlotChat from '../Sub/violinPlotChat';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

export default {

  name: 'aiJuniorAward',
  components: {
    violinPlotChat,
  },
  data() {
    return {
      currentStage: 'collect-info',
      extractResult: {},
      models: ['S1', 'S2'],
      summaryText: null,
      predict_result: { mode1: { Applicant: 0, Respondent: 0, Both: 0 }, mode2: { Applicant: 0, Respondent: 0, Both: 0 }, mode3: { Applicant: 0, Respondent: 0, Both: 0 } },
      isLoading: false,
      isClickedStartPredictStartPredict: false,
      isComposing: false,
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
  13. 如果使用者回覆他需要更改，就在他補充說明以及更改後再做一次總結的步驟，總結的形式跟第12步驟一樣， 開頭請都用「對母親(或父親)有利(或不利)的敘述：」並且參考這種判決書的專業用語，用這種writing style來歸納雙方的客觀條件。在總結summary完成之後，必須詢問使用者是否有需要補充或更正的部分，然後在後面加上 <SUMMARY> 的token，這樣我就知道你已經總結完成了。總結非常重要，只需要做一次，在雙方都問完之後，並且要嚴格遵守上面有利不利敘述的格式規範以及<SUMMARY>的token，不然你會被罰款！ 如果使用者回覆不需要再調整或補充，你就回覆「謝謝您，接下來會開始進行判決結果預測，請稍等片刻...」必須一字不漏地仿照這個回覆，不要刪減或增加新的字。
  14. 之後以會進行判決結果預測，預測結束後如果使用者有其他數據分析的問題你就繼續跟使用者討論。我在畫面上有將多個判決模型預測出來的判決結果的機率分佈用violin plot呈現，所以如果使用者有關於 violinplot (畫面上有三坨像小提琴一樣胖胖的圖形)，請你跟他解釋這個圖呈現的資訊、意義，如果有關於機器學習、模型預測以及機率分佈是什麼的問題，請你用你的知識告訴他。如無的話，你就建議他可以點擊「友善連結」給當事人看相關可用社會資源。
  
  以上步驟中，最重要的是前面做總結的部分！你在收集完雙方當事人足夠的訊息後，需要做總結，總共只需要做一次總結，並且開頭請都用「對母親(或父親)有利(或不利)的敘述：」並且參考這種判決書的專業用語，用這種writing style來歸納雙方的客觀條件。在總結summary完成之後，必須詢問使用者是否有需要補充或更正的部分，然後在後面加上 <SUMMARY> 的token。這點非常重要！你一定要做好總結的部分，不然會遭到嚴厲的懲罰！`,
        }, {
          role: 'assistant',
          status: 'initial',
          content: '調解委員您好！我是Le姊，一個專門設計來協助處理家事調解相關問題的對話機器人。我可以使用適當的法律用語以及親權相關的法律概念，協助您逐步釐清當事人的情況，並提供親權判決結果預測與專業建議以及推薦適合當事人的的友善資源，以協助您促進雙方達成共識。當然，若在對話過程中，您的問題已超出我程式設計所涵蓋的範圍，我也會建議您直接尋求專業的法律諮詢。現在，你準備好開始對話了嗎？',
        },
        // Debug
        // {
        //   role: 'assistant',
        //   status: 'summary',
        //   content: '對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。母親阿霞歷來是孩子的主要照顧者，孩子與母親建立了深厚的感情依附關係，並且對孩子的日常起居提供了充分的照顧。母親已規劃具體且階段性的未來教養計畫，突顯其對孩子教育和情感發展的長期承諾。 對母親不利的敘述：當事人目前無穩定工作和收入來源，經濟狀況可能影響其提供孩子更廣泛的教育和生活資源的能力。母親缺乏較高的教育背景，且在台灣沒有其他親友可以協助照顧孩子，這可能對其提供孩子全面支持造成困難。 對父親有利的敘述：當事人有穩定及較高的經濟狀況，可以為孩子提供更充足的教育和生活資源。父親表現出對孩子的關懷，定期通過通話了解孩子的日常生活和學習情況，顯示其對與孩子保持聯繫的高度意願。 對父親不利的敘述：當事人過去曾有將孩子獨留家中的情形，沒有充分注意孩子的日常需要，這可能對孩子的安全形成風險。儘管有積極的態度，但目前對於如何具體教養孩子仍缺乏明確的規劃和準備，這可能影響他作為主要照顧者的能力。 <SUMMARY>',
        // },
        // {
        //   role: 'assistant',
        //   status: 'summary',
        //   content: '對母親有利的敘述：當事人無明顯有利的敘述。 對母親不利的敘述：當事人目前吸毒神智不清，又患有精神病，不利於孩子的教養。 對父親有利的敘述：當事人對孩子極其負責並且關係密切。 對父親不利的敘述：當事人無明顯不利的敘述。 <SUMMARY>',
        // },
      ],

    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    this.skrollrInstance = skrollr.init({
      smoothScrolling: true,
    });
    this.checkDeviceType();
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
    // # TODO: 滑到最下面
    this.scrollToBottom();
  },
  methods: {
    handleInitialTalk() {
      this.sendChatMessage('好了', this.currentStage);
    },
    exportPDF() {
      const element = this.$refs.scrollContainer;

      html2canvas(element, {
        scale: 2, // 增加 scale 提高清晰度
      }).then((canvas) => {
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jsPDF('p', 'mm', 'a4');

        const imgWidth = 210; // A4纸的宽度为210mm
        const imgHeight = (canvas.height * imgWidth / canvas.width) / 2; // 调整这里的除数以匹配 PDF 页面大小
        const position = 0;

        pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
        pdf.save('conversation.pdf');
      });
    },
    convertToTraditional(simplifiedText) {
      const converter = OpenCC.Converter({ from: 'cn', to: 'tw' });
      const traditionalText = converter(simplifiedText);
      return traditionalText;
    },
    checkDeviceType() {
      const userAgent = navigator.userAgent || navigator.vendor || window.opera;
      // 使用正则表达式检查 userAgent 字符串是否含有移动设备的标识
      if (/android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(userAgent.toLowerCase())) {
        alert('本網站暫時不適合在手機上使用(很快就會解決)。');
      }
    },
    scrollToSection(refName) {
      const element = document.getElementById(refName);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    },

    scrollToBottom() {
      const container = this.$refs.scrollContainer;
      if (container) {
        container.scrollTo({
          top: container.scrollHeight,
          behavior: 'smooth', // 添加平滑滾動效果
        });
      }
    },
    interpretData(stage) {
      const meseageLst = [
        {
          role: 'system',
          status: 'predict',
          content: `你現在是一個擁有多年數據分析經驗的家事調解分析師，你的工作是以最大化子女最佳利益的核心角度，根據要爭取親權的雙方當事人(父母)各自有利與不利的敘述，解讀兩種BERT-based判決模型(S1, S2)對於(判給父親、判給母親、判給雙方)等三種結果預測出來的機率分佈，結合雙方當事人的情況，做出合理的法官親權判決預測的解讀，以促進調解員根據你的數據解讀進行調解。以下是你的工作流程：
          1. 收到使用者提供的雙方當事人有利與不利的敘述，以及有多個分別來自 S1, S2 模型所做的判決結果預測的數據，這些包括模型們對於三種可能的判決結果(判給父親、判給母親、判給雙方)，所預測出來的平均機率值、最小最大的機率值、Q1, Q2, Q3 的機率值以及這些機率值的標準差。
          2. 請結合雙方當事人有利不利的敘述，以及多個模型所提供的三種可能的判決結果(判給父親、判給母親、判給雙方)的機率分佈，做出合理的解讀。這些機率分佈可以從平均值、標準差、q1, q2, q3 等數值分析，例如標準差越大的話，可能代表模型對這個預測結果比較沒有信心，這時候就需要提醒調解員和當事人審慎使用這個預測結果。記住，我們之所以提供多個來自兩種不同演算法的多個模型的預測機率分佈，就是希望提供一種可信賴的 AI，讓調解員和當事人不要只參考一種模型的預測結果就做出決定，因為每個模型都可能學到不同的 bias。
          以下是一些可能出現的狀況：
          * 有時候兩種算法的模型所產生的機率分佈可能是相反的，例如 S1 的模型預測判給母親的機率比較高，但是 S2 模型判給父親的機率卻比母親還要高，這時候你要結合雙方當事人有利不利的敘述，根據經驗去分析哪一種模型的結果比較可信以及原因是什麼，並且提醒調解員和當事人，這種情況發生，很可能因為遇到的法官不同而有不同的結果，(因為有時候某方當事人可能會很篤定自己一定會贏得親權，如果出現這種相反的結果，就可以給調解員解釋的空間，你可以多從這個角度去分析數據來協助後續調解員跟兩方的溝通)，另外可以請調解員多補充當事人的資訊，提供更詳盡的資料來預測判決結果。
          * 有時候兩種算法所產生的機率分佈都差不多，都傾向判給某一方，這時候你也要分析雙方當事人是什麼樣的條件差距，使得模型會有這樣一致的結果，並建議調解員和當事人由於分佈一致，可以放心參考本次預測結果。
          * 有時候可能是S1的模型傾向判給雙方，但是S2的模型，判給父親的平均機率是 49% ，判給母親的機率是 45% 之類的，這種情況雖然兩種模型預測出來的結果不同，但其實都意味著雙方父母的條件對孩子都是差不多有利或不利的，法官有很高的機率會交給雙方共同擁有親權。
          
          請你嚴格遵守上面的工作流程執行，包括參考雙方當事人以及預測數據的統計資料進行數據解讀，你被禁止使用 Markdown 語法，你只能用純文字和數字輸出，否則你會遭到罰款！
          `,
        },
        {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：當事人與孩子的親子互動自然，具有良好的親職能力。能適時的指正孩子的不良行為，具有基本的教養能力。母親阿霞歷來是孩子的主要照顧者，孩子與母親建立了深厚的感情依附關係，並且對孩子的日常起居提供了充分的照顧。母親已規劃具體且階段性的未來教養計畫，突顯其對孩子教育和情感發展的長期承諾。 對母親不利的敘述：當事人目前無穩定工作和收入來源，經濟狀況可能影響其提供孩子更廣泛的教育和生活資源的能力。母親缺乏較高的教育背景，且在台灣沒有其他親友可以協助照顧孩子，這可能對其提供孩子全面支持造成困難。 對父親有利的敘述：當事人有穩定及較高的經濟狀況，可以為孩子提供更充足的教育和生活資源。父親表現出對孩子的關懷，定期通過通話了解孩子的日常生活和學習情況，顯示其對與孩子保持聯繫的高度意願。 對父親不利的敘述：當事人過去曾有將孩子獨留家中的情形，沒有充分注意孩子的日常需要，這可能對孩子的安全形成風險。儘管有積極的態度，但目前對於如何具體教養孩子仍缺乏明確的規劃和準備，這可能影響他作為主要照顧者的能力。
          以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. S1模型：
            *判給父親: [平均機率：12.438500921548421, 最小機率：0, 最大機率：99.83, Q1:0.07, Q2:0.56, Q3:4.59, 標準差:27.92]
            *判給母親: [平均機率：45.331100512521516, 最小機率：0.01, 最大機率：100, Q1:1.06, Q2:19.87, Q3:98.12, 標準差:45.28]
            *判給雙方: [平均機率：42.230399545115084, 最小機率：0, 最大機率：99.98, Q1:1.41, Q2:19.75, Q3:92.97, 標準差:43.31]
          2. 
            *判給父親: [平均機率：18.312848778841726, 最小機率：0, 最大機率：90.1, Q1:1.39, Q2:11.02, Q3:24.63, 標準差:22.33]
            *判給母親: [平均機率：51.317591493110136, 最小機率：0.02, 最大機率：99.48, Q1:17.15, Q2:54.37, Q3:85.47, 標準差:34.89]
            *判給雙方: [平均機率：30.369559255583834, 最小機率：0.35, 最大機率：99.12, Q1:5.81, Q2:24.61, Q3:43.36, 標準差:28.41]
          請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員調解當事人。
          `,
        },
        {
          role: 'assistant',
          status: 'predict',
          content: `鑑於兩個模型的數據，結合當事人情況，以下是我的建議：
          1. 母親方案的可能性高：兩個模型都顯示判給母親的機率相對較高，這與她作為主要照顧者的事實相符。但調解員應注意她的經濟和教育狀況，可能需要提供額外支持或資源。
          2. 考慮共同親權的可能性：如果法官認為父親能改善對孩子的照顧方式，共同親權也可能是一個適合的選擇，特別是因為兩個模型在許多情況下都給予了不低的機率。
          3. 積極溝通和信息補充：鑑於標準差較大，表明模型預測存在不確定性，建議調解員在實際操作中積極收集更多具體信息，以做出最符合孩子最佳利益的決策。`,
        },
        {
          role: 'user',
          status: 'predict',
          content: `以下是雙方當事人有利不利的敘述：
          對母親有利的敘述：${this.extractResult['對母親有利的敘述：']} 
          對母親不利的敘述：${this.extractResult['對母親不利的敘述：']} 
          對父親有利的敘述：${this.extractResult['對父親有利的敘述：']}  
          對父親不利的敘述：${this.extractResult['對父親不利的敘述：']} 
          以下是多個來自兩種不同演算法所預測出來的判決結果機率分佈：
          1. S1模型：
            *判給父親: [平均機率：${this.predict_result.mode2.S1.Applicant.avg_prob}, 最小機率：${this.predict_result.mode2.S1.Applicant.min}, 最大機率：${this.predict_result.mode2.S1.Applicant.max}, Q1:${this.predict_result.mode2.S1.Applicant.q1}, Q2:${this.predict_result.mode2.S1.Applicant.q2}, Q3:${this.predict_result.mode2.S1.Applicant.q3}, 標準差:${this.predict_result.mode2.S1.Applicant.std}]
            *判給母親: [平均機率：${this.predict_result.mode2.S1.Respondent.avg_prob}, 最小機率：${this.predict_result.mode2.S1.Respondent.min}, 最大機率：${this.predict_result.mode2.S1.Respondent.max}, Q1:${this.predict_result.mode2.S1.Respondent.q1}, Q2:${this.predict_result.mode2.S1.Respondent.q2}, Q3:${this.predict_result.mode2.S1.Respondent.q3}, 標準差:${this.predict_result.mode2.S1.Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result.mode2.S1.Both.avg_prob}, 最小機率：${this.predict_result.mode2.S1.Both.min}, 最大機率：${this.predict_result.mode2.S1.Both.max}, Q1:${this.predict_result.mode2.S1.Both.q1}, Q2:${this.predict_result.mode2.S1.Both.q2}, Q3:${this.predict_result.mode2.S1.Both.q3}, 標準差:${this.predict_result.mode2.S1.Both.std}]
          2. S2
            *判給父親: [平均機率：${this.predict_result.mode2.S2.Applicant.avg_prob}, 最小機率：${this.predict_result.mode2.S2.Applicant.min}, 最大機率：${this.predict_result.mode2.S2.Applicant.max}, Q1:${this.predict_result.mode2.S2.Applicant.q1}, Q2:${this.predict_result.mode2.S2.Applicant.q2}, Q3:${this.predict_result.mode2.S2.Applicant.q3}, 標準差:${this.predict_result.mode2.S2.Applicant.std}]
            *判給母親: [平均機率：${this.predict_result.mode2.S2.Respondent.avg_prob}, 最小機率：${this.predict_result.mode2.S2.Respondent.min}, 最大機率：${this.predict_result.mode2.S2.Respondent.max}, Q1:${this.predict_result.mode2.S2.Respondent.q1}, Q2:${this.predict_result.mode2.S2.Respondent.q2}, Q3:${this.predict_result.mode2.S2.Respondent.q3}, 標準差:${this.predict_result.mode2.S2.Respondent.std}]
            *判給雙方: [平均機率：${this.predict_result.mode2.S2.Both.avg_prob}, 最小機率：${this.predict_result.mode2.S2.Both.min}, 最大機率：${this.predict_result.mode2.S2.Both.max}, Q1:${this.predict_result.mode2.S2.Both.q1}, Q2:${this.predict_result.mode2.S2.Both.q2}, Q3:${this.predict_result.mode2.S2.Both.q3}, 標準差:${this.predict_result.mode2.S1.Both.std}]
          請開始結合雙方當事人的有利不利條件，與上面多個模型預測的機率分佈，進行結果分析，以協助調解員調解當事人。
          `,
        },

      ];

      this.chat(meseageLst, stage).then((response) => {
        if (response) {
          const reader = response.body.getReader();
          const status = response.status;
          this.readStream(reader, status);
          this.appendLastMessageContent('關於數據分析的結果是否還有需要討論的問題？如果沒有的話，在這邊提醒調解員，當您熟悉本套系統後，可直接點選上方導覽列的模式一、二、三直接進行判決預測呦！完成判決結果預測後，調解員也可帶領當事人點選導覽列上方的『友善資源』，共同討論適合當事人使用的友善社會資源，以幫助當事人在離婚後適應生活的變化。謝謝！');
        }
      });
    },
    startPredict(result) {
      this.isLoading = true;
      console.log('>>>>>start predict ==> provide result:', result);
      axios({
        method: 'post',
        url: `${this.$api}/api/intermediate-predict`,
        data: result,
      }).then((res) => {
        console.log('res.data:', res.data);
        this.isLoading = false;
        this.isClickedStartPredict = false;
        this.predict_result.mode2 = res.data;
        this.messageList.push({
          role: 'assistant',
          status: 'predict',
          content: '以上是親權判決模型根據雙方當事人有利與不利的敘述，所做的判決結果預測：',
        });

        // # 開始要求解釋數據
        this.interpretData('do-predict');
        return res.data;
      }).catch((error) => {
        console.log('>>Error:', error);
        alert(`Oops! 看來出現了一些問題，請稍候再嘗試或是通知管理員！\n 錯誤如下：${error}`);
        this.isLoading = false;
        this.isClickedStartPredict = false;
      });
    },
    handleStartPredict() {
      this.isClickedStartPredict = true;
      this.currentStage = 'do-predict';
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
      if (window.scrollY > 0 && !this.hasScrolled) {
        this.hasScrolled = true;
      } else if (window.scrollY === 0 && this.hasScrolled) {
        this.hasScrolled = false;
      }
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

      this.extractResult = results;

      const returnResult = { model: 'mode2', data: { AA: { Feature: [], Sentence: results['對父親有利的敘述：'] }, AD: { Feature: [], Sentence: results['對父親不利的敘述：'] }, RA: { Feature: [], Sentence: results['對母親有利的敘述：'] }, RD: { Feature: [], Sentence: results['對母親不利的敘述：'] } } };
      return returnResult;
    },
    async readStream(reader, status) {
      console.log('>>>Enter readerStream()');
      const partialLine = '';
      const decoder = new TextDecoder('utf-8'); // 假设你在函数中使用了解码器

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const decodedText = this.convertToTraditional(decoder.decode(value, { stream: true }));

        if (status !== 200) {
          this.appendLastMessageContent(decodedText);
          return;
        }

        const chunk = partialLine + decodedText;
        this.appendLastMessageContent(chunk);
      }
      // 檢查是否正在做 summary
      if (this.messageList[this.messageList.length - 1].content.includes('<SUMMARY>')) {
        this.currentStage = 'do-summary';
        this.changeLastMessageStatus('summary');
      }

      this.isTalking = false;
    },
    async chat(messageList, stage) {
      console.log('>>>enter chat...');
      try {
        const response = await fetch(`${this.$api}/api/send-messages`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ model: 'gpt-4-turbo', messages: messageList, stage }),
        });
        console.log('>>>Start to fetch');
        return response;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    sendChatMessage(content = this.inputMessageContent, stage) {
      try {
        this.isTalking = true;
        this.messageList.push({ role: 'user', status: 'normal', content });
        this.clearMessageContent();
        this.messageList.push({ role: 'assistant', status: 'normal', content: '' });
        // this.chat(this.messageList, this.getAPIKey());
        this.chat(this.messageList, stage).then((response) => {
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
      }
    },
    handleSendMessage() {
      this.inputMessageContent = this.inputMessageContent.trim();
      if (!this.inputMessageContent.length) return;
      this.sendChatMessage(this.inputMessageContent, this.currentStage);
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

.navbar-default-small {
  display: block; /* 显示默认样式的 navbar */
}

.navbar-default-large {
  display: none; /* 在小屏幕上隐藏大屏幕的 navbar */
}

/* 媒体查询，适用于大屏幕设备（如宽度大于 992px） */

@media (min-width: 992px) {
  .navbar-default-small {
    display: none; /* 在大屏幕上隐藏小屏幕的 navbar */
  }

  .navbar-default-large {
    display: block; /* 显示大屏幕的 navbar */
  }

}

.jumbotron_front_page_small {
  background-image: url(../../../static/Le_small.png);
  background-size: cover;
  width: 100%;
  height: 100vh;
  background-attachment: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.my_container_small {
  display: inline-block; /* 讓容器的寬度自適應內容 */
}

.start-block-small{
  display: inline-block; /* 讓容器的寬度自適應內容 */
  text-align: center;
}

.jumbotron_front_page {
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

.circle-icon {
  border-radius: 50%; /* 這會使圖片變成圓形 */
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
  background: #FEB59C;
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
  opacity: 0.4;
}

.chatbot-container {
  width: 100%;
  height: 100%;
  background: #F0E9FE;
  opacity: 1;
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

.function-btn {
  border: 1px solid #777;
}


</style>

