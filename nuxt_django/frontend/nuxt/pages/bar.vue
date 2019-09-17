<template>
    <el-container>
    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>
  <el-container style="height: 1000px; border: 1px solid #eee">
    <el-aside width="200px">
      <el-menu :default-openeds="[]">

        <el-submenu index="1">
          <template slot="title"><i class="el-icon-menu"></i>Cython_分布</template>
          <el-menu-item-group>
            <el-menu-item index="1-1" @click="plt_bar(value,year)" v-for="(value,year) in bar" :key='year'><i class="el-icon-time"></i>{{year}}年</el-menu-item>
          </el-menu-item-group>
        </el-submenu>

      </el-menu>
    </el-aside>


    <el-container>
      <el-main>
        <highcharts :options="options"  ref="lineCharts"></highcharts>
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
    return{
      name:'bar',
      bar: this.$store.state.bar.data,
      options: {
        credits: {
          enabled: false //不显示LOGO 
        },
        chart: {
          type: 'bar'
        },
        title: {
          // text: '发射点犯得上31321'
        },
        xAxis: {
          categories: ['经济金融',
            '企业管理',
            '法律法规',
            '社会民生',
            '科学教育',
            '健康生活',
            '体育运动',
            '文化艺术',
            '电子数码',
            '电脑网络',
            '娱乐休闲',
            '地区',
            '心理分析',
            '医疗卫生'
          ],
          title: {
            text: null
          },
          labels: {
            style: {
              fontSize: '1.1em',
              fontFamily: '微软雅黑'
            },
          }
        },
        yAxis: {

          min: 0,
          title: {
            text: '问题总量 (个)',
            align: 'high'
          },
          labels: {
            style: {
              fontSize: '1.1em',
              fontFamily: '微软雅黑'
            },
            overflow: 'justify'
          }
        },
        tooltip: {

          valueSuffix: ' 个'
        },
        plotOptions: {

          bar: {
            dataLabels: {
              style: {
                fontSize: '1.1em',
                fontFamily: '微软雅黑'
              },
              enabled: true,
              allowOverlap: true // 允许数据标签重叠
            }
          }
        },
        legend: {

          layout: 'vertical',
          align: 'right',
          verticalAlign: 'top',
          x: -40,
          y: 100,
          floating: true,
          borderWidth: 1,
          backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
          shadow: true
        },
        series: [
        {
          name: '问题',
          data: [null,null,null,null,null,null,null,null,null,null,null,null,null,null]
        }, {
          name: '答案',
          data: [null,null,null,null,null,null,null,null,null,null,null,null,null,null]
        }
        ]
      }
    }
  },
  methods: {
    plt_bar(value, year) {
      var chart = this.$refs.lineCharts.chart
      chart.setSize(1320,980);
      chart.title.update({'text':`（${year}）年不同领域的问答数量比较`})
      chart.update({'series': value})
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
  opacity:0.3;
}
.el-main {
  padding: 0
}
/*
el-menu{
  
}
*/
/*element.style {
    border: 0
}*/

</style>
