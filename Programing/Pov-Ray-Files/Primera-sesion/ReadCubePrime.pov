#include "colors.inc"
#fopen MyFile "cubo_prime.txt" read
                     
background{color White}

camera {location <-10, 5, -10> look_at <0, 0, 0>}
                       
#declare Re=0.2; 
#declare Mystring= "Au";  

#declare atoms=union{
                     #while (defined(MyFile))
                         #read (MyFile,Mystring,Vector)        
                         sphere {Vector,    Re}   
                     #end      
                     texture{pigment{color Blue}finish{phong 1}}
                    }   

object{atoms rotate <0,10,10>}