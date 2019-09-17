import Vue from 'vue'
import Highcharts from 'highcharts';
import VueHighcharts from 'highcharts-vue'

import wordcloud from 'highcharts/modules/wordcloud'
import treemap from 'highcharts/modules/treemap'
import sun from 'highcharts/modules/sunburst'



import exporting from 'highcharts/modules/exporting'
// import offlineexporting from 'highcharts/modules/offline-exporting'
// import exportdata from 'highcharts/modules/export-data.js'



import darkUnica from "highcharts/themes/dark-unica"
import darkBlue from "highcharts/themes/dark-blue"

// import oldie from 'highcharts/modules/oldie'
// import more from 'highcharts/highcharts-more'
// import boost from 'highcharts/modules/boost'



if (typeof window !== 'undefined') {

	wordcloud(Highcharts)
	treemap(Highcharts)
	sun(Highcharts)

	exporting(Highcharts)

	darkUnica(Highcharts)
	darkBlue(Highcharts)

	// import VueLoading  from 'vue-loading-template'

	// Vue.use(VueLoading)
	// oldie(Highcharts)
	// more(Highcharts)
	// boost(Highcharts)	

	// map(Highcharts)
	// heatmap(Highcharts)
	// highmaps(Highcharts)
	// more(Highcharts)

}

Vue.use(VueHighcharts)

