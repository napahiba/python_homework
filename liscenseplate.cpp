#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int randomDigit()
{
    int digit = rand() % 100 + 0;
    return digit % 10;
}

char randomLetter()
{
    char letter = rand() % 26 + 0;
    letter = letter + 65;
    return letter;
}

void licensePlate()
{
    const int DIGITS = 3;
    const int ALPHAS = 3;
    
    for (int i = 0; i < DIGITS; i++)
    {
        int number = 0;
        do
        {
            number = randomDigit();
            
        }while(number == 0);
        
        cout << number;
    }
    
    cout << " ";
    
    for (int j = 0; j < ALPHAS; j++)
        cout << randomLetter();
    
    cout << endl;
}

int main()
{
    srand((unsigned)(time(0)));
    //for (int i = 0; i < 20; i++)
    licensePlate();
}