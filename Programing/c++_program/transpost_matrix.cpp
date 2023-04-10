//Programa: Determinar la matriz transpuesta.

#include <iostream>

using namespace std;

int main() {
	int n,m;
	
	cout << "Give the dimension of the matrix: "; cin >> n >> m;
	
	long long A[n][m],Trans[m][n];
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cout << "Give the element (" << i << "," << j << ") ";
			cin >> A[i][j];
		}
	}
	
	cout << "Original matrix: " << endl;
	
	for(int i=0; i<n; i++){
		cout << "[";
		for(int j=0; j<m; j++){
			cout << " " << A[i][j];
		}
		cout << "]" << endl;
	}
	
	for(int i=0; i<m; i++){
		for(int j=0; j<n; j++){
			Trans[i][j]=A[j][i];
		}
	}
	
	cout << "Tranpost matrix:" << endl;
	
	for(int i=0; i<m; i++){
		cout << "[";
		for(int j=0; j<n; j++){
			cout << " " << Trans[i][j];
		}
		cout << "]" << endl;
	}
	
	return 0;
}
