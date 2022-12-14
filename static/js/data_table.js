var current_page = 1
var total_count = -1
var pre_page_url = ""
var next_page_url = ""
var condition_dict = new Array()
var condition_str = ""
var download_query_url = ""

//create table
$(document).ready(function(){
    current_page = 1
    $.get("http://127.0.0.1:50003/datatable/?page=1",function(data_result,status){
        console.log("run")
        temp_data = data_result["results"]
        total_count = data_result["count"]
        pre_page_url = data_result["previous"]
        next_page_url = data_result["next"]

        var data_tbody = document.getElementById("data_tbody")
        for (var i = 0; i < temp_data.length; i++) {
            var temp_tr = document.createElement("tr");
            temp_tr. innerHTML = '<td>' + temp_data[i]["id"] + '</td>'
                                + '<td>' + temp_data[i]["sensor_datetime"] + '</td>'
                                + '<td>' + temp_data[i]["rainfall"] + '</td>'
                                + '<td>' + temp_data[i]["temperature"] + '</td>'
                                + '<td>' + temp_data[i]["humidity"] + '</td>'
                                + '<td>' + temp_data[i]["wind_direction"] + '</td>'
                                + '<td>' + temp_data[i]["wind_speed"] + '</td>'
                                + '<td>' + temp_data[i]["pressure"] + '</td>'
                                + '<td>' + temp_data[i]["solar_radiation"] + '</td>'
                                + '<td>' + temp_data[i]["station"] + '</td>';
            data_tbody.appendChild(temp_tr)
        }
    });
});

// pre page
function pre_page(){
    if (current_page >1 ){
        current_page = current_page - 1
        $.get(pre_page_url,function(data_result,status){
            console.log(current_page)
            temp_data = data_result["results"]
            pre_page_url = data_result["previous"]
            next_page_url = data_result["next"]


            var data_tbody = document.getElementById("data_tbody")
            $("#data_tbody").empty()
            for (var i = 0; i < temp_data.length; i++) {
                var temp_tr = document.createElement("tr");
                temp_tr. innerHTML = '<td>' + temp_data[i]["id"] + '</td>'
                                    + '<td>' + temp_data[i]["sensor_datetime"] + '</td>'
                                    + '<td>' + temp_data[i]["rainfall"] + '</td>'
                                    + '<td>' + temp_data[i]["temperature"] + '</td>'
                                    + '<td>' + temp_data[i]["humidity"] + '</td>'
                                    + '<td>' + temp_data[i]["wind_direction"] + '</td>'
                                    + '<td>' + temp_data[i]["wind_speed"] + '</td>'
                                    + '<td>' + temp_data[i]["pressure"] + '</td>'
                                    + '<td>' + temp_data[i]["solar_radiation"] + '</td>'
                                    + '<td>' + temp_data[i]["station"] + '</td>';
                data_tbody.appendChild(temp_tr)
            }
        });
    }
}

//next page
function next_page(){
    if (next_page_url){
        current_page = current_page + 1
        $.get(next_page_url,function(data_result,status){
            temp_data = data_result["results"]
            console.log(current_page)
            pre_page_url = data_result["previous"]
            next_page_url = data_result["next"]
            var data_tbody = document.getElementById("data_tbody")
            $("#data_tbody").empty()
            for (var i = 0; i < temp_data.length; i++) {
                var temp_tr = document.createElement("tr");
                temp_tr. innerHTML = '<td>' + temp_data[i]["id"] + '</td>'
                                    + '<td>' + temp_data[i]["sensor_datetime"] + '</td>'
                                    + '<td>' + temp_data[i]["rainfall"] + '</td>'
                                    + '<td>' + temp_data[i]["temperature"] + '</td>'
                                    + '<td>' + temp_data[i]["humidity"] + '</td>'
                                    + '<td>' + temp_data[i]["wind_direction"] + '</td>'
                                    + '<td>' + temp_data[i]["wind_speed"] + '</td>'
                                    + '<td>' + temp_data[i]["pressure"] + '</td>'
                                    + '<td>' + temp_data[i]["solar_radiation"] + '</td>'
                                    + '<td>' + temp_data[i]["station"] + '</td>';
                data_tbody.appendChild(temp_tr)
            }
        });
    }
}

//data query
function query_data(){
    var query_id = document.getElementById("query_id").value;
    var query_station = document.getElementById("query_station").value;
    var start_time = document.getElementById("start_time").value;
    var end_time = document.getElementById("end_time").value;
//    console.log(start_time, end_time)
    condition_dict = new Array()
    condition_str = ""
    if (query_id){
        condition_dict["id"] = query_id
    }
    if (query_station){
        condition_dict["station"] = query_station
    }
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
        var query_url = "http://127.0.0.1:50003/datatable/?page=1&" + condition_str
    }else{
        var query_url = "http://127.0.0.1:50003/datatable/?page=1" + condition_str
    }

    $.get(query_url,function(data_result,status){
        console.log("run")
        temp_data = data_result["results"]
        total_count = data_result["count"]
        pre_page_url = data_result["previous"]
        console.log(pre_page_url)
        next_page_url = data_result["next"]
        console.log(next_page_url)
        console.log(temp_data.length)
        var data_tbody = document.getElementById("data_tbody")
        $("#data_tbody").empty()
        for (var i = 0; i < temp_data.length; i++) {
            var temp_tr = document.createElement("tr");
            temp_tr. innerHTML = '<td>' + temp_data[i]["id"] + '</td>'
                                + '<td>' + temp_data[i]["sensor_datetime"] + '</td>'
                                + '<td>' + temp_data[i]["rainfall"] + '</td>'
                                + '<td>' + temp_data[i]["temperature"] + '</td>'
                                + '<td>' + temp_data[i]["humidity"] + '</td>'
                                + '<td>' + temp_data[i]["wind_direction"] + '</td>'
                                + '<td>' + temp_data[i]["wind_speed"] + '</td>'
                                + '<td>' + temp_data[i]["pressure"] + '</td>'
                                + '<td>' + temp_data[i]["solar_radiation"] + '</td>'
                                + '<td>' + temp_data[i]["station"] + '</td>';
            data_tbody.appendChild(temp_tr)
        }
    });

}

//data download
function download_data(){
    console.log(condition_str)
    download_query_url = "http://127.0.0.1:50003/download/?" + condition_str
//    $.get(download_query_url,function(data_result,status){
//        const aLink = document.createElement('a')
//        aLink.href = download_query_url
//        aLink.setAttribute('download', "test" )
//        document.body.appendChild(aLink)
//        aLink.click()
//        document.body.removeChild(aLink);
//    });
    const aLink = document.createElement('a')
    aLink.href = download_query_url
    aLink.setAttribute('download', "test" )
    document.body.appendChild(aLink)
    aLink.click()
    document.body.removeChild(aLink);
}