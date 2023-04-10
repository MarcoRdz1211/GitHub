//Programa: suma de elementos de un arreglo.

#include <iostream>

using namespace std;

int main() {
	int n,suma=0;
	
	cout << "Dar el tamaño del arreglo: "; cin >> n;
	
	int num[n];
	
	for(int i=0; i<n; i++){
		cout << "Dar el elemento " << i << " del arreglo: "; cin >> num[i];	
	}
	
	for(int i=0; i<n; i++){
		suma += num[i];
	}
	
	cout << "La suma de los valores del arreglo es: " << suma;
	
	return 0;
}

