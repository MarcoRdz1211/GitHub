//---------------------------------------//
// DISEÑO DE ESCENA: CÁMARA, LUZ Y PLANO //
//---------------------------------------//

#include "colors.inc" //Libreria de colores

background {color Red} //Color del fondo
	
camera {                     // Definimos la Cámara...
  location <10, 10, -50>  // Lugar desde donde "mira" la cámara.
  look_at <0, 0, 0>    // Punto al que la cámara está "mirando".  
}


#declare radio=1.5 ;
#declare radio1=1 ;


// Definiendo una molécula
sphere {<0,3,0> radio pigment {color Green}
            }

sphere {<3,3,0> radio pigment {color Green}
            }

sphere {<0,10,0> radio pigment {color Green}
            }

cylinder {<0,3,0>, <3,3,0> radio1 
 pigment {color Orange}
             }

cylinder {<3,3,0>, <0,10,0> radio1
 pigment {color Orange}  
            }

cylinder {<0,3,0>, <0,10,0> radio1
 pigment {color Orange}  
            }

// Luz
light_source {          //Definimos un foco de luz...
  <0, 100, -100>        //Colocamos luz arriba y hacia atrás
  rgb 1.75              //Color RGB (Red, Green, Blue) puesto a 1.75 (blanco brillante)
  
  parallel              //Indicamos que es LUZ PARALELA
  point_at <0, 0, 0>    //Indicamos a dónde apunta la fuente de luz paralela
}


plane { y, 0            //Colocamos un objeto (un plano)
  pigment {
    checker <0,1,0>, <0,0,1>
  }
}

