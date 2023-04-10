      PROGRAM RungeKutta
      IMPLICIT NONE

      REAL K1y1, K2y1, K3y1, K4y1, K1v1, K2v1, K3v1, K4v1
      REAL K1y2, K2y2, K3y2, K4y2, K1v2, K2v2, K3v2, K4v2
      REAL y1, y2, v1, v2, t, y10, y20, v10, v20, t0, Limite, h
      REAL y1f, y2f, v1f, v2f
      REAL d1y1, d2y1, d1y2, d2y2
      INTEGER i

      OPEN(9, FILE = "y1.txt")
      OPEN(10, FILE = "v1.txt")
      OPEN(11, FILE = "y2.txt")
      OPEN(12, FILE = "v2.txt")

      y1 = 3.1416/4
      y2 = 0.0d0
      v1 = 0.d0
      v2 = 0.d0
      t = 0.d0
      
      Limite = 10.0
      h = 0.01d0
      
      y10 = y1
      y20 = y2
      v10 = v1
      v20 = v2
      t0 = t

      i = 1
      DO WHILE (t.LE.Limite)

      K1y1 = d1y1(t, y1, v1)
      K1y2 = d1y2(t, y2, v2)
      
      K1v1 = d2y1(t, y1, y2, v1, v2)
      K1v2 = d2y2(t, y1, y2, v1, v2)
      
      K2y1 = d1y1(t+h/2.0, y1+h*K1y1/2.0, v1+h*K1v1/2.0)
      K2y2 = d1y2(t+h/2.0, y2+h*K1y2/2.0, v2+h*K1v2/2.0)
      
      K2v1 = d2y1(t+h/2.0, y1+h*K1y1/2.0, y2+h*K1y2/2.0,
     & v1+h*K1v1/2.0, v2+h*K1v2/2.0)
      K2v2 = d2y2(t+h/2.0, y1+h*K1y1/2.0, y2+h*K1y2/2.0,
     & v1+h*K1v1/2.0, v2+h*K1v2/2.0)

      K3y1 = d1y1(t+h/2.0, y1+h*K2y1/2.0, v1+h*K2v1/2.0)
      K3y2 = d1y2(t+h/2.0, y2+h*K2y2/2.0, v2+h*K2v2/2.0)
      
      K3v1 = d2y1(t+h/2.0, y1+h*K2y1/2.0, y2+h*K2y2/2.0,
     & v1+h*K2v1/2.0, v2+h*K2v2/2.0)
      K3v2 = d2y2(t+h/2.0, y1+h*K2y1/2.0, y2+h*K2y2/2.0,
     & v1+h*K2v1/2.0, v2+h*K2v2/2.0)

      K4y1 = d1y1(t+h, y1+h*K3y1, v1+h*K3v1)
      K4y2 = d1y2(t+h, y2+h*K3y2, v2+h*K3v2)
      
      K4v1 = d2y1(t+h, y1+h*K3y1, y2+h*K3y2, v1+h*K3v1, v2+h*K3v2/2.0)
      K4v2 = d2y2(t+h, y1+h*K3y1, y2+h*K3y2, v1+h*K3v1, v2+h*K3v2/2.0)

      y1f = y10 + (1.0/6.0)*h*(K1y1 + 2.0*K2y1 + 2.0*K3y1 + K4y1)
      y2f = y20 + (1.0/6.0)*h*(K1y2 + 2.0*K2y2 + 2.0*K3y2 + K4y2)
      
      v1f = v10 + (1.0/6.0)*h*(K1v1 + 2.0*K2v1 + 2.0*K3v1 + K4v1)
      v2f = v20 + (1.0/6.0)*h*(K1v2 + 2.0*K2v2 + 2.0*K3v2 + K4v2)
      
      WRITE(9, 30) t, y1f
      WRITE(10, 30) t, v1f
      WRITE(11, 30) t, y2f
      WRITE(12, 30) t, v2f
      
      y1 = y1f
      y2 = y2f
      v1 = v1f
      v2 = v2f
      
      y10 = y1f
      y20 = y2f
      v10 = v1f
      v20 = v2f
      
      i = i + 1
      t = t0 + h*float(i)

      END DO

   30 FORMAT(2(1X,F20.8))

      PAUSE
      STOP
      END

      FUNCTION d1y1(t, y1, v1)
      IMPLICIT NONE
      REAL d1y1, t, y1, v1
      d1y1 = v1
      RETURN
      END
      
      FUNCTION d2y1(t, y1, y2, v1, v2)
      IMPLICIT NONE
      REAL  d1y1, d1y2, d2y1, t, y1, y2, v1, v2, l, g
      l = 0.5
      g = 9.81
      d2y1 = (-1.0/(l+y2))*((2.0*d1y1(t,y1,v1)*d1y2(t,y2,v2))+g*sin(y1))
      RETURN
      END

      FUNCTION d1y2(t, y2, v2)
      IMPLICIT NONE
      REAL d1y2, t, y2, v2
      d1y2 = v2
      RETURN
      END

      FUNCTION d2y2(t, y1, y2, v1, v2)
      IMPLICIT NONE
      REAL  d1y1, d1y2, d2y2, t, y1, y2, v1, v2, l, m, g, k
      k = 100
      m = 1.0
      l = 0.5
      g = 9.81
      d2y2 = (-k/m)*y2 + (l+y2)*(d1y1(t, y1, v1))**2 + g*cos(y1)
      RETURN
      END
      
      
      
      
      
      
      
      
      
             k1=h*fx(x,vx,t)
       L1=h*f(x,y,vx,vy,t)
       q1=h*gy(y,vy,t)
       m1=h*g(x,y,vx,vy,t)

       k2=h*fx(x,vx+0.5*L1,t)
       L2=h*f(x+0.5*k1,y+0.5q1,vx+0.5*L1,vy+0.5*m1,t+0.5*h)
       q2=h*gy(y,vy+0.5*m1,t)
       m2=h*g(x+0.5*k1,y+0.5*q1,vx+0.5*L1,vy+0.5*m1,t+0.5*h)

       k3=h*fx(x,vx+0.5*L2,t)
       L3=h*f(x+0.5*k2,y+0.5q2,vx+0.5*L2,vy+0.5*m2,t+0.5*h)
       q3=h*gy(y,vy+0.5*m2,t)
       m3=h*g(x+0.5*k2,y+0.5*q2,vx+0.5*L2,vy+0.5*m2,t+0.5*h)

       k4=h*fx(x,vx+L3,t)
       L4=h*f(x+k3,y+q3,vx+L3,vy+m3,t+h)
       q4=h*gy(y,vy+m3,t)
       m4=h*g(x+k3,y+q3,vx+L3,vy+m3,t+h)


       x=x+(1/6)*(k1+2.0*k2+2.0*k3+k4)
       vx=vx+(1/6)*(L1+2.0*L2+2.0*L3+L4)
       y=y+(1/6)*(q1+2.0*q2+2.0*q3+q4)
       vy=vy+(1/6)*(m1+2.0*m2+2.0*m3+m4)
       t = t+h

