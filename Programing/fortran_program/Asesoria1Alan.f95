!Inicio de programa
program Asesoria1Alan
!No asumas nada fortran, porfavor
implicitnone
!Declaracion de naturaleza de las variables
real:: t0,y0,tf,h,y,t,f
integer:: n,i

!Escribir que hace el programa
write(*,*) "Programa que determina y(1), para la ecuacion diferencial: y'=-2x^3+12x^2-20x+8.5; sabiendo que: y(0)=1"

!Declaracion de variables iniciales
t0=0.0
y0=1.0
tf=1.0
h=0.01
n=(tf-t0)/h

!Variables auxiliares
y = y0
t = t0

!Inicio del ciclo
do i=1,n
  y = y+h*f(y,t)
  t = t0+i*h

  write(*,*) "El valor de y(", t, ")=", y
  
end do

!Fin de programa
end program

!Definiendo una funcion
function f(y,x)
    real:: f,y,x
    
    !Declaracion de la funcion
    f = y

    return
end function

