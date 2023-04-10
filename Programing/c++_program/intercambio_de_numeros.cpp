//Programa: intercambio de valores

#include <iostream>;

using namespace std;

int main() {
	float x,y,aux;
	
	cout << "Dar dos numeros: ";
	cin >> x >> y;
	
	cout << "El valor del primer numero es: " << x;
	cout << "\n El valor del segundo numero es: " << y;
	
	aux = x;
	x = y;
	y = aux;
	
	cout << "\n El valor del primer numero intercambiado es: " << x;
	cout << "\n El valor del segundo numero intercambiado es: " << y;
	
	return 0;
}
