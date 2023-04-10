function X=Thomas(A1,A2,A3,B)
%Resuelve un sistema lineal tridiagonal
%A1        diagonal inferior
%A2        diagonal principal
%A3        diagonal superior
n = length(B);
for i=1:n-1
    A2(i+1) = A2(i+1)-A3(i)*A1(i)/A2(i);
    B(i+1)  = B(i+1)  -B(i)*A1(i)/A2(i);
end
X(n) = B(n)/A2(n);
for i=n-1:-1:1
    X(i) = (B(i)-X(i+1)*A3(i))/A2(i);
end