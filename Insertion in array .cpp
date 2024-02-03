#include<iostream>
using namespace std;

struct array{
    int A[10];
    int size;
    int length;
};

void display(struct array arr){
    int i;
    for(i=0;i<arr.length;i++){
        cout<<arr.A[i]<<" ";
    }
    cout<<endl;
}

void insert(struct array *arr,int x){
    int i=arr->length-1;
    if(arr->length==arr->size){
        return;
    }
    while(i>=0 && arr->A[i]>x){
        arr->A[i+1]=arr->A[i];
        i--;
    }
    arr->A[i+1]=x;
    arr->length++;
}

int main(){
    struct array arr1 = {{1,2,3,4,5,7},10,6};
    insert(&arr1,6);
    display(arr1);
    return 0;
}
