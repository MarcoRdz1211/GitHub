//Programa: Ordenar un conjunto de numeros.

#include <iostream>

using namespace std;

int main() {
	int n,a,b;
	
	cout << "Give the number of elements of the array: "; cin >> n;
	
	int A[n];
	
	for(int i=0; i<n; i++){
		cout << "Give the element " << i+1 << " of the array: "; cin >> A[i];
	}
	
	for(int i=0; i<n-1; i++){
		for(int j=i+1; j<n; j++){
			if(A[i]>A[j]){
				a = A[i]; b = A[j]; 
				A[i] = b; A[j] = a;
			}			
		}
	}
	
	cout << "Elements ordenated:" << endl;
	
	for(int i=0; i<n; i++){
		cout << "A[" << i+1 << "] = " << A[i] << endl; 
	}
	
	return 0;
}
