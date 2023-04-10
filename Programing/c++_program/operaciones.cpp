// Programa: leer dos numeros dar la suma, resta, multiplicacion y division

#include <iostream>

using namespace std;

int main() { 
	float a,b,suma,resta,mult,division;
	
	cout << "Dar dos numeros: ";
	cin >> a >> b;
	
	suma = a+b;
	resta = a-b;
	mult = a*b;
	division = a/b;
	
	cout << "\n La suma de los numeros es: " << suma;
	cout << "\n La resta de los numeros es: " << resta;
	cout << "\n La multiplicacion de los numeros es: " << mult;
	cout << "\n La division de los numeros es: " << division;
	
	return 0;
}

