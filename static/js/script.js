const normalBackgroundColor = "#182344";
const activeBackgroundColor = "#53baff";

const navbarItems = [
    "Data Report",
    "Data Center",
    "Sharing",
]

const changeElementBackgroundColor = (elementId, color) => {
    document.getElementById(elementId).style.backgroundColor = color;
}

const switchToNavbarItem = (navItem) => {
    navbarItems.forEach((item) => {
        item === navItem ? changeElementBackgroundColor(item, activeBackgroundColor) :
            changeElementBackgroundColor(item, normalBackgroundColor);
    })

    /* Handle any backend loading here */
}

function displayChart(tp){
    var url;
    if (tp == 'histogramC'){
        url = "fold_bar_chart.html";
    }else if (tp == 'foldLineChart'){
        url = "fold_line_chart.html";
    }else if (tp == 'pie_chart'){
        url = "fold_line_chart.html";
    }else{
        url = "fold_line_chart.html";
    }
    $.ajax({   
        url: url,
        data:'{}',
        type: 'post',
        dataType: 'text',
        contentType: 'application/json; charset=utf-8',
        success: function (data){                           
            if (data) {
                var char_v=$(data).find("container");
                $("#display_chart").html(char_v);                             
            }
        }
    });

}