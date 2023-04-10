program RungeKutta
implicitnone
real:: t0,y0,v0,tf,h,y,v,t,ky1,kv1,ky2,kv2,ky3,kv3,ky4,kv4,fy,fv,A(100,3)
integer:: n,i

write(*,*) "Programa que determina la solucion de: y''+6t=0"

t0 = 0
y0 = 0
v0 = 1
tf = 4.0
n = 100
h = (tf-t0)/n
y = y0
v = v0
t = t0

do i=1,n
    ky1 = fy(t,y,v)
    kv1 = fv(t,y,v)
    ky2 = fy(t+0.5*h,y+0.5*h*ky1,v+0.5*h*kv1)
    kv2 = fv(t+0.5*h,y+0.5*h*ky1,v+0.5*h*kv1)
    ky3 = fy(t+0.5*h,y+0.5*h*ky2,v+0.5*h*kv2)
    kv3 = fv(t+0.5*h,y+0.5*h*ky2,v+0.5*h*kv2)
    ky4 = fy(t+h,y+h*ky3,v+h*kv1)
    kv4 = fv(t+h,y+h*ky3,v+h*kv1)

    y = y+(h/6.0)*(ky1+2*ky2+2*ky3+ky4)
    v = v+(h/6.0)*(kv1+2*kv2+2*kv3+kv4)
    t = t+h

    A(i,1) = t
    A(i,2) = y
    A(i,3) = v

end do

write(*,*) "y(", t, ")=",y
write(*,*) "v(", t, ")=",v

open(1,file="si.txt")

    do i=1,n
        write(1,*) A(i,1),A(i,2),A(i,3)

    end do

close(1)

pause
stop
end program


function fy(t,y,v)
    real:: fy,t,y,v

    fy = v

    return
end function

function fv(t,y,v)
    real:: fv,t,y,v

    fv = -y

    return
end function