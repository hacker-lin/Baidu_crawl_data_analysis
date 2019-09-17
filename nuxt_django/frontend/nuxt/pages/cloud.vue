<template>
  <el-container>
    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-aside width="200px">
        <el-menu :default-openeds="[]">
          <el-submenu index="4">
            <template slot="title"><i class="el-icon-menu"></i>Cython_热度</template>
            <el-menu-item-group>
              <el-menu-item index="4-1" @click="plt_cloud(value,year)" v-for="(value,year) in cloud" :key='year'> <i class="el-icon-time"></i>   {{year}}年</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-main>
          <highcharts :options="options" ref="lineCharts"></highcharts>
        </el-main>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
import LinHeader from '@/components/header.vue'

export default {
  components: {
    LinHeader
  },
  data() {
    return {
      name:'cloud',
      cloud: this.$store.state.cloud.data,
      options: {
        credits: {
          enabled: false //不显示LOGO 
        },
        series: [{
          type: 'wordcloud',
          data: [{ name: "Cython_Lin", weight: 100 }]
        }],
        title: {
          text: '词云图'
        }
      }
    }

  },
  methods: {
    plt_cloud(value, year) {
      var chart = this.$refs.lineCharts.chart
      chart.setSize(1280, 980);
      chart.title.update({ 'text': `（${year}）年词云图` })
      chart.update({ 'series': value })
    },

  },
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
