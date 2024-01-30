#include <iostream>
using namespace std;

struct array{
    int A[10];
    int size;
    int length;
};

void display(struct array arr){
    int i;
    cout<<"\nElement are\n";
    for(i=0;i<arr.length;i++){
        cout<<arr.A[i];
    }
}

void insert(struct array *arr,int index,int x){
    int i;
    if(index>=0 && index<=arr->length){
        for(i=arr->length;i>index;i--){
            arr->A[i]=arr->A[i-1];
        }
        arr->A[index]=x;
        arr->length++;
    }
    
}

void append(struct array *arr, int x){
    if(arr->length<arr->size){
        arr->A[arr->length++]=x;
    }
}

int main()
{
    struct array arr1 =  {{2,3,4,5,6},10,5};
    append(&arr1,10);
    insert(&arr1,0,1);
    display(arr1);

    return 0;
}
