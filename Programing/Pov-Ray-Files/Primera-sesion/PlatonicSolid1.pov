#include "colors.inc"
#include "Math.inc"
                              
background{rgb <1,1,1>}

#fopen outFile "Hexaedro.txt" write

camera {location <-2, 0, -7.5> look_at <0, 0, 0>}

#declare radioedge=0.1;
#declare radiounion=0.05;
#declare edgecolor=rgb <0,1,0>;
#declare unioncolor=rgb <0.5,0.2,0.5>;
#declare centercolor=rgb <0.5,0,1>;
#declare a=1;
#declare Pos=array[8];
#declare Pos[0]=<a/2,a/2,a/2>;
#declare Pos[1]=<a/2,a/2,-a/2>;
#declare Pos[2]=<a/2,-a/2,a/2>;
#declare Pos[3]=<-a/2,a/2,a/2>;
#declare Pos[4]=<a/2,-a/2,-a/2>;
#declare Pos[5]=<-a/2,a/2,-a/2>;
#declare Pos[6]=<-a/2,-a/2,a/2>;
#declare Pos[7]=<-a/2,-a/2,-a/2>;

#declare MidPos=array[6];
#declare num=0;

#for(i,0,7)
    #for(j,0,7)
       #declare d=VDist(Pos[i],Pos[j]);  
       
       #if(d=a*sqrt(2) & d in MidPos)
          #declare MidPos[num]=(Pos[i]+Pos[j])/2;
          #declare num = num+1;      
       #end
    #end
#end
#declare hexaedro = union{
                           #for(i,0,7)
                               sphere{Pos[i],radioedge pigment{color edgecolor}}
                           #end
                             
                           #for(i,0,7)
                               #for(j,0,7)
                                   #declare d=VDist(Pos[i],Pos[j]); 
                                   #if(d=a)
                                        cylinder{Pos[i],Pos[j],0.05 texture{pigment{color unioncolor}} finish{phong 1}}   
                                   #end
                               #end
                           #end
                           }

#declare hexaedro1 = union{
                           #for(i,0,7)
                               sphere{Pos[i],radioedge pigment{color edgecolor}}
                           #end
                             
                           #for(i,0,7)
                               #for(j,0,7)
                                    #if(i != j)
                                        cylinder{Pos[i],Pos[j],0.05} 
                                   #end
                               #end
                           #end
                           }

#declare hexaedro2 = union{
                           #for(i,0,7)
                               sphere{Pos[i],radioedge pigment{color edgecolor}}
                           #end
                             
                           #for(i,0,7)
                               #for(j,0,7)
                                    #if(i != j)
                                        cylinder{Pos[i],Pos[j],0.05} 
                                   #end
                               #end
                           #end
                           }

#declare hexaedro3 = union{#for(i,0,5)
                                sphere{MidPos[i],radioedge pigment{color centercolor}}
                           #end
                          }

object{hexaedro3}