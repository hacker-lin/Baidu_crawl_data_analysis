<template>
  <el-container>
    <el-header>
      <lin-header :active='name'></lin-header>
    </el-header>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-aside width="200px">
        <el-menu :default-openeds="[]">
          <el-submenu index="5">
            <template slot="title"><i class="el-icon-menu"></i>Cython_结构</template>
            <el-menu-item-group>
              <el-menu-item index="5-1" @click="plt_matrix(value,year)" v-for="(value,year) in matrix" :key='year'><i class="el-icon-time"></i>{{year}}年</el-menu-item>
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
      name:'matrix',
      matrix: this.$store.state.matrix.data,

      options: {
        credits: {
          enabled: false //不显示LOGO 
        },
        chart: {
          renderTo: 'main'
        },
        series: [{
          type: "treemap",
          layoutAlgorithm: 'squarified',
          allowDrillToNode: true,
          dataLabels: {
            enabled: false
          },
          levelIsConstant: false,
          levels: [{
            level: 1,
            dataLabels: {
              enabled: true
            },
            borderWidth: 3
          }],
          data: ''
        }],
        title: {
          text: ''
        }
      }
    }

  },
  methods: {
    plt_matrix(data, year) {
      var chart = this.$refs.lineCharts.chart

      chart.setSize(1310, 980);

      var points = []
      var region_p,
        region_val,
        region_i,
        country_p,
        country_i,
        cause_p,
        cause_i,
        cause_name = [];


      // cause_name['Communicable & other Group I'] = 'Communicable diseases';
      // cause_name['Noncommunicable diseases'] = 'Non-communicable diseases';
      // cause_name['Injuries'] = 'Injuries';
      region_i = 0;

      for (var region in data) { // 一层 {领域名:{}}
        region_val = 0;
        region_p = {
          id: "id_" + region_i,
          name: region, // 一层名
          color: Highcharts.getOptions().colors[region_i]
        };
        country_i = 0;
        for (var country in data[region]) { // 二层 {二层名:}
          country_p = {
            id: region_p.id + "_" + country_i,
            name: country, // 二层名
            parent: region_p.id
          };
          points.push(country_p);
          cause_i = 0;
          for (var cause in data[region][country]) { // {一层名:{二层名:{三层名:权值}}
            cause_p = {
              id: country_p.id + "_" + cause_i,
              name: cause,
              parent: country_p.id,
              value: Math.round(+data[region][country][cause])
            };
            region_val += cause_p.value;
            points.push(cause_p);
            cause_i++;
          }
          country_i++;
        }
        region_p.value = Math.round(region_val / country_i);
        points.push(region_p);
        region_i++;
      }
      chart.title.update({ 'text': `${year}年矩形树图` })
      chart.update({
        'series': [{
          turboThreshold: 0,
          type: "treemap",
          layoutAlgorithm: 'squarified',
          allowDrillToNode: true,
          dataLabels: {
            enabled: false
          },
          levelIsConstant: false,
          levels: [{
            level: 1,
            dataLabels: {
              enabled: true
            },
            borderWidth: 2
          }],

          data: points
        }]
      })

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
