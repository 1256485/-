#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() 
{
    int boys = 0;
    int girls = 0;
    srand(time(NULL));
    for (int i = 0; i < 1000000; i++) 
    {
        while (true) 
        {
            string child = (rand() % 2 == 0) ? "boy" : "girl";
            if (child == "boy") 
            {
                boys++;
                break;
            } else 
            {
                girls++;
                if (boys + girls == 1000000) 
                {
                    break;
                }
            }
        }
    }
    cout << "Final male to female ratio: " << (double)boys/girls << endl;
    return 0;
}
