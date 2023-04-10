//Programa: tipo de variable.

#include <iostream>
#include <math.h>
#include <typeinfo>

using namespace std;

int main(){
	long long n;
	
	cin >> n;
	
	while(n!=1){
		cout << n << " ";
/*		if(n==1){
			break;
		}*/
		if(n%2 == 0){
			n /= 2;
		}
		else{
			n = 3*n+1;
		}
	}
	
	return 0;
}
