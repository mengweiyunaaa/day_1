<template>
<!-- lunbotu -->
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <div v-show="index === nowIndex" v-for="(imgUrl,index) in sliderImgList" :key="index" class="slider-item" v-bind:class="['item'+[index+1]]">
            <a href="">
                <img v-bind:src=imgUrl alt="">
            </a>
        </div>
        <!-- dots -->
        <!-- tupianbiaoti -->
        <h2 v-for='(item,title) in sliderImgList'>{{ title }}</h2>
        <!-- javascript:void(0)禁止跳转 -->
        <a v-on:click='preHandler' class='btn pre-btn' href="javascript:void(0)">&lt;</a>
        <a v-on:click='nextHandler' class='btn next-btn' href="javascript:void(0)">&gt;</a>
        <!-- 1234 -->
        <ul class="slider-dots">
            
            <li v-on:click='page(index)' v-for='(item,index) in sliderImgList' :key="index">{{ index+1 }}</li>
            
           
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList:[
                require('../assets/a.jpg'),
                require('../assets/b.jpg'),
                require('../assets/c.jpg'),
                require('../assets/d.jpg')]
        }
    },
    methods: {
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
        },
        nextHandler(){
           this.autoPlay()
        },
        page(index){
            this.nowIndex=index
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex === 4){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoPlay,1000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    // 钩子函数   当页面加载时先加载他
    created() {
        this.runInv()
    },
}
</script>

<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 500px;
        overflow: hidden;
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        position: absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .slider-dots{
        position: absolute;
        right: 50px;
        bottom: 20px;
        z-index: 200;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
        background: #000;
        float: left;
        color: #ffffff;
        opacity: 0.6;
        margin: 0 10px;
    }
    .btn{
        width: 50px;
        height: 50px;
        background: green;
        color: aliceblue;
        position: absolute;
        z-index: 300;
        font-size: 40px;
        text-align: center;
        line-height: 50px;
        top:50%;
    }
    .pre-btn{
        left:10px;
    }
    .next-btn{
        right: 10px;
    }
    .a{
        background: red
    }
</style>