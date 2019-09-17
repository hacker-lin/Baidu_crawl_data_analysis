<!-- <el-container>
  <el-header>Header</el-header>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-main>Main</el-main>
  </el-container>
</el-container>
 -->

<template>
  <el-menu :default-active="active" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#000000" text-color='#ffffff' active-text-color='#409EFF'>
   <el-menu-item index="1"><nuxt-link to='/'><span class="iconfont">&#xe606;</span></nuxt-link></el-menu-item>
   <el-menu-item index="2"><nuxt-link to='/plot'>折线图</nuxt-link></el-menu-item>
    <el-menu-item index="3"><nuxt-link to='/bar'>条形图</nuxt-link></el-menu-item>
    
    <el-menu-item index="4"><nuxt-link to='/pyramid'>金字塔</nuxt-link></el-menu-item>

    <el-menu-item index="5"><nuxt-link to='/pie'>饼图</nuxt-link></el-menu-item>
    
    <el-menu-item index="6"><nuxt-link to='/cloud'>词云图</nuxt-link></el-menu-item>

    
    <el-menu-item index="7"><nuxt-link to='/matrix'>矩形树图</nuxt-link></el-menu-item>
    
    <el-menu-item index="8"><nuxt-link to='/sun'>旭日图</nuxt-link></el-menu-item>
    <el-menu-item index="8"><a href='/spider'>爬虫</a></el-menu-item>    

  </el-menu>
 
 
</template>
<script>
export default {
  props: {
    active:String
  },
  data() {
    return {

    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}

</script>

<style>
  * {
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: large;
  }

</style>


<style type="text/css"></style>
