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
  option7 = {
      "title": {
          "text": "Wind Speed and Wind Direction Rose Chart",
          "left": "left",
          "top": "10",
           subtext: "from " + data_result["start_time"] + " to " + data_result["end_time"]
      },
      grid:{
               x:600,
               y:600,
      },
      toolbox: {
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            },
      },
      "legend": {
          "show": true,
          "top": "30",
          "right": "right",
          "data": ["<1(m/s)", "1-2(m/s)", "2-4(m/s)", "4-6(m/s)", "6-8(m/s)", "8-10(m/s)", ">10(m/s)"],
          "orient": "vertical"
      },
      "tooltip": {
          "formatter": "{a}<br/>{b}：{c}%"
      },
      "color": ["#1E98E3", "#1EE3D4", "#1EE363", "#AAE31E", "#E3CB1E", "#E3981E", "#E3511E"],
      "angleAxis": {
          "type": "category",
          "data": ["N", "NW", "W", "SW", "S", "SE", "E", "NE"],
          "z": 0,
          "boundaryGap": false,
          "splitLine": {
              "show": true,
              "lineStyle": {
                  "color": "#ddd",
                  "type": "solid",
                  "width":2
              }
          },
          "axisLine": {
              "show": false
          }
      },
      "radiusAxis": {
          "name": "frequency(%)",
          "nameLocation": "middle",
          splitArea: {
              show: true,
              areaStyle: {
                  color: ["rgba(0,0,0,.01)", "rgba(0,0,0,.2)"]
              },
               "width":2

          },
      },
      "polar": {},
      "series": [{
          "type": "bar",
          "data": data_result["data"][0],
          "coordinateSystem": "polar",
          "name": "<1(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][1],
          "coordinateSystem": "polar",
          "name": "1-2(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][2],
          "coordinateSystem": "polar",
          "name": "2-4(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][3],
          "coordinateSystem": "polar",
          "name": "4-6(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][4],
          "coordinateSystem": "polar",
          "name": "6-8(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][5],
          "coordinateSystem": "polar",
          "name": "8-10(m/s)",
          "stack": "a"
      }, {
          "type": "bar",
          "data": data_result["data"][6],
          "coordinateSystem": "polar",
          "name": ">10(m/s)",
          "stack": "a"
      }]
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