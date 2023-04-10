
#include "colors.inc"
#include "textures.inc"
#include "metals.inc"

#version 3.6;
global_settings {  assumed_gamma 1.0 }


// La camara ----------
camera {
  angle    35
  location <12,8,0>

/* Probar estas otras vistas
location -2*z
location 5*z
location 2*x
*/


  right    x*image_width/image_height
  look_at  <0 , 0, 0>

}



background { color Blue}


plane { y, -4            //Colocamos un objeto (un plano)
  pigment {
    checker rgb 1, rgb 0.75
  }
}
//''''''''''''''''''''''''''''''''''''''''

 #declare t1 = texture{ pigment{ Jade }
          finish{ phong 1.0 }
        }


#declare t2 = texture{pigment{ color Green } finish { diffuse 0.9
                           phong 1}}

#declare t3= texture{ Gold_Nugget finish { phong 1.0 }}

#declare t4= texture{ pigment{ color Orange}
         normal { bumps 0.5 scale 0.05 }
         finish { phong 1.0 reflection{0.2} }
       }      

#declare t5= texture{Polished_Chrome   finish { phong 1.0 }}
    
//---------------------------------------

sphere{ <0,0,0>, 1   texture { t1}  translate z*2} // Fin de la textura

sphere{ <0,0,0>, 1   texture { t2} translate z*-2} // Fin de la textura
 

sphere{ <0,0,0>, 1   texture { t4} translate x*-3 scale 2} // Fin de la textura  

sphere{ <0,0,0>, 1   texture { t3} translate x*3} // Fin de la textura 

sphere{ <0,0,0>, 1   texture { t5} translate y*0} // Fin de la textura 

//*************************************************************************
// Haciendo que la luz disminuya desde la fuente
#declare luz_8 = light_source{ <3,3,0>
              color White
              fade_distance 1.2
              fade_power 2 // 1,2,3, ...
 } 

//******Aqui se define la luz

light_source{luz_8}

