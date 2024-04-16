#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int output = 0;
    int number;
    for (int i = 0; i < strlen(word); i++) //for each character in word
    {
        if (isupper(word[i]))
        {
            number = word[i] - 65; //ASCII value of uppercase character - 65 to get number 0 - 25
            number = POINTS[number]; //getting value from array
        }
        else if (islower(word[i]))
        {
            number = word[i] - 97; //ASCII value of lowercase character - 97 to get number 0 - 25
            number = POINTS[number]; //getting value from array
        }
        else //if character is not a letter, dont add any value
        {
            number = 0;
        }
        output += number;
    }
    return output; //returns score of a player
}
