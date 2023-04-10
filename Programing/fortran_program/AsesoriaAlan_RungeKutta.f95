program RungeKutta
implicitnone
real:: t0,y0,t,tf,h,y,k1,k2,k3,k4,f
integer:: n,i

write(*,*) "Programa que determina la solucion de: y'=y"

t0 = 0.0
y0 = 1.0
tf = 1.0
h = 0.25
n = (tf-t0)/(1.0*h)
y = y0
t = t0

do i=1,n
    k1 = f(t,y)
    k2 = f(t+0.5*h,y+0.5*h*k1)
    k3 = f(t+0.5*h,y+0.5*h*k2)
    k4 = f(t+h,y+h*k3)

    y = y+(h/6.0)*(k1+2*k2+2*k3+k4)
    t = t+h

end do

write(*,*) "y(", t, ")=",y

pause
stop
end program

function f(t,y)
    real:: f,t,y

    f = y

    return
end function

program RungeKutta
implicitnone
real:: t0,y0,t,tf,h,y,k1,k2,k3,k4,f
integer:: n,i
