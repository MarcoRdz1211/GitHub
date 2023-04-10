//Programa: calcular x^y sin usar pow.

#include <iostream>

using namespace std;

int main() {
	int x,y,resultado;
	
	cout << "Dar dos numeros: "; cin >> x >> y;
	
	resultado = x;
	
	for(int i=1; i<y; i++){
		resultado *= x;
	}

	cout << "El valor de: " << x << "^" << y << " es: " << resultado;

	return 0;
}

