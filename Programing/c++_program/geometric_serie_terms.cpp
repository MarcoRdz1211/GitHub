//Program: Dado un numero base, determinar la suma de su serie geometrica hasta un valor dado.

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int a,n;
	long long sum;
	
	cout << "Give the base and the last term of geometric serie: "; cin >> a >> n;
	
	sum = 0;
	
	for(int i=1; i<=n; i++){
		sum += pow(a,i);
	}
	
	cout << "The sum of the first " << n << " terms in the geometric serie of " << a << " is: " << sum;
	
	return 0;
}
