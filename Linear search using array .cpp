//move to head method(fast approach)
#include <stdio.h>
#include <iostream>
using namespace std;

struct array{
    int A[10];
    int size;
    int length;
};

void display (struct array arr){
    cout<<"\nthe elements:\n";
    for(int i=0;i<arr.length;i++){
        cout<<arr.A[i];
        
    }
    cout<<"\n";
}

void swap(int *x, int *y){
    int temp=*x;
    *x=*y;
    *y=temp;
}

int linearSearch(struct array *arr,int key){
    for(int i=0;i<arr->length;i++){
        if(key==arr->A[i]){
            swap(&arr->A[i],&arr->A[0]);//instead of A[0] ,you can use A[i-1] for transposition method 
            return i;
        }
    }
    return -1;
}

int main()
{
    struct array arr1 = {{2,3,4,5,6},10,5};
    cout<<linearSearch(&arr1,3);
    display(arr1);

    return 0;
}
