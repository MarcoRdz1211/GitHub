#Programa que resuelve ecuaciones diferenciales mediante el metodo de interfases

x0 = 0.0;
xf = 1.0;
alpha = 0.72;
a = 1;

DisplayPlotAnswer = 1;
DisplayLatexAnswer = 1;
DisplaySmAnswer = 1;

ExampleB = 1;
ExampleF = 1;

m = 6;
Mnodes = @(x) 10*power(2,(n-1));

if ExampleF==1
  uL = @(x) cos(A*x);
  uxL = @(x) -A*sin(A*x);
  uxxL = @(x) -(A*A)*cos(A*x);

  uR = @(x) cos(A*x);
  uxR = @(x) -A*sin(A*x);
  uxxR = @(x) -(A*A)*cos(A*x);

elseif ExampleF==2
  uL = @(x) (power(x,3))/3;
  uxL = @(x) power(x,2);
  uxxL = @(x) 2*x;

  uR = @(x) (power(x,3))/3;
  uxR = @(x) power(x,2);
  uxxR = @(x) 2*x;

elseif ExampleF==2
  A= 1;
  B= 2;

  uL = @(x) cos(A*x);
  uxL = @(x) -A*sin(A*x);
  uxxL = @(x) -(A^A)*cos(A*x);

  uR = @(x) cos(B*x);
  uxR = @(x) -B*sin(B*x);
  uxxR = @(x) -(B*B)*cos(B*x);

end


if ExampleB==1

  bL = @(x) 1+0*x;
  bxL = @(x) 0*x;
  bxxL = @(x) 0*x;

  bR = @(x) 1+0*x;
  bxR = @(x) 0*x;
  bxxR = @(x) 0*x;

elseif ExampleB==2
  bL   = @(x) 2+0*x;
  bxL  = @(x) 0*x;
  bxxL = @(x) 0*x;

  bR   = @(x) 1+0*x;
  bxR  = @(x) 0*x;
  bxxR = @(x) 0*x;

elseif ExampleB==3

  bL = @(x) power(x,2);
  bxL = @(x) 2*x;
  bxxL = @(x) 2;

  bR = @(x) x^2;
  bxR = @(x) 2*x;
  bxxR = @(x) 2;

elseif ExapleB==4

  bL = @(x) cos(x);
  bxL = @(x) -sin(x);
  bxxL = @(x) -cos(x);

  bR = @(x) x^2;
  bxR = @(x) 2*x;
  bxxR = @(x) 2;

end

fL = @(x) bxL(x)*uxL(x)+bL(x)*uxxL(x)-a*uxL(x);
fR = @(x) bxR(x)*uxR(x)+bR(x)*uxxR(x)-a*uxR(x);

beta = @(x) (x<=alpha)*bL(x) + (x>alpha)*bR(x);
f    = @(x) (x<=alpha)*fL(x) + (x>alpha)*fR(x);

disp("-------------------------------------")
Norm1 = zeros(n,1);
Norm2 = zeros(n,2);
OrderOr1 = zeros(n,1);
OrderOr2 = zeros(n,2);

for s=1:m
  n = Mnodes(s);
  x = linspace(x0,xf,n+1);
  fprintf(s,n+1)

  for i=1:n
    if (x(i) <= alpha)& (x(i) >= alpha);
      I = i;
      break;
    end
  end

  h = x(2)-x(1);
  h2 = h^2;
  n0 = n-2;

  A1 = zeros(n-1,1);
  A2 = zeros(n-1,1);
  A3 = zeros(n-1,1);
  b = zeros(n-1,1);

  for i=1:n-1
    xL = x(i+1)-h/2;
    xR = x(i+1)+h/2;

    A1(i) = beta(xL)/h2+a/(2*h);
    A2(i) = beta(xR)/h2-a/(2*h);
    A3(i) = -(A1(i)+A2(i));
    b(i) = f(x(i+1));

  end

  b(1) = b(1)-A1(1)*uL(x(1));
  b(n-1) = b(n-1)-A3(n-1)*uR(n-1);

  Uaux = Thomas(A1(2:end),A2,A3(1:n-2),b);

  Ua = uL(x(1));
  Ub = uR(x(n+1));
  U = [Ua,Uaux,Ub];

  Ureal = zeros(n+1,1);

  for i=1:I
    Ureal(i) = uL(x(i));
  end
  for i=I+1:n+1
    Ureal(i) = uR(x(i));
  end

end
