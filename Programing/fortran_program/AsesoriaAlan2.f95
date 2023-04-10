!Inicio de programa
program Asesoria1Alan
!No asumas nada fortran, porfavor
implicitnone
!Declaracion de naturaleza de las variables
real:: t0,y0,h,yold,ynew,t,f
integer:: i

!Escribir que hace el programa
write(*,*) "Programa que determina y(1), para la ecuacion diferencial: y'=g-cv^2/m; sabiendo que: y(1)=0"

!Declaracion de variables iniciales
t0=1.0
y0=0.0
h=0.001
i=0

!Variables auxiliares
yold = y0-1
ynew = y0
t = t0

!Inicio del ciclo
do while (abs(ynew-yold)>=10.0**(-5.0))
  i = i+1
  yold = ynew
  ynew = yold+h*f(yold,t)
  t = t0+i*h

  write(*,*) "El valor de y(", t, ")=", ynew
  
end do

write(*,*) "La cantidad de pasos que hizo fue:", i

!Fin de programa
end program

!Definiendo una funcion
function f(v,t)
    real:: f,v,g,c,m,t

    g = 9.81    
    c = 12.5
    m = 68.1
    !Declaracion de la funcion
    f = g-(c/m)*v**2

    return
end function