//Programa: Creacion de matrices.

#include <iostream>

using namespace std;

int main() {
	int n,m;
	
	cout << "Give the dimension of the matrix: "; cin >> n >> m;
	
	int matrix[n][m];
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cout << "Give the element (" << i << "," << j << ") "; cin >> matrix[i][j];
		}
	}

	cout << "The matrix is: " << endl;

	for(int i=0; i<n; i++){
		cout << "[ ";
		for(int j=0; j<m; j++){
			cout << matrix[i][j] << " ";
		}
		cout << "]" << endl;
	}
	
	return 0;
}
