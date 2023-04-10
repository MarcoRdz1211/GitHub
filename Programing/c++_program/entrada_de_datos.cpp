//Programa: entrada de datos

#include <iostream>

using namespace std;

/*
	Comentario 
	muy
	muy
	muy
	largo
*/

int main() {
	int x;
	float y;
	double z;
	long long n;
	char p;
	
	cout << "Dat un numero entero: ";
	cin >> x;
		
	cout << "Dat un numero decimal: ";
	cin >> y;
	
	cout << "Dat un numero largo: ";
	cin >> z;
	
	cout << "Dat un numero muy largo: ";	
	cin >> n;
	
	cout << "Dat un caracter: ";
	cin >> p;
	
	cout << "Este es el entero dado: " << x << endl;
	
	cout << "Este es el decimal dado: " << y << endl;

	cout << "Este es el numero largo dado: " << z << endl;

	cout << "Este es el numero muy largo dado: " << n << endl;

	cout << "Este es el caracter dado: " << p << endl;
	
	return 0;
}
