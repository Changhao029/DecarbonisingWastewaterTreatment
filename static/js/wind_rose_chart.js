var dom7 = document.getElementById('container7');
var myChart7 = echarts.init(dom7, null, {
  renderer: 'canvas',
  useDirtyRect: false
});

var option7;

function create_wind_rose_url(){

  var condition_dict = new Array()
  var condition_str = ""

  if ((start_time && end_time) && (end_time >= start_time)){
      condition_dict["start_time"] = start_time
      condition_dict["end_time"] = end_time
  }
  for (var key in condition_dict){
      condition_str = condition_str + key + "=" + condition_dict[key] + "&"
  }
  condition_str = condition_str.substring(0, condition_str.length - 1)
  console.log(condition_str)
  if (condition_str.length>0){
      var query_url = "http://127.0.0.1:50003/" + interface_url + "/?" + condition_str
  }else{
      var query_url = "http://127.0.0.1:50003/" + interface_url + "/" + condition_str
  }
  return query_url

}

function create_wind_rose_chart(data_result){
  function load_data(){
    var series = [];
    for (var i = 1; i <= 5; i++) {
      series.push({
        type: 'radar',
        symbol: 'none',
        lineStyle: {
          width: 1
        },
        emphasis: {
          areaStyle: {
            color: 'rgba(0,250,0,0.3)'
          }
        },
        data: data_result["data_result"]
      });
    }
    return series
  }

  option7 = {
    title: {
      text: 'Wind Direction Chart',
      top: 10,
      left: 10
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      type: 'scroll',
      bottom: 10,
      data:["231824A","231825A","231826A","231827A","231828A"]
    },
    radar: {
      indicator: [
        { text: 'N', max: data_result["max_value"], axisLabel: { show: true, fontWeight: 'bolder' }},
        { text: 'WN', max: data_result["max_value"]},
        { text: 'W', max: data_result["max_value"]},
        { text: 'SW', max: data_result["max_value"]},
        { text: 'S', max: data_result["max_value"]},
        { text: 'ES', max: data_result["max_value"]},
        { text: 'E', max: data_result["max_value"]},
        { text: 'NE', max: data_result["max_value"]}
      ]
    },
    series: load_data()
  };

  if (option7 && typeof option7 === 'object') {
    myChart7.setOption(option7);
  }

  window.addEventListener('resize', myChart7.resize);
}

$(document).ready(function(){
    $.get("http://127.0.0.1:50003/windrose/",function(data_result,status){
      create_wind_rose_chart(data_result)
    });
});

function chart7_time_range(){
  var start_time = document.getElementById("chart7_start_time").value;
  var end_time = document.getElementById("chart7_end_time").value;
  console.log(start_time, end_time)

  query_url = create_url(start_time, end_time, "windrose")

  $.get(query_url,function(data_result,status){
    create_wind_rose_chart(data_result)
  });
}