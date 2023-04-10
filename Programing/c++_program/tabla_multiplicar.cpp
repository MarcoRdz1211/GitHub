//Programa: Tablas de multiplicar entre 1 y 10.

#include <iostream>

using namespace std;

int main(){
	int n;
	
	do{
		cout << "Dar un numero entre 1 y 10: "; cin >> n;
	} while(n<1 || n>10);
	
	for(int i=1; i<=10; i++){
		cout << n << "x" << i << " = " << n*i << endl;
	}
		
	return 0;
}
