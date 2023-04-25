import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/components/Main/homePage';
import PastCase from '@/components/Main/pastCase';
import UserPredict from '@/components/Main/userPredict';
import UserInputGroup from '@/components/Sub/userInputGroup';
import GenderSelect from '@/components/Sub/genderAndCountrySelect';
import CheckboxGroup from '@/components/Sub/checkboxGroup';
import SupplementDescription from '@/components/Sub/supplementDescription';
import PredictResult from '@/components/Sub/predictResult';
import ResultFeedback from '@/components/Sub/resultFeedback';

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
      path: '/pastCase',
      name: 'PastCase',
      component: PastCase,
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
        { path: ':mode', component: UserInputGroup }
      ],
    },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});
