$(document).ready(function(){
    $.get("http://127.0.0.1:50003/linechart/",function(data_result,status){
        
        
        // [data_result["temperature"]];
        // data.push(data_result["sensor_datetime"])
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
    
      
        // let data = [[new Date(data_result["sensor_datetime"][0]), data_result["temperature"][0], data_result["station_num"][0]]]
        let temperature_station1 = []
        let temperature_station2 = []
        let temperature_station3 = []
        let temperature_station4 = []
        let temperature_station5 = []

        let windspeed_station1 = []
        let windspeed_station2 = []
        let windspeed_station3 = []
        let windspeed_station4 = []
        let windspeed_station5 = []

        let pressure_station1 = []
        let pressure_station2 = []
        let pressure_station3 = []
        let pressure_station4 = []
        let pressure_station5 = []

        let solar_radiation_station1 = []
        let solar_radiation_station2 = []
        let solar_radiation_station3 = []
        let solar_radiation_station4 = []
        let solar_radiation_station5 = []
        // console.log(data[0])
        for (let i = 0; i < data_result["sensor_datetime"].length; i++) {
            if (data_result["station"][i] == "231824A"){
                temperature_station1.push([data_result["sensor_datetime"][i], data_result["temperature"][i],  data_result["station"][i]]);
                windspeed_station1.push([data_result["sensor_datetime"][i], data_result["wind_speed"][i],  data_result["station"][i]]);
                pressure_station1.push([data_result["sensor_datetime"][i], data_result["pressure"][i],  data_result["station"][i]]);
                solar_radiation_station1.push([data_result["sensor_datetime"][i], data_result["solar_radiation"][i],  data_result["station"][i]]);
            }else if(data_result["station"][i] == "231825A"){
                temperature_station2.push([data_result["sensor_datetime"][i], data_result["temperature"][i], data_result["station"][i]]);
                windspeed_station2.push([data_result["sensor_datetime"][i], data_result["wind_speed"][i],  data_result["station"][i]]);
                pressure_station2.push([data_result["sensor_datetime"][i], data_result["pressure"][i],  data_result["station"][i]]);
                solar_radiation_station2.push([data_result["sensor_datetime"][i], data_result["solar_radiation"][i],  data_result["station"][i]]);
            }else if(data_result["station"][i] == "231826A"){
                temperature_station3.push([data_result["sensor_datetime"][i], data_result["temperature"][i], data_result["station"][i]]);
                windspeed_station3.push([data_result["sensor_datetime"][i], data_result["wind_speed"][i],  data_result["station"][i]]);
                pressure_station3.push([data_result["sensor_datetime"][i], data_result["pressure"][i],  data_result["station"][i]]);
                solar_radiation_station3.push([data_result["sensor_datetime"][i], data_result["solar_radiation"][i],  data_result["station"][i]]);
            }else if(data_result["station"][i] == "231827A"){
                temperature_station4.push([data_result["sensor_datetime"][i], data_result["temperature"][i], data_result["station"][i]]);
                windspeed_station4.push([data_result["sensor_datetime"][i], data_result["wind_speed"][i],  data_result["station"][i]]);
                pressure_station4.push([data_result["sensor_datetime"][i], data_result["pressure"][i],  data_result["station"][i]]);
                solar_radiation_station4.push([data_result["sensor_datetime"][i], data_result["solar_radiation"][i],  data_result["station"][i]]);
            }else if(data_result["station"][i] == "231828A"){
                temperature_station5.push([data_result["sensor_datetime"][i], data_result["temperature"][i], data_result["station"][i]]);
                windspeed_station5.push([data_result["sensor_datetime"][i], data_result["wind_speed"][i],  data_result["station"][i]]);
                pressure_station5.push([data_result["sensor_datetime"][i], data_result["pressure"][i],  data_result["station"][i]]);
                solar_radiation_station5.push([data_result["sensor_datetime"][i], data_result["solar_radiation"][i], data_result["station"][i]]);
            }else{

            }
        }
        
        option1 = {
            tooltip: {
                trigger: 'axis',
                position: function (pt) {
                return [pt[0], '10%'];
                }
            },
            title: {
                left: 'center',
                text: 'Temperature Chart'
            },
            toolbox: {
                feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            interval: 100,
            boundaryGap: false,
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
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
                name: 'Station1',
                type: 'line',
                // smooth: true,
                symbol: 'none',
                // areaStyle: {},
                data: temperature_station1
            },
            {
                name: 'Station2',
                type: 'line',
                symbol: 'none',
                data: temperature_station2
            },
            {
                name: 'Station3',
                type: 'line',
                symbol: 'none',
                data: temperature_station3
            },
            {
                name: 'Station4',
                type: 'line',
                symbol: 'none',
                data: temperature_station4
            },
            {
                name: 'Station5',
                type: 'line',
                symbol: 'none',
                data: temperature_station5
            }
        ]
        };

        option2 = {
            tooltip: {
                trigger: 'axis',
                position: function (pt) {
                return [pt[0], '10%'];
                }
            },
            title: {
                left: 'center',
                text: 'Wind Speed Chart'
            },
            toolbox: {
                feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            interval: 100,
            boundaryGap: false,
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
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
                name: 'Station1',
                type: 'line',
                // smooth: true,
                symbol: 'none',
                // areaStyle: {},
                data: windspeed_station1
            },
            {
                name: 'Station2',
                type: 'line',
                symbol: 'none',
                data: windspeed_station2
            },
            {
                name: 'Station3',
                type: 'line',
                symbol: 'none',
                data: windspeed_station3
            },
            {
                name: 'Station4',
                type: 'line',
                symbol: 'none',
                data: windspeed_station4
            },
            {
                name: 'Station5',
                type: 'line',
                symbol: 'none',
                data: windspeed_station5
            }
        ]
        };


        option5 = {
            tooltip: {
                trigger: 'axis',
                position: function (pt) {
                return [pt[0], '10%'];
                }
            },
            title: {
                left: 'center',
                text: 'Pressure Chart'
            },
            toolbox: {
                feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            interval: 100,
            boundaryGap: false,
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
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
                name: 'Station1',
                type: 'line',
                // smooth: true,
                symbol: 'none',
                // areaStyle: {},
                data: pressure_station1
            },
            {
                name: 'Station2',
                type: 'line',
                symbol: 'none',
                data: pressure_station2
            },
            {
                name: 'Station3',
                type: 'line',
                symbol: 'none',
                data: pressure_station3
            },
            {
                name: 'Station4',
                type: 'line',
                symbol: 'none',
                data: pressure_station4
            },
            {
                name: 'Station5',
                type: 'line',
                symbol: 'none',
                data: pressure_station5
            }
        ]
        };

        option6 = {
            tooltip: {
                trigger: 'axis',
                position: function (pt) {
                return [pt[0], '10%'];
                }
            },
            title: {
                left: 'center',
                text: 'Solar Radiation Chart'
            },
            toolbox: {
                feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            interval: 100,
            boundaryGap: false,
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
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
                name: 'Station1',
                type: 'line',
                // smooth: true,
                symbol: 'none',
                // areaStyle: {},
                data: solar_radiation_station1
            },
            {
                name: 'Station2',
                type: 'line',
                symbol: 'none',
                data: solar_radiation_station2
            },
            {
                name: 'Station3',
                type: 'line',
                symbol: 'none',
                data: solar_radiation_station3
            },
            {
                name: 'Station4',
                type: 'line',
                symbol: 'none',
                data: solar_radiation_station4
            },
            {
                name: 'Station5',
                type: 'line',
                symbol: 'none',
                data: solar_radiation_station5
            }
        ]
        };


        
        if (option1 && typeof option1 === 'object') {
            myChart1.setOption(option1);
        } 

        if (option2 && typeof option2 === 'object') {
            myChart2.setOption(option2);
        } 

        if (option5 && typeof option5 === 'object') {
            myChart5.setOption(option5);
        } 

        if (option6 && typeof option6 === 'object') {
            myChart6.setOption(option6);
        } 

        window.addEventListener('resize', myChart1.resize);
        window.addEventListener('resize', myChart2.resize);
        window.addEventListener('resize', myChart5.resize);
        window.addEventListener('resize', myChart6.resize);
    });
});

