#include <iostream> 
#include <algorithm> 
using namespace std; 

int main(void) { 
	int N;
	 
	cin >> N;
	 
	long long * A = new long long [N]; 
	
	for (int i = 0; i < N; i++) 
		cin >> A[i]; 
	
	sort(A, A + N); 
	
	int answer = 1;
	
	for (int i = 0; i < N; i++) { 
		if (answer != A[i]) 
			break;
			
		for (int j = i + 1; j < N; j++) { 
			if (A[i] == A[j]) 
				i = j; 
			else 
				break; 
			} 
			answer++; 
	} 
	cout << answer; 
	delete[] A; 
}
