var dom1 = document.getElementById('container1');
var myChart1 = echarts.init(dom1, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var dom2 = document.getElementById('container2');
var myChart2 = echarts.init(dom2, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var dom5 = document.getElementById('container5');
var myChart5 = echarts.init(dom5, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var dom6 = document.getElementById('container6');
var myChart6 = echarts.init(dom6, null, {
  renderer: 'canvas',
  useDirtyRect: false
});

var option1;
var option2;
var option5;
var option6;

function create_chart(option, myChart, name, data_result, scale, ytitle){
    option = {
        tooltip: {
            trigger: 'axis',
            position: function (pt) {
            return [pt[0], '10%'];
            }
        },
        legend: {
            data: ["231824A", "231825A", "231826A", "231827A", "231828A"]
        },
        title: {
            left: 'left',
            text: name
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
        xAxis: {
            name: 'time',
            type: 'time',
            interval: 100,
            boundaryGap: false,
        },
        yAxis: {
            name: ytitle,
            type: 'value',
            boundaryGap: [0, '100%'],
            axisLabel: {formatter: '{value}'+scale},
            axisLine: {
                show: true,
                lineStyle:{
                    color:'black',
                    width:2
                }
            },
        },
        dataZoom: [
            {
                type: 'inside',
                start: 0,
                end: 20
            },
            {
                start: 0,
                end: 20
            }
        ],
        series: [
            {
                name: '231824A',
                type: 'line',
                symbol: 'none',
                data: data_result["station1"]
            },
            {
                name: '231825A',
                type: 'line',
                symbol: 'none',
                data: data_result["station2"]
            },
            {
                name: '231826A',
                type: 'line',
                symbol: 'none',
                data: data_result["station3"]
            },
            {
                name: '231827A',
                type: 'line',
                symbol: 'none',
                data: data_result["station4"]
            },
            {
                name: '231828A',
                type: 'line',
                symbol: 'none',
                data: data_result["station5"]
            }
        ]
    };

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
    window.addEventListener('resize', myChart.resize);
}

$(document).ready(function(){
    $.get("http://127.0.0.1:50003/temperaturelinechart/",function(data_result,status){
        create_chart(option1, myChart1, "Temperature Chart", data_result, "℃", "temperature")
    });

    $.get("http://127.0.0.1:50003/windspeedlinechart/",function(data_result,status){
        create_chart(option2, myChart2, "Wind Speed Chart", data_result, "ms^-1", "wind speed")
    });

    $.get("http://127.0.0.1:50003/pressurelinechart/",function(data_result,status){
        create_chart(option5, myChart5, "Pressure Chart", data_result, "hPa", "pressure")
    });

    $.get("http://127.0.0.1:50003/solarradiationlinechart/",function(data_result,status){
        create_chart(option6, myChart6, "Solar Radiation Chart", data_result, "W m^-2", "solar radiation")
    });
});

function create_url(start_time, end_time, interface_url){
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

function chart1_time_range(){
    var start_time = document.getElementById("chart1_start_time").value;
    var end_time = document.getElementById("chart1_end_time").value;
    console.log(start_time, end_time)

   query_url = create_url(start_time, end_time, "temperaturelinechart")

    $.get(query_url,function(data_result,status){
        create_chart(option1, myChart1, "Temperature Chart", data_result, "℃")
    });

}

function chart2_time_range(){
    var start_time = document.getElementById("chart2_start_time").value;
    var end_time = document.getElementById("chart2_end_time").value;
    console.log(start_time, end_time)
    query_url = create_url(start_time, end_time, "windspeedlinechart")

    $.get(query_url,function(data_result,status){
        create_chart(option2, myChart2, "Wind Speed Chart", data_result, "ms^-1")
    });

}

function chart5_time_range(){
    var start_time = document.getElementById("chart5_start_time").value;
    var end_time = document.getElementById("chart5_end_time").value;
    console.log(start_time, end_time)
    query_url = create_url(start_time, end_time, "pressurelinechart")

    $.get(query_url,function(data_result,status){
        create_chart(option5, myChart5, "Pressure Chart", data_result, "hPa")
    });

}

function chart6_time_range(){
    var start_time = document.getElementById("chart6_start_time").value;
    var end_time = document.getElementById("chart6_end_time").value;
    console.log(start_time, end_time)
    query_url = create_url(start_time, end_time, "solarradiationlinechart")

    $.get(query_url,function(data_result,status){
        create_chart(option6, myChart6, "Solar Radiation Chart", data_result, "W m^-2")
    });
}