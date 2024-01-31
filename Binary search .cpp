#include<iostream>
#include<stdlib.h>
using namespace std;

struct array{
    int A[10];
    int size;
    int length;
};

void display(struct array arr){
    cout<<"\nElements are: \n";
    for(int i=0;i<arr.length;i++){
        cout<<arr.A[i];
    }
}

int binarySearch(struct array arr,int key){
    int l,mid,h;
    l=0;
    h=arr.length-1;
    
    while(l<=h){
        mid=(l+h)/2;
        if(key==arr.A[mid]){
            return mid;
        }
        else if(key<arr.A[mid]){
            h=mid-1;
        }
        else{
            l=mid+1;
        }
    }
    return -1;
    
}

int main(){
    struct array arr1 = {{2,3,4,5,6},10,5};
    cout<<binarySearch(arr1,5);
    display(arr1);
    
    return 0;
}
