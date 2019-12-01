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


    //Registrar el Service Worker
    if ('serviceWorker' in navigator && 'PushManager' in window) {
        console.log('Service Worker and Push is supported');
      
        navigator.serviceWorker.register('sw.js')
        .then(function(swReg) {
          console.log('Service Worker is registered', swReg);
      
          swRegistration = swReg;
        })
        .catch(function(error) {
          console.error('Service Worker Error', error);
        });
      } else {
        console.warn('Push messaging is not supported');
        pushButton.textContent = 'Push Not Supported';
      }




});