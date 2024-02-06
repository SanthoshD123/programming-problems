#include<iostream>
using namespace std;

int main(){
    char A[]="decimal";
    char B[]="medical";
    int i,H[26]={0};
    
    for(i=0;A[i]!='\0';i++){
        H[A[i]-'a']+=1;
    }
    for(i=0;B[i]!='\0';i++){
        H[B[i]-'a']-=1;
        if(H[B[i]-'a']<0){
            cout<<"Not an anagram";
            return 0;
        }
    }
    if(B[i]=='\0'){
        cout<<"Yep, it's an Anagram";
    }
    return 0;
}
