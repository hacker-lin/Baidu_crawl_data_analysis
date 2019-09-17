<template>
  <el-container>
    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-main>
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="12">
            <div class="grid-content">
              <div style="font-size: 7rem; color:#00FFFF;text-align: center;">
                <el-button @click='start' :disabled='start_unable'>开启爬虫</el-button>
              </div>
              <div style="font-size: 7rem; color:#00FFFF;text-align: center;">
                <el-button><a href="http://39.107.86.223:8000/xadmin/" target="_blank">查看数据</a></el-button>
              </div>
              <div style="font-size: 7rem; color:#00FFFF;text-align: center;">
                <el-button><a href="http://39.107.86.223:8000/" target="_blank">查看Json</a></el-button>
              </div>
              <div style="font-size: 7rem; color:#00FFFF;text-align: center;">
                <el-button @click='stop' :disabled='stop_unable'>关闭爬虫</el-button>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
import LinHeader from '@/components/header.vue'
import axios from 'axios'

export default {
  components: {
    LinHeader
  },
  data() {
    return {
      name: 'spider',
      start_msg: '',
      stop_msg: '',
      start_unable: false,
      stop_unable: true,
    }
  },
  methods: {
    start() {
      axios.get('http://39.107.86.223:8000/spider', {
        params: { 'tag': 'start' }
      }).then(
        (response) => {
          this.tag = Number.parseInt(response['data'])
          if (this.tag === 0) {
            this.start_msg = '开启成功，切记不要重复开启'
            this.start_unable = true
            this.stop_unable = false
            this.start_layer()
 			// this.stop_unable = false


          }
        }
      )
    },

    stop() {
      axios.get('http://39.107.86.223:8000/spider', {
        params: { 'tag': 'stop' }
      }).then(
        (response) => {
          this.tag = Number.parseInt(response['data'])
          if (this.tag === 0) {
            this.stop_msg = '关闭成功，切记不要重复关闭'
            this.start_unable= false
            this.stop_unable = true
            this.stop_layer()
            

          }
        }
      )
    },
    start_layer(){
        this.$notify({
          title: '开启提示',
          message: this.start_msg,
          duration: 0
        });
    },
    stop_layer(){
        this.$notify({
          title: '关闭提示',
          message: this.stop_msg,
          duration: 0
        });
    },



  }

}

</script>
<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
  padding: 0;
}

.el-aside {
  color: #333;
}

.el-main {
  padding: 0
}

</style>
