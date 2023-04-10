!Definicion de la funcion f, tal que: dy/dx=f(y,t)
function f(y,t)
    real:: f,y,t

    f = -2.0*t**3.0+12.0*t**2-20*t+8.5

    return
end function

!Inicio del programa e inicialización de las variables
program Asesoria1
implicitnone
real:: t0,y0,h,t,tf,y,f
integer:: i,n

write(*,*) "Este programa determina la solucion y(a) de una ecuacion diferencial"

!Condiciones iniciales.
t0=0
y0=1
tf=1
h=0.01
n=(tf-t0)/h

y=y0
t=t0

write(*,*) "El valor de: y(", t, ")=", y  

do i=1,n
  y=y+h*f(y,t)
  t = t0+i*h
  
  write(*,*) "El valor de: y(", t, ")=", y

end do

write(*,*) "El valor de: y(", t, ")=", y

pause
stop
end program