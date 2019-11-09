setTimeout(function(){
    $('#message').fadeOut(function(){
        $(this).remove();
    });
},3000);