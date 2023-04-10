//Programa: leer entradas de datos tipo caracter y escribirlos

#include <iostream>;

using namespace std;

int main() {
	int edad;
	char sexo[20];
	float heigh;
	
	cout << " Dar la edad: "; cin >> edad;
	cout << "\n Dar el sexo: "; cin >> sexo;
	cout << " \n Dar la altura en metros: "; cin >> heigh;
	
	cout << "La edad es: " << edad << endl;
	cout << "EL sexo es: " << sexo << endl;
	cout << "La altura en metros es:" << heigh << endl;
	
	return 0;
}
