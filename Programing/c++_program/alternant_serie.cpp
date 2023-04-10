//Programa: serie alternante desde 1 hasta un valor dado.

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n,sum,c;
	
	cout << "Until what number do you want to calculate the alternant serie? "; cin >> n;
	
	sum = 0;
	c = -1;
	
	for(int i=1; i<=n; i++){
		sum -= i*c;
		c *= -1;
	}
	
	cout << "The sum of the alternant serie from 1 to " << n << " is: " << sum;
	
	return 0;
}

