<template>
  <el-container>
    <el-header>
      <lin-header></lin-header>
    </el-header>
    <el-container style="height: 700px; border: 1px solid #eee">
      <el-main>
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="12">
            <div class="grid-content">
              <div style="font-size: 7rem; color:#00FFFF;text-align: center;">
                Cython Lin
              </div>
              <br>
              <br>
              <!-- 输入框 -->
              <div>
                <el-input :placeholder="input_placeholder" v-model="input" size='large' @keyup.enter.native="postQuestion" :disabled="input_disable" :autofocus="auto_focus">
                  <el-button slot='append' name='question' style='background-color: #000000' @click='postQuestion' :disabled="input_disable">发送</el-button>
                </el-input>
              </div>
              <!-- 聊天内容 -->
              <el-container>
                <el-main style='height: 450px; border:1px'>
                  <!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32 <br> -->
                  <!-- ele内置滚动条 -->
                  <el-scrollbar>
                    <el-card class="box-card" style='height: 100%; background-color: rgba(0,0,0,0)'>
                      <div class="text item" v-for="per_list,index in question_list" :key="index" :style="{color: index%2==1? rgb2: rgb1} ">
                        <!-- per_list  ['Cython_lin', this.question, this.getTime()] -->
                        [{{per_list[2]}}] {{per_list[0]}}：{{per_list[1]}}
                      </div>
                    </el-card>
                  </el-scrollbar>
                </el-main>
              </el-container>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
    <el-container style="height:90%; border: 1px solid #eee">
      <el-carousel :interval="3000" type="card" height="200px" style='width: 100%;text-align: center;'>
        <el-carousel-item v-for="tuto_url, img_src in flash_imgs" :key="img_src">
          <!-- <nuxt-link to='tuto_url'> <img :src="img_src" width="100%" height="100%"></nuxt-link> -->
          <a :href='tuto_url'> <img :src="img_src" width="100%" height="100%"></a>

        </el-carousel-item>
      </el-carousel>
    </el-container>
    <!-- 底部 -->
    <el-footer>
      <div style="text-align: center;color:rgb(255,255,255);font-size: 1rem;">
        Copyright © 2019 http://cklin.top<br>
        吉ICP备 17008948号
      </div>
    </el-footer>
  </el-container>
</template>
<script>
import Highcharts from 'highcharts';
import LinHeader from '@/components/header.vue'
import axios from 'axios'
import Bscroll from 'better-scroll'

export default {
  components: {
    LinHeader,
  },
  data() {
    return {
      input: '',
      date: new Date(),
      question: '',
      question_list: [],
      answer: '',
      rgb1: '#80FF00',
      rgb2: '#00FFFF',
      input_disable: false,
      input_placeholder: '你随便问，知道算我输  ~。~😄😄😄',
      auto_focus: true,
      refresh: true,
      refresh_key: 0,
      fit: 'fill',
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      flash_imgs: {
        '/flash/cython_lin.png': '/',
        '/flash/python.jpg': 'https://www.python.org/',
        '/flash/tensorflow.png':'https://tensorflow.google.cn/',
        '/flash/HighCharts.png': 'https://www.highcharts.com/',
        '/flash/nuxt.jpg': 'https://nuxtjs.org/',
        '/flash/vue.png': 'https://vuejs.org/',
        '/flash/drf.png': 'https://www.django-rest-framework.org/',
        '/flash/ml.png': 'http://pandas.pydata.org/',
        '/flash/numpy.jpg': 'http://www.numpy.org/',
        '/flash/keras.png': 'https://keras.io/',
        '/flash/sanic.png':'https://sanic.readthedocs.io/en/latest/',
      }
    }
  },
  computed: {

    pushList() {
      // 当计算属性需要传递参数的时候，里面加一层闭包即可
      return (value) => this.question_list.push(value)
    }
  },
  methods: {
    getTime() {
      let _this = this
      // toString().padStart(2,'0') 是为了填充时间
      return `${new Date().getHours().toString().padStart(2,'0')}:${new Date().getMinutes().toString().padStart(2,'0')}:${new Date().getSeconds().toString().padStart(2,'0')}`
    },

    postQuestion() {
      // console.log(this.input)
      this.question = this.input
      // 为了不让时间以制，需要把懒惰执行存起来，然后用的时候后取静态
      this.pushList(['（问）Cython_lin', this.question, this.getTime()])
      // 每次回答初始化
      this.answer = ''
      // 没返回之前，不让用户再次输入，为了样式
      this.input_disable = true
      this.input_placeholder = '正在拼命思考中。。。😣😣😣'
      axios.get('http://39.107.86.223:5000/question', {
        params: { 'question': this.input }
      }).then(
        (response) => {
          this.answer = response['data']
          this.question_list.push(['（答）AI___小虎', this.answer, this.getTime()])
          this.input_disable = false
          this.input_placeholder = '久等啦，继续问吧 ^-^😊😊😊'
        }
      )
      // 清空输入框
      this.input = ''
    },
  },
}

</script>
<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
  padding: 0
}

.el-aside {
  color: #333;
}

.el-main {
  padding: 0;

}


.el-footer {
  background-color: rgb(34, 34, 34);
}



.el-input {
  /*  opacity: 0.8;*/
}

.grid-content {
  /*background-color: rgb(44, 143, 121);*/
  border-radius: 4px;
  min-height: 500px;
  min-width: 400px;
}

</style>
