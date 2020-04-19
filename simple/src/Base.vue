<template>
  <div id="app">
    
    <div class="app-head">
      <div class='app-head-inner'>
        <img src="./assets/logo.png" alt="">
        <div class="head-nav">
          <ul>
            <li v-on:click='ShowLoginView'>登录</li>
            <li class='nav-pile'>|</li>
            <li>注册</li>
            <li class='nav-pile'>|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app-content">
      <router-view></router-view>
      
    </div>
    <div class="app-foot">
      <p>&copy; mwy</p>
    </div>
    <Mylogin v-show="isShowLoginView"></Mylogin>
  </div>
  
</template>


<script>
// 使用就得引入 建议不加后缀名  
import Mylogin from './components/myLogin'
export default {
  components:{
    Mylogin
  },
  data(){
    return{
      isShowLoginView:false
    }
  },
  methods:{
    ShowLoginView(){
      this.isShowLoginView=true
    }
  }
};
</script>

<style>
/* reset.css 充值样式*/
time, mark, audio, video {
    margin:0;
    padding:0;
    border:0;
    outline:0;
    font-size:100%;
    vertical-align:baseline;
    background:transparent;
    box-sizing:border-box;
}
body {
    line-height:1;
}

:focus {
    outline: 1;
}

article,aside,canvas,details,figcaption,figure,
footer,header,hgroup,menu,nav,section,summary { 
    display:block;
}

ul {
    list-style:none;
}

blockquote, q {
    quotes:none;
}

blockquote:before, blockquote:after,
q:before, q:after {
    content:'';
    content:none;
}

a {
    margin:0;
    padding:0;
    border:0;
    font-size:100%;
    vertical-align:baseline;
    background:transparent;
}

ins {
    background-color:#ff9;
    color:#000;
    text-decoration:none;
}

mark {
    background-color:#ff9;
    color:#000; 
    font-style:italic;
    font-weight:bold;
}

del {
    text-decoration: line-through;
}

abbr[title], dfn[title] {
    border-bottom:1px dotted #000;
    cursor:help;
}

table {
    border-collapse:collapse;
    border-spacing:0;
}

hr {
    display:block;
    height:1px;
    border:0;   
    border-top:1px solid #cccccc;
    margin:1em 0;
    padding:0;
}

input, select {
    vertical-align:middle;
}
/* yangshi*/
body{
  background:white;
  font-size:14px;
  color:black
}
.app-head{
  width: 100%;
  height: 100px;
  line-height: 100px;
  color: rgb(137, 168, 235);
  background: grey;
}
.app-head-inner{
  width: 1200px;
  margin :0 auto;

}
.app-head-inner img{
  width: 50px;
  margin-top: 25px;
  float: left;
}
.head-nav{
  float:rigth;
  

}
.head-nav li {
  float: left;
  cursor: pointer;
  

}
.nav-pile{
  padding: 0 10px
}
.app-foot{
  text-align: center;
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: #cccccc;
  margin-top: 30px
}
.app-content{
  width: 1200px;
  margin: 0 auto;
}
</style>
