#include <iostream>
using namespace std;

struct array {
    int A[10];
    int size;
    int length;
};

void missing(struct array arr) {
    int *h = new int[arr.size + 1]; // Initialize h array to count occurrences
    for (int i = 0; i < arr.size + 1; i++) {
        h[i] = 0; // Initialize to 0
    }
    for (int i = 0; i < arr.length; i++) {
        h[arr.A[i]]++;
    }
    for (int i = 1; i <= arr.size; i++) { // iterate from 1 to size
        if (h[i] == 0) {
            cout << i << " ";
        }
    }
    delete[] h; // Deallocate memory
}

int main() {
    struct array arr1 = { {2, 1, 1, 6, 1}, 5, 5 };
    missing(arr1);
    return 0;
}
