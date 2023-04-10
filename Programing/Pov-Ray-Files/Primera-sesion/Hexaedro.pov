#include "colors.inc"
#include "Math.inc"
                              
background{rgb <1,1,1>}

#fopen outFile "Hexaedro.txt" write

camera {location <-2, 0, -7.5> look_at <0, 0, 0>}

#declare Pos=array[8];
#declare radioedge=0.1;
#declare radiounion=0.05;
#declare edgecolor=rgb <0,1,0>;
#declare unioncolor=rgb <0.5,0.5,0.5>;
#declare a=1;
#declare Pos[0]=<a,a,a>;
#declare Pos[1]=<a,a,-a>;
#declare Pos[2]=<a,-a,a>;
#declare Pos[3]=<-a,a,a>;
#declare Pos[4]=<a,-a,-a>;
#declare Pos[5]=<-a,a,-a>;
#declare Pos[6]=<-a,-a,a>;
#declare Pos[7]=<-a,-a,-a>;

#declare hexaedro = union{
                           #for(i,0,7)
                               sphere{Pos[i],radioedge pigment{color edgecolor}}
                           #end
                             
                           #for(i,0,7)
                               #for(j,0,7)
                                   #declare d=VDist(Pos[i],Pos[j]);
                                   #if(d<2*a*sqrt(2) & d!=0)
                                       cylinder{Pos[i],Pos[j],0.05 texture{pigment{color unioncolor}} finish{phong 1}}
                                       
                                   #end
                               #end
                           #end
                           }




object{hexaedro}
