program AsesoriaAlan3
implicitnone
real:: x0,y0,xf,h,y,f
integer:: i,n

write(*,*) "Resolucion de la ecuacion diferencial: y'=f(x,y), sujeta a y(0)=1"

x0 = 0.0
y0 = 1.0
xf = 1.0
n = 2000
h = (xf-x0)/(1.0*n)
y = y0

do i=0,n-1
    y = y+f(x0+i*h,y)*h

end do

write(*,*) "El valor de y(", xf, ")=", y

pause
stop
end program

function f(x,y)
    real:: f,x,y

    f = y

    return
end function