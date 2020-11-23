 window.onload=function() {
    
    
     
 
        
        
        
    
    
    
    
    
    
    
    
    // Dropdown hover


var trn = document.getElementById('toprightname');
            
            trn.onmouseover = function() {
                
                document.getElementById('dropdowncontent').style.visibility = 'visible';
                
            }
                
            trn.onmouseout = function() {
                
                document.getElementById('dropdowncontent').style.visibility="hidden";
                
            }
                
            
            // Keep Visible
            
             document.getElementById('dropdowncontent').onmouseover = function() {
                
                document.getElementById('dropdowncontent').style.visibility="visible";
            }
                
            document.getElementById('dropdowncontent').onmouseout = function() {
                
                document.getElementById('dropdowncontent').style.visibility="hidden";
            }
               
            
            
               }