var myChart = echarts.init(document.getElementById("barChart"))
var option;
var xAxisData = [];
var seriesData = [];
for (var i = 1; i <= 12; i++) {
	var d = Math.floor(Math.random()*10+1);
	xAxisData.push(i + "h")
	seriesData.push(200 + d)
}
option = {
	title: {
		text: 'Rainfall',
		left: 'center'
	},
	xAxis: {
	  type: 'category',
	  data: xAxisData
	},
	yAxis: {
	  type: 'value'
	},
	series: [
	  {
		data: seriesData,
		type: 'bar'
	  }
	]
};

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);