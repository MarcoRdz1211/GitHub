#include "colors.inc"
                     
background{color White}

camera {location <-15, 10, -7.5> look_at <0, 0, 0>}
                                  
#fopen outFile "test_tetaedro.txt" write
      
#declare Re=0.2;
#declare a=3;
#declare r=5;
#declare i=0;
#declare j=0;
#declare k=0;  

#declare atoms=union{
                     #for (i,-r,r)     
                        #for (j,-r,r)
                            #for (k,-r,r)       
                                
                                #write(outFile,"<",i*a/r,",",j*a/r,",",k*a/r,">","\n")
                                sphere {<i*a/r,j*a/r,k*a/r> Re}
                            #end
                        #end
                     #end   
                        
                     texture{pigment{color Blue}finish{phong 1}}
                    }   

object{atoms}