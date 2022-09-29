$(document).ready(function () {
    $.get('http://127.0.0.1:50003/rainfall_BarChart/', function (data) {
        let value_r = [];
        for (let key in data) {
            value_r.unshift(data[key]);
        }
        barchart(value_r, "container3", "Rainfall Chart", "mm")
    })
    $.get('http://127.0.0.1:50003/humidity_BarChart/', function (data) {
        let value_h = [];
        for (let key in data) {
            value_h.unshift(data[key]);
        }
        barchart(value_h, "container4", "Humidity Chart", "%")
    })
})

function barchart(r_data, id, name, scale) {
    var BarChart = echarts.init(document.getElementById(id));
    option = {
        title: {
            text: name,
            left: 'center',
            top: 10
        },
        xAxis: {
            name: 'each day',
            type: 'category'
        },
        yAxis: {
            name: 'total',
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
        series: [
            {
                data: r_data,
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(180, 180, 180, 0.2)'
                }
            }
        ]
    };

    BarChart.setOption(option)
}


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


function chart3_time_range(){
    var start_time = document.getElementById("chart3_start_time").value;
    var end_time = document.getElementById("chart3_end_time").value;
    console.log(start_time, end_time)

   query_url = create_url(start_time, end_time, "rainfall_BarChart")

    $.get(query_url,function(data,status){
        let value_r = [];
        for (let key in data) {
            value_r.unshift(data[key]);
        }
        barchart(value_r, "container3", "Rainfall Chart")
    });

}

function chart4_time_range(){
    var start_time = document.getElementById("chart4_start_time").value;
    var end_time = document.getElementById("chart4_end_time").value;
    console.log(start_time, end_time)
    query_url = create_url(start_time, end_time, "humidity_BarChart")

    $.get(query_url,function(data,status){
        let value_h = [];
        for (let key in data) {
            value_h.unshift(data[key]);
        }
        barchart(value_h, "container4", "Humidity Chart")
    });
}