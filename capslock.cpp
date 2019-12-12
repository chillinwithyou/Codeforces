#include <iostream>
#include <cstdio>

using namespace std;

int setLength(string s){
    int length = 0;

    char c = s[length];

    while(c){
        length++;
        c = s[length];
    }
    return length;
}

int main()
{

    string word;

    cin >> word;

    int length = setLength(word);
    int counter = 0;

    int i = 0;
    for(i=0; i<length; i++){
        if(isupper(word[i])){
            counter++;
        }
    }
    if(counter==length){
        for(i=0; i<length; i++){
            word[i] = tolower(word[i]);
        }
    }else if(counter == length-1 && islower(word[0])){
        word[0] = toupper(word[0]);
        for(i=1; i<length; i++){
            word[i] = tolower(word[i]);
        }
    }
    cout << word << endl;

    return 0;
}
