<template>
    <div class="index-wrapper">
        <div class="index-left">
            <div class="index-left-block all-products">
                <h2>全部产品</h2>
                <!-- 方法二： -->
                <template v-for="product in productlist">
                    <h3>{{ product.title }}</h3>
                    <ul>
                        <!-- <li v-for="item in productlist.pc.list">
                            <a v-bind:href="item.url">{{ item.title }}</a>
                        </li> -->
                        <li v-for="item in product.list">
                            <a v-bind:href="item.url">{{ item.title }}</a>
                            <span v-if="item.hot" class="hot-tag">HOT</span>
                        </li>
                    </ul>
                    <hr v-if="!product.last">
                </template>
                
                <!-- 方法一： -->
                <!-- <h3>手机应用类</h3>
                <ul>
                    <li v-for="item in productlist.app.list">
                        <a v-bind:href="item.url">{{ item.title }}</a>
                    </li>
                </ul> -->
            </div>
            <div class="index-left-block lastest-news">
                <h2>最新消息</h2>
                <ul>
                    
                    <li v-for='news in newsList'>
                        <a v-bind:href="news.url">{{ news.title }}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="index-right">
            <slider-component></slider-component>
            <div class="index-board-list">
                <div class="index-board-item" v-for="item in boardList">
                    <div class="index-board-item-inner">
                        
                        <h2>{{ item.title }}</h2>
                        <p>快乐个鸡</p>
                        <div class="index-board-button">立即开学</div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import SliderComponent from './silderCompont'
export default {
    components:{
        SliderComponent
    },
  
    mounted() {
        axios.get("getNewsList")
        .then((response) => {
            console.log(response)
            this.newsList = response.data.list
        })
        .catch((error) => {
            console.log(error)
        }),
        axios.get("getProductList")
        .then((response) => {
            console.log(response)
            this.productlist = response.data
        })
        .catch((error) => {
            console.log(error)
        }),
        axios.get("getBoardList")
        .then((response) => {
            console.log(response)
            this.boardList = response.data
        })
        .catch((error) => {
            console.log(error)
        })
    },
    
  
    
    data() {
        return {
            newsList:[],
            productlist:null,
            boardList:null
            
        }
    },
}
</script>

<style scoped>
    .index-wrapper{
        width: 1200px;
        margin: 0 auto;
        display: flex;
    }
    .index-left{
        width:300px;
        /* border: 1px solid black; */
    }
    .index-right{
        width:900px;
    }
    .index-left-block{
        margin: 15px;
        background:#ffffff;
        box-shadow: 0 0 1px #ddd;
        border-radius: 0 0 10px 10px;
    }
    .index-left-block h2{
        color:#ffffff;
        background:green;
        padding: 10px 15px;
        margin-bottom: 15px;
    }
    .all-products h3{
        padding: 0 15px 5px 15px;
        font-weight: bolder;
        color:#222222;
    }
    .index-left-block ul{
        padding: 10px 15px;
    }
    .index-left-block li{
        padding: 5px;
    }
    .hot-tag{
        color: white;
        background:purple;
        font-size:13px;
    }
    .index-board-list{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .index-board-item{
        width: 400px;
        background:yellowgreen;
        box-shadow:0 0 1px #ddd;
        margin-bottom: 20px;
        padding-top: 20px;
    }
    .index-board-item-inner{
        height: 125px;
        padding-left: 120px;
        background: url(../assets/logo.png) no-repeat;
        background-repeat: no-repeat;
        background-size: 20%;
        background-position: 20px;
    }
    .index-board-item-inner h2{
        font-size: 18px;
        font-weight: bolder;
        color: black;
        margin-bottom: 15px
    }
    .index-board-item-inner p{
        margin-bottom: 15px;

    }
    .index-board-button{
        width: 80px;
        height: 30px;
        background:green;
        border-radius: 5px;
        text-align: center;
        line-height: 30px;
    }
    
</style>