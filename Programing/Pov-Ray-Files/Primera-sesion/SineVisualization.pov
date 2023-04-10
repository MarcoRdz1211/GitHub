#include "colors.inc"
                     
background{color White}

camera {location <10, 0, 10> look_at <0, 0, 0>}

#declare steep=radians(10);
#declare Ball=sphere{<0,0,0> 0.1 pigment{color Green}}

#fopen outFile "sen.txt" write

#declare xx=-2*pi;
#while (xx<2*pi)
    #declare yy=sin(xx)/xx;
    
    object{Ball translate<xx,yy,0>} 
    
    #write(outFile,xx," ",yy,"\n")
    #declare xx=xx+steep;
#end

#fclose