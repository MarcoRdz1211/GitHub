//Programa: suma de los primeros n cuadrados.

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n,suma;
	
	cout << "Dar hasta que cuadrado se quiere obtener: "; cin >> n;
	
	suma = 0;
	
	for(int i=0; i<=n; i++){
		cout << i << "^2 = " << pow(i,2) << endl;
		suma += pow(i,2);
	}
	
	cout << suma;
	
	return 0;
}
