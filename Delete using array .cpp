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


int deleteEle(struct array *arr,int index){
    int x=0;
    int i;
    if(index>=0 && index<arr->length){
        x=arr->A[index];
        for(i=index;i<arr->length-1;i++){
            arr->A[i] = arr->A[i+1];
        }
        arr->length--;
        return x;
    }
    return 0;
}

int main()
{
    struct array arr1 =  {{2,3,4,5,6},10,5};
    cout<<deleteEle(&arr1,4);
    display(arr1);

    return 0;
}
