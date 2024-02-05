#include<iostream>
using namespace std;

int main() {
    char A[] = "python";
    int i, j;
    char t;
    
    // Find the length of the string
    for (j = 0; A[j] != '\0'; j++) {}
    
    j = j - 1; // Adjusting j to point to the last valid character

    // Swap characters to reverse the string
    for (i = 0; i < j; i++, j--) {
        t = A[i];
        A[i] = A[j];
        A[j] = t;
    }
    
    cout << A; // Output the reversed string
    return 0;
}
