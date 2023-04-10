//Programa: Suma de enteros entre 1 y n.

#include <iostream>

using namespace std;

int main() {
	int n,sum;
	
	cout << "Until what number is the sum? "; cin >> n;
	
	sum = 0;
	
	for(int i=1; i<=n; i++){
		sum += i;
	}
	
	cout << "The sum from 1 to " << n << " is: " << sum << endl;
	
	return 0;
}
