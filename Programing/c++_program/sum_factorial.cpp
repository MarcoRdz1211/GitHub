//Programa: Dado un numero, calcular su factorial.

#include <iostream>

using namespace std;

int main() {
	int n,fac,sum;
	
	cout << "Until what factorial do you want? "; cin >> n;
	
	sum = 0;
	
	for(int i=1; i<=n; i++){
		fac = 1;
		for(int j=2; j<=i; j++){
			fac *= j;
		}
		sum += fac;
	}
	
	cout << "The sum of factorials from 1 to " << n << " is: " << sum;
	
	return 0;
}
