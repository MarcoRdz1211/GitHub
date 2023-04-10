function f(y,t)
    real:: f,y,t

    f=y

    return
end function

program Asesorias2
real:: t0,y0,h,t,tf,y,ynew,f
integer:: n,i

t0=0
tf=1
y0=1
h=0.01
n = (tf-t0)/h
y = y0
t = t0

write(*,*) "Programa que aproxima el valor de y(", t0, ") para la funcion solucion de: y'=y en [0,1]"

write(*,*) "El valor de y(", t, ")=", y

do i=1,n
    ynew = y+h*f(y,t)
    y = y+0.5*h*(f(y,t)+f(y,t+h))
    t = t0+i*h

    write(*,*) "El valor de y(", t, ")=", y

end do

write(*,*) "El valor de y(", t, ")=", y

pause
stop
end program
