
#include "colors.inc"

#version 3.6;
global_settings {  assumed_gamma 1.0 }

/*
//Para ver como un Sistema derecho
camera {  //  Camera StdCam
  location  <0.000, 5.000, 0>
  direction <0.0,     0.0,  1.9067>
  sky       <0.0,     0.0,  1.0>  // Z esta arriba
  up        <0.0,     0.0,  1.0>  // 
  right     <1.33333, 0.0,  0.0>
  look_at   <0.000, 0.000, 0.000>
} 
*/



// La camara que muestra como es el sistema de coordenadas en Pov-Ray
#declare Camera_0 = camera {
			  angle    35
			  location -5*x
		    right    x*image_width/image_height
		    look_at  <0 , 0, 0>}


#declare Camera_1 = camera {
			  angle    35
			  location -2*z
 right    x*image_width/image_height
		    look_at  <0 , 0, 0>}


#declare Camera_2 = camera {/*ultra_wide_angle*/ angle 90 // right side view
                            location  <3.0 , 1.0 , 0.0>
                            right     x*image_width/image_height
                            look_at   <0.0 , 0.0 , 0.0>}

#declare Camera_3 = camera {/*ultra_wide_angle*/ angle 10        // top view
                            location  <0.0 , 3.0 ,-2.>
                            right     x*image_width/image_height
                            look_at   <0.0 , 0.0 , 0.0>}

//Mantiene una linea recta sin deformarla
#declare Camera_4 =camera{ // perspective //optional
        location < 0.00, 3, -3.00>
        look_at  < 0.00, 0,  0>
        right x*image_width/image_height
        angle  50} 

//Esta curva una linea recta
#declare Camera_5 =camera{ ultra_wide_angle angle 120 //cambiar el angulo para ver efecto
        location < 0.00, 3, -3.00>
        look_at  < 0.00, 0,  0>
        right x*image_width/image_height} 

// Camara ortografica. Paralelas permanecen paralelas y objetos del mismo tamaño
#declare Camera_6 =
camera{ orthographic angle  33
        location < 0.00, 3,-3.00>
        look_at  < 0.00, 0,  0>
        right x*image_width/image_height} 

//ortografica isometrica
#declare Camera_7 =
camera{ orthographic angle 50
        location < 3,3,-5>
        look_at  <  0.00, 1,  0.00>
        right x*image_width/image_height} 

//camara cilindrica
#declare Camera_8 =
camera{ cylinder 1 angle 180
        location < 0.00,0, -2.00>
        look_at  <  0.00,0,0>      
        right 1.33
        up  1
      } 

//camara esferica
#declare Camera_9 =
camera{ spherical
        angle 358  // horizontal
              180  // vertical(optional)
        location <  0.00, 0.00, -2>
        look_at  <  0.00, 0,0>
        right  x*image_width/image_height
      } 

//camara esferica
#declare Camera_10=

camera{ fisheye
        angle 180 // horizontal
        location < 0.00,0.00,-2>
        look_at  <  0.00, 0,  0>
        right  x*image_width/image_height
      } 

//camara blur
#declare Camera_11=
camera{ angle 40
        location < 0.00,2.00,-3.00>
        look_at  < 0.00,0, 0>
        right  x*image_width/image_height      
     // focal blur settings:
        focal_point <0.20,1.5,-5.25>
        aperture 0.7     // 0.05 ~ 1.5
        blur_samples 100 // 4 ~ 100
        confidence 0.9   // 0 ~ 1
        variance 1/128   // 1/64 ~ 1/1024 ~
      } 

//camara perturbada
#declare Camera_12=
camera{ angle 40
        location < 0.00,2.00,-3.00>
        look_at  < 0.00,0.00, 0>
        right  x*image_width/image_height      
        normal{ bumps 0.15
                scale 0.4 translate<-0.2,0,0>}
      } 


//camara perturbada 2
#declare Camera_13=
camera{ angle 40
        location < 0.00,2.00,-3.00>
        look_at  < 0.00,0, 0>
        right  x*image_width/image_height      
        normal{ cells 0.15 turbulence 0.2
                scale 0.3 translate<-0.0,0,0>}
      } 

                                                   

//  AQUI SE ELIGE EL TIPO DE CAMARA (1-13) QUE SE USA EN LA ESCENA
camera{Camera_13}


//*****************************************************************
background { color Blue}

//---------------------------------------
light_source{ <1500,2500,-2500>  // La luz esta apuntando de la pantalla hacia atras de la pantalla
              color rgb<1,1,1> }
//---------------------------------------

sphere{ <0,0,0>, 0.15   texture { pigment{ color Green }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera

sphere{ <1.5,0,0>, 0.15   texture { pigment{ color Red }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera


sphere{ <-1.5,0,0>, 0.15   texture { pigment{ color Yellow }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera

sphere{ <-0.75,0,0>, 0.15   texture { pigment{ color Cyan}
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera

sphere{ <0.75,0,0>, 0.15   texture { pigment{ color White }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera


sphere{ <2.75,0,0>, 0.15   texture { pigment{ color Pink }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera

sphere{ <-2.75,0,0>, 0.15   texture { pigment{ color Blue*1.3 }
                  finish { diffuse 0.9
                           phong 1}
                } // Fin de la textura

       } // Fin de la esfera
//*******************************************************
cylinder {
  <3,  0, 0>,        //Primer "tapa" del cilindro.
  <-3, 0, 0>,        //Segunda "tapa" del cilindro.
  1                 //Radio del cilindro.

  pigment {         
    rgb <0.5, 0.75, 1>   //color AZUL.
  }

  translate y*3  translate z*0  translate x*0  //Apoyamos el cilindro en el suelo.
scale 0.5}


/*plane { y, -4            //Colocamos un objeto (un plano)
  pigment {
    checker rgb 1, rgb 0.75
  }
}*/