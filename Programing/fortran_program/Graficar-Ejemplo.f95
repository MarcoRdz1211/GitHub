program Graficar
implicitnone
real:: x0,y0,xf,h,y,x,f,A(100,2)
integer:: n,i

write(*,*) "Programa que grafica un conjunto de puntos"

x0 = 0
y0 = f(x0)
xf = 5
n = 100
h = (xf-x0)/n
y = y0
x = x0

do i=1,n
    x = x+h
    y = f(x)
    
    A(i,1) = x
    A(i,2) = y

!    write(*,*) "f(", x, ")=", y

    write(*,*) "f(", A(i,1), ")=", A(i,2)

end do

open(1,file="plot_data-example1.txt")

    do i=1,n
      write(1,*) A(i,1), A(i,2)
    end do
    
close(1)

write(*,*) "f(", x, ")=", y

pause
stop
end program

function f(x)
    real:: f,x

    f = x**4.0-5.0*x**3.0+2.0*x+2.0

end function