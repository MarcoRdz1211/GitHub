//Programa: Serie de Fibonacci:

#include <iostream>

using namespace std;

int main() {
	int pre,next,n,aux;
	
	cout << "Until what term do you want to obtain the Fibonacci Serie? "; cin >> n;
	
	pre = 1; next = 1; aux = pre;
	
	cout << "Term 1: " << pre << endl;
	
	for(int i=2; i<=n; i++){
		pre = next; next += aux; aux = pre;
		cout << "Term " << i << ": " << next << endl;
	}
	
	return 0;
}
