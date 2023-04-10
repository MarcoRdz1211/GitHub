#include "colors.inc"
#fopen MyFile "NewCube.txt" read    //Archivo de entrada
                     
background{color White}

camera {location <-2, 0, -7.5> look_at <0, 0, 0>}
                     
#declare Re=0.2; 
#declare Mystring= "H";  

#declare atoms=union{
                     #while (defined(MyFile))
                         #read (MyFile,Mystring,Vector)        
                         sphere {Vector,    Re}   
                     #end      
                     texture{pigment{color Red}finish{phong 1}}
                    }   

object{atoms}