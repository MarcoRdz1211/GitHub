#include "colors.inc"
#fopen MyFile "cubo_prime2.txt" read
                     
background{color White}

camera {location <-10, 5, -10> look_at <0, 0, 0>}
                       
#declare Re=0.2; 
#declare Mystring= "Au";
#declare i=0;  

#declare atoms=union{
                     #while (i<16)
                         #read (MyFile,Mystring,x0,y0,z0)        
                         sphere {<x0,y0,z0>, Re}   
                     #declare i=i+1;
                     #end      
                     texture{pigment{color Blue}finish{phong 1}}
                    }   

object{atoms rotate <0,10,10>}