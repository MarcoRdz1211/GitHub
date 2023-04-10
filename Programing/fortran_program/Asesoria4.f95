function f(y,t)
    real:: f,y,t

    f=y

    return
end function    

program Asesoria4
implicitnone
real:: f,t0,y0,tf,h,y,t,K1,K2,K3,K4
integer:: n,i

t0=0
y0=1
tf=1
h=0.25
n=(tf-t0)/h

y=y0
t=t0

write(*,*) "Este programa determina la solucion: y(", tf, ") para: y'=y"

write(*,*) "El valor de: y(", t, ")=", y
  
do i=1,n
    K1=f(y,t)
    K2=f(y+0.5*h*K1,t+0.5*h)
    K3=f(y+0.5*h*K2,t+0.5*h)
    K4=f(y+h*K3,t+h)
    
    y=y+(h/6.0)*(K1+2*K2+2*K3+K4)
    t=t0+i*h
    
    write(*,*) "El valor de: y(", t, ")=", y

end do

write(*,*) "El valor de: y(", t, ")=", y

pause
stop
end program