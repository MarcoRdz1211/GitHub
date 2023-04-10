//Programa: Determinar si una matriz es una matriz simetrica.

#include <iostream>

using namespace std;

int main() {
	int n,m;
	
	cout << "Give the dimension of the matrix: "; cin >> n >> m;
	
	int A[n][m], trans[m][n];
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cout << "Give the element: (" << i << "," << j << "): ";
			cin >> A[i][j];
		}
	}

	int k=0;
	
	if(n==m){
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(A[i][j]!=A[j][i]){
					k = -1;
					break;
				}
			}
		}		
	}else{
		k = -1;
	}
	
	if(k==0){
		cout << "This matrix is simetric: " << endl;
	}else {
		cout << "This matrix is not simetric: " << endl;
	}
	
	for(int i=0; i<n; i++){
		cout << "[";
		for(int j=0; j<m; j++){
			cout << " " << A[i][j];
		}
		cout << "]" << endl;
	}
	
	return 0;
}
