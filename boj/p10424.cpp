#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n, h;
    cin >> n >> h;
    int top[n/2];
    int bottom[n/2];
    int rb, rt; rb = rt = 0;
    int m = 200001;
    int c, r; c = r = 0;

    for (int i=0; i < n/2; i++){
        // cin >> top[i];
        // cin >> bottom[i];
        top[i] = i+1;
        bottom[i] = i+1;
    }

    sort(top, top+n/2);
    sort(bottom, bottom+n/2);

    for (int i=0; i<h; i++){
        r = rt;
        for (int e=rb; e<n/2; e++)
            if (bottom[e] >= i+1){
                if (bottom[e] == i+1)
                    rb = e;
                r++;
            }
        for (int e=rt; e<n/2; e++)
            if (h-top[e] < i+1) r++;
            else rt = e;
        if (m > r){
            m = r;
            c = 1;
            continue;
        } else if (m == r)
            c++;
    }

    cout << m  << ' ' << c << endl;
}
