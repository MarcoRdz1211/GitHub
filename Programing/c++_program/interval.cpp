//Programa: Determinar si un dato esta en un intervalo dado.

#include <iostream>

using namespace std;

int main(){
	int a,b,x;
	
	cout << "Give the interval. "; cin >> a >> b;
	cout << "Give a data. "; cin >> x;
	
	if(x>=a && x<=b){
		cout << "The number is between " << a << " & " << b;
	}
	else{
		cout << "The number is not between " << a << " & " << b;
	}	
	
	return 0;
}
