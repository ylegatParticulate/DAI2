$(document).ready(function() {

 $.get("/DjangoApp1/reclama_datos", function(datos){
         //   alert("Data: " + datos['0'] + "\nStatus: " );
visualiza_datos(datos);
        });



function visualiza_datos(datos){

$("#container").highcharts({       
      chart: {
            type: 'bar'
        },
        title: {
            text: 'Bars'
        },
        xAxis: {
            categories: datos['0']
        },
        yAxis: {
            title: {
                text: 'Visitors'
            }
        },
        series: [{
           name: 'Visitors',
           data: datos['1']
        }, {
            name: 'Likes',
            data: datos['2']
        }]
    });
};

$('#likes_bar').click(function(){
    var barid;
    barid = $(this).attr("data-barid");
    $.get('/DjangoApp1/like_bar/', {bar_slug: barid}, function(data){
               $('#like_count').html(data);
               $('#likes_bar').hide();
	});

});

$('#likes_tapas').click(function(){
    var tapid;
    tapid = $(this).attr("data-tapid");
    $.get('/DjangoApp1/like_tapas/', {tapas_slug: tapid}, function(data){
               $('#like_count').html(data);
               $('#likes_tapas').hide();
	});

});

});
