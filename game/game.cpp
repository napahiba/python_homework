#include <iostream>
#include <string>

using namespace std;

class Player
{
    private:
        string mName;
    public:
        Player()
        {
            setName();
        }
    
        void setName()
        {
            cout << "What is your name?" << endl;
            string name;
            cin >> name;
            
            mName = name;
        }
        
        void getName()
        {
            cout << "Name:\t" << mName << endl;
        }
};




int main()
{
    Player player;
    player.getName();
    
}