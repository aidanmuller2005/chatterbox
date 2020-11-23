window.onload=function () {
    
    var creatorlocation = document.getElementById('creatorurl').innerHTML;
     
     document.getElementById('posttitle').innerHTML = document.getElementById('titlevar').innerHTML;
    
    // Post title hover
     
     document.getElementById('posttitle').onmouseover = function() {
         
         document.body.style.cursor='pointer';
         document.getElementById('posttitle').innerHTML = document.getElementById('creatorvar').innerHTML;
         document.getElementById('posttitle').style.color = 'blue';
         document.getElementById('posttitle').onclick = function() { window.location.href=creatorlocation; }
         
     }
     
     document.getElementById('posttitle').onmouseout = function() {
         
         document.body.style.cursor='default';
         document.getElementById('posttitle').innerHTML = document.getElementById('titlevar').innerHTML;
         document.getElementById('posttitle').style.color = 'black';
         
     }
    
     
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