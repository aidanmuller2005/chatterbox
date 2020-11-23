function submitForm(){
    
    // http://79.97.52.85/action?=create&name?=' + un + '&password?=' + np + '/
    var un = document.getElementById('un').value;
    var np = document.getElementById('np').value;
    var cp = document.getElementById('cp').value;
    
    
    
   if (un != '') {
       
       
       if (np != '') {
           
           
           if (cp != '') {
               
               if (np == cp) {

                   if (un.indexOf("=") > -1) {

                       alert("Please do not include the following characters in your username: '='");
                       

                   }

                   else {

                       window.location.href = 'http://79.97.52.85/action?=create&name?=' + un + '&password?=' + np + '/';

                       

                   }
                   
               }
               
               
               else {
        
        alert("Passwords do not match!")
        
    }
               
               
           }
           
           else {
        
        alert("Please do not leave any fields blank!")
        
    }
           
           
           
       }
       
       else {
        
        alert("Please do not leave any fields blank!")
        
    }
       
   }
    
    else {
        
        alert("Please do not leave any fields blank!")
        
    }
    
    
}
