//Programa: Sentencia switch

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	float a,b,c,d;
	int result;
	
//	ax^2+bx+c=0
	
	cout << "Dar el coeficiente del termino cuadratico, lineal e independiente respecitivamente: ";
	cin >> a >> b >> c;

	d = pow(b,2)-4*a*c;
	
	cout << d << endl;
	
	if(d>0){
		cout << "El valor del discriminante es mayor a 0" << endl; 
		result = 1;
	}
	else{if(d==0){
			cout << "El valor del discrimiante es igual a 0" << endl;
			result = 0;
		}
		else{ 
			cout << "El valor del discriminante es menor a 0" << endl;
			result = -1;
		}
	}
	

	switch(result){
		case 1: cout << "Las raices son reales y distintas."; break;
		case 0: cout << "Las raices son reales e iguales."; break;
		case -1: cout << "Las raices son imaginarias."; break;
	}
	
	return 0;
}
