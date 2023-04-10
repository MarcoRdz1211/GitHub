//Programa: Pariedad de un numero

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n;
	
	cout << "Give a natural number: "; cin >> n;
	
	if(n%2==0){
		cout << "The number is even.";
	}
	else{
		cout << "The number is odd.";
	}
	
	if(n>=0){
		cout << "The number is positive.";
	}
	else{
		cout << "The number is negative.";
	}
	
	return 0;
}
