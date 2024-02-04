#include<iostream>
using namespace std;

struct array{
    int A[10];
    int size;
    int length;
};

void missing(struct array arr){
    int diff=arr.A[0]-0;
    for(int i=0;i<arr.length;i++){
        if(arr.A[i]-i!=diff){
            while(diff<arr.A[i]-i){
                cout<<i+diff;
                diff++;
            }
        }
    }
}

int main(){
    struct array arr1 ={{1,2,4,5,7},10,5};
    missing(arr1);
}
