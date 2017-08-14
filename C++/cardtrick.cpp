#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

enum suits { CLUBS, DIAMONDS, HEARTS, SPADES };
enum ranks { DEUCE, TREY, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING };

int getSuit();
int getRank();
void getCard(int *cardSuit, int *cardRank);


int main()
{
    string suitsArr[] = { "Clubs", "Diamonds", "Hearts", "Spades" };
    string ranksArr[] = { "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K" };
    
    const int NUMBER_OF_CARDS = 4;
    const int SUIT_AND_RANK = 2;
    int cardsArr[NUMBER_OF_CARDS][SUIT_AND_RANK];
    
    getCard(&cardsArr[0][0], &cardsArr[0][1]);
    
    cout << "Card #1: " << suitsArr[cardsArr[0][0]] << ranksArr[cardsArr[0][1]] << endl;
    
}

suits getSuit()
{
    char chooseSuit = 'C';
    bool goodSuit = false;
    
    cout << "Please choose a suit.\n" <<
            "C - Clubs\n" <<
            "D - Diamonds\n" <<
            "H - Hearts\n" <<
            "S - Spades" << endl;
    
    cin >> chooseSuit;
    chooseSuit = toupper(chooseSuit);
    
    do
    {
        switch(chooseSuit)
        {
            case 'C':
                goodSuit = true;
                return 0;
                break;
            case 'D':
                goodSuit = true;
                return 1;
                break;
            case 'H':
                goodSuit = true;
                return 2;
                break;
            case 'S':
                goodSuit = true;
                return 3;
                break;
            default:
                cout << "That option is not valid.\n" <<
                        "Please choose a suit.\n" <<
                        "C - Clubs\n" <<
                        "D - Diamonds\n" <<
                        "H - Hearts\n" <<
                        "S - Spades" << endl;
                cin >> chooseSuit;
                chooseSuit = toupper(chooseSuit);
        }
    }while (goodSuit == false);
}

int getRank()
{
    char chooseRank = '2';
    bool goodRank = false;
    
    cout << "Please choose a rank.\n" <<
            "2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A" << endl;
    cin >> chooseRank;
    chooseRank = toupper(chooseRank);
    
    do
    {
        switch(chooseRank)
        {
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
            {
                goodRank = true;
                char convertRank[10] = {chooseRank};
                return atoi(convertRank);
                break;
            }
            
            case 'T':
            {
                return 10;
                break;
            }
            case 'J':
            {
                return 11;
                break;
            }
            case 'Q':
            {
                return 12;
                break;
            }
            case 'K':
            {
                return 13;
                break;
            }
            default:
            {
                cout << "That option was not valid.\n" <<
                        "Please choose a rank.\n" <<
                        "2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A" << endl;
                cin >> chooseRank;
                chooseRank = toupper(chooseRank);  
            }   
        }
    }while(goodRank == false);
}

void getCard(int *cardSuit, int *cardRank)
{
    *cardSuit = getSuit();
    *cardRank = getRank();
}