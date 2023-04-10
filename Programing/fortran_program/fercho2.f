       Program FER TE Quiero Mucho2
       Implicit None
       real:: t0,x0,y0,vx0,vy0,tf,h,x,y,vx,vy,t,k1,k2,k3,k4,L1,L2,L3,L4
       real:: m1,m2,m3,m4,f,g,fx,gy,A(100,5),q1,q2,q3,q4
       integer:: n,i

      t0 = 0
      x0 = 45
      y0 = 0.1
      vx0 = 0
      vy0 = 0
      tf = 10
      n = 5
      h = (tf-t0)/n
      x = x0
      y = y0
      vx = vx0
      vy = vy0
      t = t0


       do i=1,n
       k1=h*vx
       L1=h*f(x,y,vx,vy,t)
       q1=h*vy
       m1=h*g(x,y,vx,vy,t)

       k2=h*(vx+0.5*L1)
       L2=h*f(x+0.5*k1,y+0.5*q1,vx+0.5*L1,vy+0.5*m1,t+0.5*h)
       q2=h*(vy+0.5*m1)
       m2=h*g(x+0.5*k1,y+0.5*q1,vx+0.5*L1,vy+0.5*m1,t+0.5*h)

       k3=h*(vx+0.5*L2)
       L3=h*f(x+0.5*k2,y+0.5*q2,vx+0.5*L2,vy+0.5*m2,t+0.5*h)
       q3=h*(vy+0.5*m2)
       m3=h*g(x+0.5*k2,y+0.5*q2,vx+0.5*L2,vy+0.5*m2,t+0.5*h)

       k4=h*(vx+L3)
       L4=h*f(x+k3,y+q3,vx+L3,vy+m3,t+h)
       q4=h*(vy+m3)
       m4=h*g(x+k3,y+q3,vx+L3,vy+m3,t+h)

       x=x+(1/6)*(k1+2.0*k2+2.0*k3+k4)
       vx=vx+(1/6)*(L1+2.0*L2+2.0*L3+L4)
       y=y+(1/6)*(q1+2.0*q2+2.0*q3+q4)
       vy=vy+(1/6)*(m1+2.0*m2+2.0*m3+m4)
       t = t+h


       write(*,*) k1,L1,q1,m1
       write(*,*) k2,L2,q2,m2
       write(*,*) k3,L3,q3,m3
       write(*,*) k4,L4,q4,m4
       write(*,*) x,vx,y,vy,t

        pause

        A(i,1) = t
        A(i,2) = x
        A(i,3) = y
        A(i,4) = vx
        A(i,5) = vy


       end do

       open(5,file="fer te quiero.txt")

       do i=1,n
        write(5,*) A(i,1),A(i,2),A(i,3),A(i,4),A(i,5)

       end do

      close(5)


       pause
       stop
       End Program


        function fx(x,y,vx,vy,t)
       real:: fx,x,y,vx,vy,t

        fx = vx

        return
       end function

       function f(x,y,vx,vy,t)
       real:: f,x,y,vx,vy,t,L
       L=0.5

        f = -1.0/(L+y)*(2.0*vx*vy+9.8*sin(x))

        return
        
        end function
        
             function gy(x,y,vx,vy,t)
       real:: gy,x,y,vx,vy,t

        gy = vy

        return
       end function

       function g(x,y,vx,vy,t)
       real:: g,x,y,vx,vy,t,L,k,m
       l=0.5

        g = (L+y)*((vx)**2)+9.5*cos(x)-(100.0)*y

        return
        end function
