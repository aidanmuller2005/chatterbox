window.onload = function() {
var box = document.getElementById('messagecontent');
box.focus();
    
    
    
}
function openInput() {
var box = document.getElementById('messagecontent');
var sendbtn = document.getElementById('sendmsgbtn');
    box.style.width="570px";
    box.style.left="47.5%";
    box.style.textAlign="left";
    sendbtn.style.right="27%";
    
    
    
}


function sendDM() {
var msgcontent = document.getElementById('messagecontent').value;
var namelink = document.getElementById('namelink').innerHTML;

if(msgcontent != '') {    
window.location.href='http://79.97.52.85/action?=dm&to?=' + namelink + '&msg?=' + msgcontent +'/';
}
 
    else {
        
        alert("Please do not leave the message box empty");
        
    }
    
}