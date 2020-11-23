function rotatebtn() {
    
    var composebtn = document.getElementById('composebtn');
    composebtn.style = "transform:rotate(360deg)";
    setTimeout(function(){
        
        composebtn.style = "transform:rotate(0deg)";
        document.getElementById("composebox").style.visibility="visible";
                         
                         
                         
                         }, 500);
    
    
    
}

function sendMsg() {
    
    var personto = document.getElementById("personto").value;
    var msg = document.getElementById("messagecontent").value;
    window.location.href='http://79.97.52.85/action?=dm&to?=' + personto + '&msg?=' + msg + '/';
    
    
}