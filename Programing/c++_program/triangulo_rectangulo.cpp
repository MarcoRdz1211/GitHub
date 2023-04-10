//Programa: dadas las entradas de dos catetos, determinar la hipotenusa

#include <iostream>;
#include <math.h>;

using namespace std;

int main() {
	float a,b,c;
	
	cout << "Dar los dos cateto del triangulo rectangulo: ";
	cin >> a >> b;
	
	c = sqrt(pow(a,2)+pow(b,2));
	
	cout << "El valor de la hipotenusa es: " << c;
	
	return 0;
}
