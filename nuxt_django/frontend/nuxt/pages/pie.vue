<template>

  <el-container>

    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>


  <el-container style="height: 1000px; border: 1px solid #eee">
    <el-aside width="200px">
      <el-menu :default-openeds="[]">
        <el-submenu index="3">
          <template slot="title" class='list'><i class="el-icon-menu"></i>Cython_比例
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1" @click="plt_pie(value,year)" v-for="(value,year) in pie" :key='year'><i class="el-icon-time"></i>  {{year}}年</el-menu-item>
            
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

import Highcharts from 'highcharts';
import LinHeader from '@/components/header.vue'


export default {
  components: {
    LinHeader
  },

  data() {
    return {
      name: 'pie',
      pie: this.$store.state.pie.data,
      options: {
        credits: {
          enabled: false //???ʾLOGO 
        },
        chart: {

          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: 'pie',
        },

        title: {
          // text: '?????ͼ',
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %',
              style: {
                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black',
                fontSize: '1.1em',
                fontFamily: "",
              }
            }
          }
        },
        series: [{
          name: '',
          colorByPoint: true,
          data: [{},{}, {},{}, {},{}, {},{}, {},{}, {},{}, {},{}]
        }]
      }
    }

  },
   methods: {
      plt_pie(value, year) {
        var chart = this.$refs.lineCharts.chart

        chart.setSize(1300,700);
        chart.update({'series': value})
        chart.title.update({'text': `（${year}）年领域问题占比`})
        // chart.title.update({'text':11)
      }

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
/*.el-menu-item-group {
  background-color: #000;
}*/

</style>
