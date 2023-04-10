
#include "colors.inc"

#version 3.6;
global_settings {  assumed_gamma 1.0 }


// La camara ----------
camera {
  angle    45
  location <12,8,0>

/* Probar estas otras vistas
location -2*z
location 5*z
location 2*x
*/


  right    x*image_width/image_height
  look_at  <0 , 0, 0>

}



background { color Pink}


plane { y, -4            //Colocamos un objeto (un plano)
  pigment {
    checker rgb 1, rgb 0.75
  }
}

//---------------------------------------

sphere{ <0,0,0>, .5   texture { pigment{ color Green }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera


sphere{ <3,0,0>, .5   texture { pigment{ color Red }
                  finish { diffuse 0.9
                           phong 1}
                }} // Fin de la textura


sphere{ <-3,0,0>, .5   texture { pigment{ color Red }
                  finish { diffuse 0.9
                           phong 1}
                }} // Fin de la textura
//*************************************************************************
// Camaras

//Imita la luz del sol
#declare luz_0 = light_source{ <2000,2000,  -1000> color White}

//Imita la luz de una lampara
#declare luz_1 = light_source{ <0, 5, 0>  color rgb<1,1,1> } 

//Camara que no produce sombra
#declare luz_2 = light_source{ <2000,2000, -1000> color White
              shadowless }

//Luz conica
#declare luz_3 = light_source{ <0,5,0> color rgb <1,1,1>   
              spotlight
              point_at<0,0,0>
              radius 20  // hotspot
              tightness 100 //su rango debe ser de 1 a 100. 1=suave, 100=aguda
              falloff 60    //Circulo mas externo de la luz
             // translate< 1.3, 3, 0>
            }

//Imita un laser
#declare luz_4 = light_source{ <0,5,0> color rgb <1,1,1>
              cylinder
              point_at<0, 0, 0>
              radius 20
              tightness 100
              falloff 60
             // translate< 1.3, 3, 0 >
            } 

//Imita la luz solar
#declare luz_5 = light_source{ <0,5,0> color rgb <1,1,1>
              parallel
              point_at<1, 0, 0> 
            } 

//Luces locales (en este ejemplo genera 16 luces)
#declare luz_6 = light_source{ <0,0,0>
              color rgb<1,1,1>
              area_light
              <5, 0, 0> <0, 0, 5>
              4,4 // numbers in directions
              adaptive 0  // 0,1,2,3...
              jitter // random softening
              translate<10, 10,  0>
             }//---- end of area_light}


//Para hacer visible la fuente de luz
#declare luz_7 = light_source{<0,3,0> color White*0.7
        looks_like{
           sphere{ <0,0,0>,0.5
                   texture{
                    pigment{color Gold}
                    finish {ambient 0.9
                            diffuse 0.1
                            phong 1}
                   }}}}


// Haciendo que la luz disminuya desde la fuente
#declare luz_8 = light_source{ <3,3,01
              color White
              fade_distance 1.2
              fade_power 1 // 1,2,3, ...
 } 

//******Aqui se define la luz (0-7)

light_source{luz_1}

