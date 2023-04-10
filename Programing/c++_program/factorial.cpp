//Programa: Dado un numero, calcular su factorial.

#include <iostream>

using namespace std;

int main() {
	int n,fac;
	
	cout << "What factorial do you want? "; cin >> n;
	
	fac = 1;
	
	for(int i=2; i<=n; i++){
		fac *= i;
	}
	
	cout << n << "! = " << fac;
	
	return 0;
}
