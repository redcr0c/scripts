#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;  
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int a,b;
        cin >> a >> b;
        
        int n;  // Maximum number of guesses
        cin >> n;
        
        int low = a + 1;  // +1 because A is inclusive
        int high = b;
        
        while (true) {
            // Binary search
            int mid = (low + high) / 2;
            cout << mid << endl;
            cout.flush();
            
            string response;
            cin >> response;
            
            if (response == "CORRECT") {
                break;
            } else if (response == "TOO_SMALL") {
                low = mid + 1;  // Number is larger than mid
            } else if (response == "TOO_BIG") {
                high = mid - 1;  // Number is smaller than mid
            } else if (response == "WRONG_ANSWER") {
                return 1;
            }
        }
    }
    
    return 0;
}
