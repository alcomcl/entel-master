$(document).ready(function(){

    //Reloj

    setInterval(function(){// usamos setInterval para que el reloj se actualize cada 1 segundo
        var reloj = moment().format("hh:mm:ss");
        $("#reloj").html(reloj+' hrs.');
    }, 1000);

    //Slider
    if(window.location.href.indexOf('base') > -1){
      
        $('.galeria').bxSlider({
            mode: 'fade',
            captions: true,
            pager: true,
            slideWidth: 700,
            responsive: true
        });
    }







});