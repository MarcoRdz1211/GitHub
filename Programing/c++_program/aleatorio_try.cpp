//Programa: Adivinar un numero random y dar la cantidad de interntos.

#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() {
	int n,valor,intentos=1;
	
	srand(time(NULL));
	valor = 1+rand()%100;
	
	cout << "Dar un numero: "; cin >> n;
	
	do{
		intentos += 1;
		if(n>valor){
			cout << "Dar un numero menor: "; cin >> n;
		}
		else{
			cout << "Dar un numero mayor: "; cin >> n;
		}
	}while(n!=valor);
	
	cout << "Valor: " << valor << " - Intentos: " << intentos;
	
	return 0;
}
