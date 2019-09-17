<template>
  
<el-container>
<el-header>  <lin-header></lin-header></el-header>

  <el-container style="height: 1000px; border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :default-openeds="[]">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>直方图</template>
          <el-menu-item-group>
            <el-menu-item index="1-1" @click="plt_bar(value,year)" v-for="(value,year) in bar" :key='year'>{{year}}年</el-menu-item>
          </el-menu-item-group>
        </el-submenu>


        <el-submenu index="2">
          <template slot="title"><i class="el-icon-menu"></i>折线图</template>
          <el-menu-item-group>
            <el-menu-item index="2-1" @click="plt_plot(plot)">（2011-2019）年问答分布情况</el-menu-item>
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
  components:{
    LinHeader
  },
  data() {
    return {
      bar: this.$store.state.bar.data,
      plot: this.$store.state.plot.data,
      options: {
        credits: {
          enabled: false //不显示LOGO 
        },
        title: {
          text: '（2011~2019）年领域问题数量趋势图'
        },

        xAxis: {
          lineWidth: 1,
          lineColor: "#1a96ef",
          tickWidth: 0,
          labels: {
            // y: 20, //x轴刻度往下移动20px
            style: {

              fontSize: '1.2em' //字体
            }
          },
          categories: ['One', 'Two', 'three']
        },

        yAxis: {
          tickPositions: [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 82000, 132000, 182000, 232000, 250000],
          gridLineWidth: 1,
          title: {
            style: {
              fontSize: '1.3em',
              fontFamily: '微软雅黑'
            },
            text: '问题数量'
          },
          labels: {

            style: {

              fontSize: '1.2em' //字体
            }
          },

        },
        legend: {

          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },
        plotOptions: {

          series: {
            label: {
              connectorAllowed: false,


            },
            pointStart: 2011
          }
        },
        series: [{
          name: '',
          data: []
        }, {
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },{
          name: '',
          data: []
        },],
        responsive: {
          rules: [{
            condition: {
              maxWidth: 500
            },
            chartOptions: {
              legend: {
                style: {
                  fontSize: '1.5em',
                  fontFamily: '微软雅黑'
                },
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
              }
            }
          }]
        }
      }
    }

  },
  methods: {
    plt_plot(list) {
      console.log(list)
      var chart = this.$refs.lineCharts.chart

      chart.setSize(1310,970);
      chart.update({'series': list})
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
