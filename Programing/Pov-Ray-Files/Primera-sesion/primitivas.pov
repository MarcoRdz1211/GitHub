
// Da la idea de como generar una escena en Pov-Ray
// Ademas de introducir al uso de objetos

// Alfredo Tlahuice Flores
// Dic 2010  
   

#include "colors.inc"

#declare camara=
camera {                //Definimos la Cámara...
  location <0, 10, -15> //Lugar desde donde "mira" la cámara.
  look_at <0, 0, 15>    //Punto al que la cámara está "mirando".  
}

#declare luz=
light_source {          //Definimos un foco de luz...
  <0, 100, -100>        //Colocamos luz arriba y hacia atrás
  rgb 1.75              //Color RGB (Red, Green, Blue) puesto a 1.75 (blanco brillante)
  
  parallel              //Indicamos que es LUZ PARALELA
  point_at <0, 0, 0>    //Indicamos a dónde apunta la fuente de luz paralela
}

// Create an infinite sphere around scene and allow any pigment on it
sky_sphere{ pigment { gradient <0,1,0>
                      color_map { [0.00 rgb <0.6,0.7,1.0>]
                                  [0.35 rgb <0.0,0.1,0.8>]
                                  [0.65 rgb <0.0,0.1,0.8>]
                                  [1.00 rgb <0.6,0.7,1.0>] 
                                } 
                      scale 2         
                    } // end of pigment
          } //end of skysphere -------------------------------------


#declare plano=
plane { y, 0            //Colocamos un objeto (un plano)
  pigment {
    checker rgb <1,0,0>, rgb <0,1,0>
  }
}

//---------------------------------------------------------------------------------
// Se definen los 5 tipos de primitivas que existen en PovRay

#declare esfera1=
// Agregamos una esfera
sphere {                //Invocamos una esfera...
  <0, 0, 0>,            //Centro de la esfera en coordenadas X=0, Y=0, Z=0
  1                     //Radio de la esfera: 1 UPV

  pigment {             //Definimos color.
    rgb <1, .5, 0>       //Damos color RGB 0 1 0 (verde)
  }
              
  translate x*5
}



#declare esfera2=
// Una esfera con color verde y transladada en direccion x
sphere {                //Invocamos una esfera...
  <0, 0, 0>,            //Centro de la esfera en coordenadas X=0, Y=0, Z=0
  1                     //Radio de la esfera: 1 UPV

  pigment {             //Definimos color.
    color Cyan       //Damos color RGB 0 1 0 (verde)
  }
translate x*2.5
}


// Esfera verde transladada en X y Y
#declare esfera3=
sphere {                //Invocamos una esfera...
  <1, .3, .5>,            //Centro de la esfera en coordenadas X=0, Y=0, Z=0
  1                     //Radio de la esfera: 1 UPV

  pigment {             //Definimos color.
    rgb <.3, 1, 1>       //Damos color RGB 0 1 0 (verde)
  }
translate <2.5,8.0,0>
}

// Definimos una caja
#declare caja=
box {                   //Invocamos una caja...
  <1, 1, 1>,            //Ubicación de la primer esquina.
  <-1, -1, -1>          //Ubicación de la esquina contraria.

  pigment {         
    rgb <1, 0, 0>   //color ROJO.
  }
  scale y*3
  translate <-2, 6, 0> rotate y*30
}


//definimos un cilindro
#declare cilindro=
cylinder {
  <0,  1, 0>,        //Primer "tapa" del cilindro.
  <0, -1, 0>,        //Segunda "tapa" del cilindro.
  1                 //Radio del cilindro.

  pigment {         
    rgb <0, 0, 1>   //color AZUL.
  }

  translate y*1  translate z*-2  translate x*-6  //Apoyamos el cilindro en el suelo.
}

//Definimos un cono
#declare cono=
cone {
  <0,  1, 0>,       //Primer "tapa" del cilindro.
  0,                //Radio de la primer "tapa".
  <0, -1, 0>,       //Segunda "tapa"del cilindro.
  2                 //Radio de la segunda "tapa".
  
  pigment {
    rgb <1, 0, 1>
  }    
  
  translate z*5 translate y*1  scale 2.0
}


//definimos un torus
#declare dona=
torus {
  1,                 //Radio del anillo.
  0.25               //Radio del grosor del anillo.

  pigment {
    rgb <1, 1.6, 0>
  }            
  
  translate y*0.25
}


//Hacemos una flecha
#declare flecha=
union{
   cylinder{0,1.5*x,0.2}      //vector unitario
   cone{1.5*x,1,2*x,0} 
 }

//******************************************************************
// Aqui definimos los elementos de la escena
plane{plano}
light_source{luz}
camera{camara}
sphere{esfera1}
  

cone{cono}
sphere{esfera1}
sphere{esfera2}
sphere{esfera3}
box{caja}
cylinder{cilindro}
torus{dona}
object{flecha pigment {rgb <0, 0, 1>}  translate y*5 translate x*5 rotate y*20}



