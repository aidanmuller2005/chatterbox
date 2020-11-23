function submitPost() {
    
    var ptitle = document.getElementById('ptitle').value;
    var pcontent = document.getElementById('pcontent').value;
     
    
    
    if (ptitle != '') {
        
        
        if (pcontent != '') {
            
            
            
            if(pcontent.length <= 1362) {
                
                if(ptitle.length <= 74) { 
                
            window.location.href='http://79.97.52.85/action?=post&title?=' + ptitle + '&content?=' + pcontent + '/';
                    
                }
                
                else {
                    
                    
                    alert("Your post's content contains too many characters! Maximum is 74");
                    
                }
            
            }
            
            else {
                
                alert("Your post's content contains too many characters! Maximum is 1362");
                
            }
            
            
        }
        
        
        else {
            
            
            alert('Please do not leave any fields empty!');
            
        }
        
        
        
    }
    
    else {
        
        
        
        alert('Please do not leave any fields empty!');
        
    }
        
        
        
    
    
    
}