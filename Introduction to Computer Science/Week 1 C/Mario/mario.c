#include <cs50.h>
#include <stdio.h>

void Hashes(int n);

int main(void)
{
    //getting user input ranging from 1-8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    int space = height - 1;
    //calculate and print output
    for (int row = 0; row < height; row++) //for each row
    {
        //print spaces
        for (int l = 0; l < space; l++)
        {
            printf(" ");
        }
        //print left hashes
        Hashes(row);
        //print space in the middle
        printf("  ");
        //print right hashes
        Hashes(row);
        printf("\n");
        space--;
    }
}
//creating function that prints hashes
void Hashes(int n)
{
    for (int j = 0; j < n + 1; j++) //for each row print n hashes
    {
        printf("#");
    }
}