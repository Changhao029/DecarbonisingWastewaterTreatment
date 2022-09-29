$(document).ready(function () {
    $.get('http://127.0.0.1:50003/barchart/', function (data) {
        console.log(data['0'])
        let value_r = [];
        let value_h = [];
        let rainfall = data[0]
        let humidity = data[1]
        for (let key in rainfall) {
            value_r.unshift(rainfall[key]);
        }
        for (let key in humidity) {
            value_h.unshift(humidity[key]);
        }
        console.log(value_r)
        console.log(value_h)
        barchart(value_r, "container3", "Rainfall")
        barchart(value_h, "container4", "Humidity")


    function barchart(r_data, id, name) {
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
                type: 'value'
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

    // function barchart(girth,id,name) {
    //     console.log(girth)
    //     var histogramChart = echarts.init(document.getElementById(id));
    //     var bins = ecStat.histogram(girth, 'freedmanDiaconis');
    //     var interval;
    //     var min = Infinity;
    //     var max = -Infinity;
    //     var data = echarts.util.map(bins.data, function (item, index) {
    //         var x0 = bins.bins[index].x0;
    //         var x1 = bins.bins[index].x1;
    //         interval = x1 - x0;
    //         min = Math.min(min, x0);
    //         max = Math.max(max, x1);
    //         return [x0, x1, item[1]];
    //     });
    //
    //     function renderItem(params, api) {
    //         var yValue = api.value(2);
    //         var start = api.coord([api.value(0), yValue]);
    //         var size = api.size([api.value(1) - api.value(0), yValue]);
    //         var style = api.style();
    //         return {
    //             type: 'rect',
    //             shape: {x: start[0] + 1, y: start[1], width: size[0] - 2, height: size[1]},
    //             style: style
    //         };
    //     }
    //
    //     option = {
    //         title: {
    //             text: name,
    //             left: 'center',
    //             top: 10
    //         },
    //         color: ['rgb(25, 183, 207)'],
    //         grid: {top: 80, containLabel: true},
    //         xAxis: [{type: 'value', min: min, max: max, interval: interval}],
    //         yAxis: [{type: 'value',}],
    //         series: [{
    //             name: 'height',
    //             type: 'custom',
    //             renderItem: renderItem,
    //             label: {show: true, position: 'insideTop'},
    //             encode: {x: [0, 1], y: 2, tooltip: 2, label: 2}, data: data
    //         }]
    //     };
    //     histogramChart.setOption(option)
    // }
})