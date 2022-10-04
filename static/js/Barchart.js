$(document).ready(function () {
    $.get('http://127.0.0.1:50003/rainfall_BarChart/?station=231824A', function (data) {
        let value_r = [];
        for (let key in data["data"]) {
            value_r.push(data["data"][key]);
        }
        barchart(value_r, "container3", "Rainfall Chart", "mm", data["start_t"], data["end_t"])
    })
    $.get('http://127.0.0.1:50003/humidity_BarChart/?station=231824A', function (data) {
        let value_h = [];
        for (let key in data["data"]) {
            value_h.push(data["data"][key]);
        }
        barchart(value_h, "container4", "Humidity Chart", "%", data["start_t"], data["end_t"])
    })
})

function barchart(r_data, id, name, scale, start_t, end_t) {
    var BarChart = echarts.init(document.getElementById(id));
    option = {
        title: {
            text: name,
            subtext: "from " + start_t + " to " + end_t ,
            left: 'left',
            top: 10
        },
        grid: {
            top: '25%'
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
                itemStyle: {
							normal: {
								label: {
									show: true,
									position: 'top',
									textStyle: {
										color: 'black',
										fontSize: 16
									},
									formatter: (params) => {
                                        return params.value.toFixed(2);
                                    },
								}
							}
				},
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


function create_url(start_time, end_time, station, interface_url){
    var condition_dict = new Array()
    var condition_str = ""

    if ((start_time && end_time) && (end_time >= start_time)){
        condition_dict["start_time"] = start_time
        condition_dict["end_time"] = end_time
    }
    condition_dict["station"] = station
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
    var station_select = document.getElementById("chart3_station");
    var station_str = station_select.options[station_select.selectedIndex].value;
    console.log(station_str)


   query_url = create_url(start_time, end_time, station_str,"rainfall_BarChart")

    $.get(query_url,function(data,status){
        let value_r = [];
        for (let key in data["data"]) {
            value_r.push(data["data"][key]);
        }
//        barchart(value_r, "container3", "Rainfall Chart", "mm")
        barchart(value_r, "container3", "Rainfall Chart", "mm", data["start_t"], data["end_t"])
    });

}

function chart4_time_range(){
    var start_time = document.getElementById("chart4_start_time").value;
    var end_time = document.getElementById("chart4_end_time").value;
    var station_select = document.getElementById("chart4_station");
    var station_str = station_select.options[station_select.selectedIndex].value;
    console.log(station_str)
    query_url = create_url(start_time, end_time, station_str, "humidity_BarChart")

    $.get(query_url,function(data,status){
        let value_h = [];
        for (let key in data["data"]) {
            value_h.push(data["data"][key]);
        }
//        barchart(value_h, "container4", "Humidity Chart", "%")
        barchart(value_h, "container4", "Humidity Chart", "%", data["start_t"], data["end_t"])
    });
}
