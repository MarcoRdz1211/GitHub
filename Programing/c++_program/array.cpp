//Programa: Arreglo de numeros y escribirlos.

#include <iostream>

using namespace std;

int main() {
	int n;
	
	cout << "Give the number of elements in the array: "; cin >> n;
	
	int A[n],array[n];
	
	for(int i=0; i<n; i++){
		cout << "Give the element " << i+1 << " of the array: "; cin >> A[i];
	}
	
	for(int i=0; i<n; i++){
		cout << "A[" << i << "] = " << A[i] << endl;
	}
	
	return 0;
}
