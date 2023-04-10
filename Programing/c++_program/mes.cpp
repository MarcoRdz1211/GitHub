//Programa: Dado un entero, determinar el dia del año correspondiente.

#include <iostream>

using namespace std;

int main(){
	int n,r,sum;
	int mes[11]={31,28,31,30,31,30,31,31,30,31,30};
	string meses[12]={"enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"};
	
	cout << "Dar un valor entre 1 y 365 "; cin >> n;
	r = 0;
	sum = 0;
	
	while(n>sum+mes[r]){
		sum += mes[r];
		r++;
	}
	
	// Metodo de stwitch:	
	switch(r){
		case 0: cout << "Es el dia: " << n-sum << " de enero" << endl; break;
		case 1: cout << "Es el dia: " << n-sum << " de febrero" << endl; break;
		case 2: cout << "Es el dia: " << n-sum << " de marzo" << endl; break;
		case 3: cout << "Es el dia: " << n-sum << " de abril" << endl; break;
		case 4: cout << "Es el dia: " << n-sum << " de mayo" << endl; break;
		case 5: cout << "Es el dia: " << n-sum << " de junio" << endl; break;
		case 6: cout << "Es el dia: " << n-sum << " de julio" << endl; break;
		case 7: cout << "Es el dia: " << n-sum << " de agosto" << endl; break;
		case 8: cout << "Es el dia: " << n-sum << " de septiembre" << endl; break;
		case 9: cout << "Es el dia: " << n-sum << " de octubre" << endl; break;
		case 10: cout << "Es el dia: " << n-sum << " de noviembre" << endl; break;
		case 11: cout << "Es el dia: " << n-sum << " de diciembre" << endl; break;
	}
	
	// Metodo de while:
	cout << "Es el dia: " << n-sum << " de " << meses[r];
	
	return 0;
}
