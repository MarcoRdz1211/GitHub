//Programa: Calcular la descomposición de un numero en sus factores primos.

#include <iostream>

using namespace std;

int main() {
	int n;
	
	cout << "Give me a integer: "; cin >> n;
	
	int i = 2;
	
	cout << n << "=";
	
	do{
		if(n%i==0){
			n /= i;
			cout << "(" << i << ")";
		}
		else{
			i += 1;
		}
	}while(n!=1);
	
	return 0;
}
