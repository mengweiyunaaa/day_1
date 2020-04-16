import Vue from 'vue'
import VueRouter from 'vue-router'
import Base from './Base.vue'
// import HelloComponent from './HelloComponent.vue'
import InderPage from './components/index.vue'
import mock from './mock/mock'

Vue.use(VueRouter)
// luyou
let router = new VueRouter({
  mode:'history',
  routes:[
    {
      path:'/',
      component:InderPage
    }
  ]
})
// 实例化   注册
new Vue({
  el: '#app',
  router,
  components:{
    Base,
    // HelloComponent
  },
  template:'<Base/>'

})

