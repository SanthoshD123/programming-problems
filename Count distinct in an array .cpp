#include<iostream>
using namespace std;

int countD(int arr[],int n){
    int count = 0;
    bool isD = true;
    for(int i=0;i<n;i++){
        isD = true;
        for(int j=i-1;j>=0;j--){
            if(arr[i] == arr[j]){
                isD = false;
                break;
            }
        }
        if(isD==true){
            count++;
        }
    }
    return count;
}

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<countD(arr,n);
    return 0;
}
