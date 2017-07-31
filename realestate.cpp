#include <iostream>
#include <string>

using namespace std;

bool checkVowel(char letter)
{
    if (letter == 'a' ||
        letter == 'e' ||
        letter == 'i' ||
        letter == 'o' ||
        letter == 'u')
        return true;
    else
        return false;
}

/*
void removeVowels(char *letter)
{
    char alpha;
    char previous = ' ';
    bool stringDone = false;
    
    do
    {
        alpha = *letter;
        bool isVowel = checkVowel(alpha);
    
        if (*letter = '\0')
            stringDone = true;
        else if (previous == ' ')
            cout << alpha;
        else if (isVowel == true);
        else 
            cout << alpha;
        previous = alpha;
        alpha++;
    }while (stringDone == false);
}
*/

int main()
{
    string entry;
    cout << "Please enter line to be converted." << endl;
    getline(cin, entry);
  
    //removeVowels(&entry[0]);
    

    int index = 0;
    
    char previous = ' ';
    
    do 
    {
        char letter = entry[index];
        bool isVowel = checkVowel(letter);
        
        if (previous == ' ')
            cout << letter;
        else if (isVowel == true);
        else 
            cout << letter;
        
        previous = letter;
        index++;
    }while (entry[index] != '\0');
    
    /*
    do
    {
        char vowelCheck = entry[index]
        char previous; 
        if (entry[index] == 'a' ||
            entry[index] == 'e' ||
            entry[index] == 'o' ||
            entry[index] == 'i' ||
            entry[index] == 'u');
        else if (entry[index] == ' ')
            index++;
            cout << entry[index];
        
        index++;
    }while (entry[index] != '\0');
    */
}