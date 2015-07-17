#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n;
    cin >> n;
    int arr[n];
    int store[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
     }
    for(int i=0; i<n; i++){
        store[arr[i]-1] = arr[i] - (i+1);
    }
    for(int i=0; i<n; i++){
        cout << store[i] << endl;
    }
    return 0;
}
