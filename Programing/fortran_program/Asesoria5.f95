function f(y,x)
    real:: f,y,x

    f = -6*x

    return
end function

program Asesoria5
implicitnone
real:: t0,y0,v0,k1y,k2y,k3y,k4y,k1v,k2v,k3v,k4v,tf,t,y,v,h,f
integer:: n,i

t0 = 1
y0 = 3
v0 = 1
tf = 2
h = 0.1
n = (tf-t0)/h

t = t0
y = y0
v = v0

write(*,*) "Este programa determina: y(", tf, "), para la ecuacion diferencial: y''+6x=0"

write(*,*) "El valor de: y(", t, ")=", y
write(*,*) "El valor de: y'(", t, ")=", v

do i=1,n
    k1y = f(v,t)
    k1v = f(-y,t)
    k2y = f(v+0.5*h*k1v,t+0.5*h)
    k2v = f(-y-0.5*h*k1y,t+0.5*h)
    k3y = f(v+0.5*h*k2v,t+0.5*h)
    k3v = f(-y-0.5*h*k2y,t+0.5*h)
    k4y = f(v+h*k3v,t+h)
    k4v = f(-y-h*k3y,t+h)

    y = y+(h/6.0)*(k1y+2*k2y+2*k3y+k4y)
    v = v+(h/6.0)*(k1v+2*k2v+2*k3v+k4v) 
    t = t0+i*h  

!    write(*,*) "El valor de: y(", t, ")=", y
!    write(*,*) "El valor de: y'(", t, ")=", v

end do

    write(*,*) "El valor de: y(", t, ")=", y
    write(*,*) "El valor de: y'(", t, ")=", v

pause
stop
end program