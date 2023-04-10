Program RK4Shooting
! Se resuelve una ecuacion de segundo orden

! Se usa dos grupos de funciones.
! La posicion esta dada por: K1y,K2y,K3y,K4y
! La velocidad por: K1v, K2v, K3v y K4v
! Aqui t es la variable independiente!!!

      real K1y,K2y,K3y,K4y
      real K1v,K2v,K3v,K4v
      real*8 t,yi,yf,c,y,pi,v, t0, d1y, d2y
      integer n

      OPEN( 9,  FILE='funcion_analitica.txt' )
      OPEN( 10, FILE='fnumerica.txt' )
      OPEN( 11, FILE='derivada_analitica.txt' )
      OPEN( 12, FILE='derivada_num.txt' )

! Se debe dar un valor inicial de la derivada de la funci¢n (v)
!        WRITE(*,*) "Entra un valor de y' inicial: "
!        READ(*,*) v
      v = 1
!      Condiciones iniciales
!      Condiciones iniciales
   !***************   ejercicio 1  ***********************************
           t0=0.d0   ! Indica el valor de t0 en y(t0)
      y=0.d0   !y(0) inicial
      !v=-1.0  !y'(0) inicial    Sol: 32.5
      n=510!numero de intervalos
      h=0.01d0

!***********       CONDICIONES INICIALES   ***************************
      y0=y   ! Funcion ...asume que t0= 0.0
      v0=v   ! Derivada de la funcion ...asume que t0= 0.0
      contador=1
      write(*,*) '    t         Yreal          DYreal     Ycalc  DYcalc'
!   Se hacen los ciclos con 2 ecuaciones de primer orden
!   acopladas
! Recordas que la velocidad y la posici¢n son funcion del tiempo
!      V(t) es la primer derivada
!      Y (t) es la posicion
      do 10 i =1,n
      t= t0+h*float(i) !incrementos del tiempo



! ********************  Ejercicio 1 *******************************
           Yreal= 5.d0
      Vreal= 3.d0    !derivada analitica
      !yError=yreal-yf
  ! ********************  Ejercicio 3 *******************************
      !     Yreal= log(1.d0/t)+2.d0
      !Vreal= -1.d0/t    !derivada analitica
 !     yError=yreal-yf

! ********************  Ejercicio 8 *******************************
      !Yreal= 1.1392070132*t+(-0.039207/t**2.)-(0.3*sin(log(t)))-0.1d0*cos(log(t))  !Funcion analitica
      !Vreal= 1.d0/(t+1.d0)    !derivada analitica
      !yError=yreal-yf

      K1y=d1y(t, y, v)
      K1v=d2y(t, y, v)

      K2y=d1y(t+h/2.,  y+h*K1y/2.,  v+h*K1v/2.)
      K2v=d2y(t+h/2.,  y+h*K1y/2.,  v+h*K1v/2.)

      K3y=d1y(t+h/2.,  y+h*K2y/2.,  v+h*K2v/2.)
      K3v=d2y(t+h/2.,  y+h*K2y/2.,  v+h*K2v/2.)

      K4y=d1y(t+h,   y+h*K3y,  v+h*K3v)
      K4v=d2y(t+h,   y+h*K3y,  v+h*K3v)

      yf= y0+(1./6.)*h*(K1y+   2.*K2y+  2.*K3y+  K4y)
      Vf= V0+(1./6.)*h*(K1v+   2.*K2v+  2.*K3v+  K4v)

      If(i.eq.contador)then
       WRITE( *,20)t, yreal,vreal,yf,Vf
       WRITE( 9,30)t, yreal ! Valores de la funcion analitica
       WRITE(10,30)t, yf ! Valores de la funcion (numericos)
       WRITE(11,30)t, Vf  ! Valores de la derivada analitica
       WRITE(12,30)t, Vreal
      contador=contador+1
!      print*,'   '
      endif
      y=yf
      v=Vf
      y0=yf
      V0=Vf

   20 FORMAT(7(1X,F16.8))
   30 FORMAT(2(1X,F16.8))
10    continue
      Pause
      stop
      end

      ! VELOCIDAD
!Calcula dX/dt....primer derivada de y
      FUNCTION d1y(t,y,v)
      implicit none
      Real*8 d1y, t, y,v, g,L,pi
      d1y=v
      RETURN
      END

      ! ACELERACION
! Calcula dV/dt ....segunda derivada de y
! Esta es v'
      FUNCTION d2y(t,y,v)
      implicit none
      Real*8  d2y, t, y, v,g,L,pi
      d2y=-9.8  !Ejemplo 1  Soluci¢n=32.5 m/s
!        d2y=-v/t !Ejemplo 3
!      d2y=4.2d0*t-t*v+3.d0*y !Ejemplo 4
!       d2y= -y  !Ejemplo 5
       !d2y=y+v*t !Ejemplo 6
!       d2y=-v**2.d0        ! Ejercicio 7
 !     d2y=(-2./t)*v+(2./t**2.)*y+(sin(log (t))/t**2.) !Ejercicio 8
!      d2y= 8.*t*(9.-t)+2.d0*y   ! Ejercicio 9


      RETURN
      END
