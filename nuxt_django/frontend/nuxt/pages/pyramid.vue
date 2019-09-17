<template>
  <el-container>
    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-aside width="200px">
        <el-menu :default-openeds="[]">
          <el-submenu index="4">
            <template slot="title"><i class="el-icon-menu"></i>Cython_差异</template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="plt_pyramid(pyramid)"><i class="el-icon-time"></i>全领域问答分布</el-menu-item>
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
      name: 'pyramid',
      pyramid: this.$store.state.pyramid.data,
      categories: ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],

      options: {
        credits: {
          enabled: false //不显示LOGO 
        },
        chart: {
          type: 'bar'
        },
        title: {
          text: '（2011~2019）年所有领域问答分布金字塔图'
        },

        xAxis: [{
          categories: ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
          reversed: false,
          labels: {
            step: 1,
            style: {
              fontSize: '1.1em',
              fontFamily: '微软雅黑'
            },
          }
        }, {
          // 显示在右侧的镜像 xAxis （通过 linkedTo 与第一个 xAxis 关联）
          opposite: true,
          reversed: false,
          categories: ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
          linkedTo: 0,
          labels: {
            step: 1,
            style: {
              fontSize: '1.1em',
              fontFamily: '微软雅黑'
            },
          }
        }],
        yAxis: {
          title: {
            text: null
          },
          labels: {
            formatter: function() {
              return (Math.abs(this.value) / 10000) + 'W';
            },
            style: {
              fontSize: '1.1em',
              fontFamily: '微软雅黑'
            },
          },
          min: -1300000,
          max: 1300000
        },
        plotOptions: {
          series: {
            stacking: 'normal'
          }
        },
        tooltip: {
          // formatter: function() {
          //   return '<b>' + this.series.name + ', age ' + this.point.category + '</b><br/>' +
          //     '人口: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);
          // }
        },
        series: [{
          name: '问题',
          data: [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]
        }, {
          name: '答案',
          data: [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]
        }]
      }
    }

  },
  methods: {
    plt_pyramid(list) {
      var chart = this.$refs.lineCharts.chart
      chart.setSize(1280, 980);
      // chart.title.update({ 'text': `${year}年饼` })
      chart.update({ 'series': list })
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
