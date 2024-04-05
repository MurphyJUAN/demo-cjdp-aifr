import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/components/Main/homePage';
import HomePageDemo from '@/components/Main/homePageDemo';
import UserPredictDemo from '@/components/Main/userPredictDemo';
import UserPredict from '@/components/Main/userPredict';
import UserInputGroup from '@/components/Sub/userInputGroup';
import Links from '@/components/Sub/links';
import GenderSelect from '@/components/Sub/genderAndCountrySelect';
import CheckboxGroup from '@/components/Sub/checkboxGroup';
import SupplementDescription from '@/components/Sub/supplementDescription';
import PredictResult from '@/components/Sub/predictResult';
import ResultFeedback from '@/components/Sub/resultFeedback';
import TechDoc from '@/components/Main/TechDoc';
import ContactUs from '@/components/Main/contactUs';
import ChatBotDemo from '@/components/Main/chatBotDemo';
import VoteMonitor from '@/components/Main/voteMonitor';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
      path: '/demo-home',
      name: 'HomePageDemo',
      component: HomePageDemo,
    },
    {
      path: '/predict-mode4',
      name: 'UserPredictDemo',
      component: UserPredictDemo,
    },
    {
      path: '/demo-predict',
      name: 'UserPredictDemo',
      component: UserPredictDemo,
      children: [
        { path: '/demo-predict/genderSelect', component: GenderSelect },
        { path: '/demo-predict/checkboxGroup', component: CheckboxGroup },
        { path: '/demo-predict/supplementDescription', component: SupplementDescription },
        { path: '/demo-predict/predictResult', component: PredictResult },
        { path: '/demo-predict/resultFeedback', component: ResultFeedback },
      ],
    },
    {
      path: '/voteMonitor',
      name: 'VoteMonitor',
      component: VoteMonitor,
    },
    {
      path: '/links',
      name: 'Link',
      component: Links,
    },
    {
      path: '/techDoc',
      name: 'TechDoc',
      component: TechDoc,
    },
    {
      path: '/contactUs',
      name: 'ContactUs',
      component: ContactUs,
    },
    {
      path: '/userPredict',
      name: 'UserPredict',
      component: UserPredict,
      children: [
        // { path: '/userPredict/genderSelect', component: GenderSelect },
        // { path: '/userPredict/checkboxGroup', component: CheckboxGroup },
        // { path: '/userPredict/supplementDescription', component: SupplementDescription },
        // { path: '/userPredict/predictResult', component: PredictResult },
        // { path: '/userPredict/resultFeedback', component: ResultFeedback },
        { path: ':mode', component: UserInputGroup },
      ],
    },
    {
      path: '/chatbot',
      name: 'ChatBotDemo',
      component: ChatBotDemo,
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/index',
    },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});
