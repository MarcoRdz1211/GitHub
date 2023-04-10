//Programa: Determinar las raices de una ecuacion cuadratica

#include <iostream>
#include <math.h>

using namespace std;

int main(){
	float a,b,c,x1,x2;
	
	//ax^2+bx+c=0
	
	cout << "Dar el coeficiente del termino cuadratico, lineal e independiente respectivamene: ";
	cin >> a >> b >> c;
	
	if (pow(b,2)>=4*a*c){
		x1 = (-b+sqrt(pow(b,2)-4*a*c))/(2*a);
		x2 = (-b-sqrt(pow(b,2)-4*a*c))/(2*a);
	
		cout << "\n Las raices son:" << x1 << x2;
	}	
	else{
		cout << "\n Ambas raices son imaginarias";
	}
	
	return 0;
}
