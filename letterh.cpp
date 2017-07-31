//the letter H

#include <iostream>

using namespace std;

int getSize();
void makeH(int size);

int main()
{
   int size;
   size = getSize();
   
   cin.get();
   
   makeH(size);
   
   cin.get();
   
   return 0;
}

int getSize()
{
    int size;
    const int MAX = 10;
    const int MIN = 1;
    
    do
    {
        cout << "Please enter a size betwen 1 and 10." << endl;
        cin >> size;
    }while (size < MIN || size > MAX);
    
    return size;
}

void makeH(int size)
{
   const int COLUMN = 3;
   const int ROW = 3;
   
   for (int i = 0; i < ROW; i++)
   {
       for (int j = 0; j < size; j ++)
       {
           for (int k = 0; k < COLUMN; k++)
           {
               for (int l = 0; l < size; l++)
               {
                   if (i == 0 || i == 2)
                   {
                        if (k == 0 || k == 2)
                            cout << "*";
                        else
                            cout << " ";
                   }
                   
                   else
                        cout << "*";
               }
              
           }
           cout << endl;
       }
   }
}