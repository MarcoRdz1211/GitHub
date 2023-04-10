function fy(t,y,v)
    real:: fy,t,y,v

    fy = v

    return
end function

function fv(t,y,v)
    real:: fv,t,y,v

    fv = -9.8

    return
end function

program RungeKutta
implicitnone
real:: t0,y0,v0,t,tf,h,v,y,ky1,ky2,ky3,ky4,kv1,kv2,kv3,kv4,fy,fv,A(2000,3)
integer:: n,i

t0 = 0.0
y0 = 0.0
v0 = 1
tf = 2.0
h = 0.001
n = (tf-t0)/(1.0*h)
t = t0
y = y0
v = v0

do i=1,n
    ky1=fy(t,y,v)
    kv1=fv(t,y,v)
    ky2=fy(t+h/2.0,y+h*ky1/2.0,v+h*kv1/2.0)
    kv2=fv(t+h/2.0,y+h*ky1/2.0,v+h*kv1/2.0)
    ky3=fy(t+h/2.0,y+h*ky2/2.0,v+h*kv2/2.0)
    kv3=fv(t+h/2.0,y+h*ky2/2.0,v+h*kv2/2.0)
    ky4=fy(t+h,y+h*ky3,v+h*kv3)
    kv4=fv(t+h,y+h*ky3,v+h*kv3)

    y= y+(1.0/6.0)*h*(ky1+2.0*ky2+2.0*ky3+ky4)
    v= v+(1.0/6.0)*h*(kv1+2.0*kv2+2.0*kv3+kv4)
    t = t+h

    A(i,1) = t
    A(i,2) = y
    A(i,3) = v    

!    write(*,*) "y(", t, ")=",y
!    write(*,*) "v(", t, ")=",v

end do

!Graficar y con respecto a t

open(1,file="plot_data-RungeKutta2-t_vs_y.txt")

    do i=1,n
        write(1,*) A(i,1), A(i,2)
    end do

close(1)

open(2,file="plot_data-RungeKutta2-t_vs_y.txt")

    do i=1,n
        write(2,*) A(i,1), A(i,2)
    end do

close(2)

write(*,*) "y(", t, ")=",y
write(*,*) "v(", t, ")=",v

pause
stop
end program