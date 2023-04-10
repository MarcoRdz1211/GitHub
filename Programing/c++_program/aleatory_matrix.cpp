//Programa: Dadas las dimensiones de una matriz, regresarla con numeros aleatorios.

#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() {
	int n,m;
	
	cout << "Give the dimension of the matrix: "; cin >> n >> m;
	
	long long A[n][m];
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			A[i][j] = rand();
		}
	}

	for(int i=0; i<n; i++){
		cout << "[";
		for(int j=0; j<m; j++){
			cout << " "<< A[i][j];
		}
		cout << "]" << endl;
	}
	
	return 0;
}
