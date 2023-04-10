program GrafiarDatos
implicitnone
real:: x0,xf,x,y,f,h,A(200,2)
integer:: n,i

write(*,*) "Programa que determina los valores de f(x)=x^2, para 0<=x<=5 con 200 intervalos"

x0 = 0.0
xf = 5.0
n = 200
h = (xf-x0)/n
x = x0

do i=1,n
    y = f(x)
    x = x+h

    A(i,1) = x
    A(i,2) = y

    write(*,*) A(i,1),A(i,2)

end do

open(39,file="unu.txt")

    do i=1,n
        write(39,*) A(i,1),A(i,2)

    end do

close(39)

pause
stop
end program



function f(x)
    real:: f,x

    f = x**2.0

    return
end function