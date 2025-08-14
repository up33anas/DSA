#include <iostream>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        if(l1 == 0 && l2 == 0) return "";
        if(l1 == 0 || l2 == 0) {
            string arr[2];
            arr[0] = word1;
            arr[1] = word2;
            for(int i = 0; i < 2; i++) 
                if(arr[i].length() > 0) return arr[i];
        }
        string result;
        if(l1 == l2) {
            for(int i=0; i<l1; i++) {
                result.push_back(word1[i]);
                result.push_back(word2[i]);
            }
        } else if(l1 < l2) {
            for(int i=0; i<l1; i++) {
                result.push_back(word1[i]);
                result.push_back(word2[i]);
            }
            for(int i=l1; i<l2; i++) {
                result.push_back(word2[i]);
            }
        }
        else {
            for(int i=0; i<l2; i++) {
                result.push_back(word1[i]);
                result.push_back(word2[i]);
            }
            for(int i=l2; i<l1; i++) {
                result.push_back(word1[i]);
            }
        }
        return result;
    }
};

int main() {

    Solution s1;
    string word1, word2;

    cout << "Enter Word1: ";
    cin >> word1;
    cout << "Enter Word2: ";
    cin >> word2;

    cout << "Mixed words: " << s1.mergeAlternately(word1, word2) << endl;

    return 0;
}