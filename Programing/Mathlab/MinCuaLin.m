%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%              ---  Método de Mínimos Cuadrados Lineales ---              %
%                          Miguel Angel Uh Zapata                         %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                         %
%  Esta función calcula la recta de ajuste f de un número de              %
%  puntos (x,y) usando el método de mínimos cuadrados y evualua la aprox. %
%  del vector u:                                                          %
%                     v(k) = f(u(k)) = a*u(k) + b                         %
%                                                                         %
%  ENTRADAS:                                                              %
%            x   : vector de las coordenadas x de los puntos a interpolar %
%            y   : vector de las coordenadas y de los puntos a interpolar %
%            u   : vector de puntos a evaluar                             %
%  SALIDAS:                                                               %
%            v   : puntos evaluados por la interpolacion.                 %
%                                                                         %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [a,b] = MinCuaLin(x,y)
n = length(x);
%_______________________________________
% Calcular a y b

sumx2 = 0;
sumxy = 0;
sumy  = 0;
sumx  = 0;
for i=1:n
   sumx2 = sumx2 + x(i)*x(i);
   sumxy = sumxy + x(i)*y(i);
   sumy  = sumy  + y(i);
   sumx  = sumx  + x(i);
end
deter = n*sumx2-sumx*sumx;
a = (n*sumxy-sumx*sumy)/deter;
b = (sumx2*sumy-sumxy*sumx)/deter;

end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
