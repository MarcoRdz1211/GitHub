//Programa: Multiplicacion de elementos en un arreglo.

#include <iostream>

using namespace std;

int main() {
	int n;
	long long mult=1;
	
	cout << "Give the lengh of the array: "; cin >> n;
	
	int A[n];
	
	for(int i=0; i<n; i++){
		cout << "Give the element " << i+1 << " of the array: "; cin >> A[i];
	}
	
	for(int i=0; i<n; i++){
		mult *= A[i];
	}
	
	cout << "The multiplication of the elements of the array is: " << mult;
	
	return 0;
}
