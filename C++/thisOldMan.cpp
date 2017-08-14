//"This Old Man"
//Homework Week 1

#include <iostream>
#include <string>

using namespace std;

void thisOldMan(int verse);
void clearScreen();

int main()
{
	const int NUMBER_VERSE = 9;
	for (int i = 0; i <= NUMBER_VERSE; i++)
	{	
		//clearScreen();
		thisOldMan(i);
		if (i < NUMBER_VERSE)
		{
			cout << "\nPress ENTER for the next verse." << endl;
			cin.get();
		}
		else
		{
			cout << "\nThat was the last verse. Thanks for singing along." << endl;
			cin.get();
		}
	}
	return 0;
}

void thisOldMan(int verse)
{
	string lyrics[] =
	{
		"on my drum;",
		"on my shoe;",
		"on my tree;",
		"on my door;",
		"on my hive;",
		"on my sticks;",
		"up in heaven;",
		"on my gate;",
		"on my spine;",
		"on my hen;"
	};

	const int SKIP_ZERO = 1;
	cout << "This old man, he played " << verse + SKIP_ZERO<< ".\n" <<
			"He played nick-nack " << lyrics[verse] << "\n" <<
			"With a nick-nack paddy-whack, give a dog a bone,\n" <<
			"This old man came running home." << endl;
}

void clearScreen()
{
	cout << string(100, '\n');
}