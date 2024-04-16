#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int letter, sentence;
int word = 1; // starts with 1 becouse of last word in the text

int main(void)
{
    //picking up text
    string text = get_string("Input: ");
    //lenght of text
    int txtlen = strlen(text);

    //analyse text with for loop
    for (int i = 0; i < txtlen; i++) //for each character in text
    {
        //counting alpha. chars
        if (isalpha(text[i]))
        {
            letter++;
        }
        //counting number of spaces +1
        if (i < txtlen - 1 && isspace(text[i]))
        {
            word++;
        }
        //counting how much punctions are in the text
        if (i > 0 && (text[i] == '!' || text[i] == '?' || text[i] == '.') && isalpha(text[i - 1]))
        {
            sentence++;
        }
    }
    //INDEX
    float L = (100 / (float) word) * letter;
    float S = (100 / (float) word) * sentence;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    //print text grade
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 0 && index < 16)
    {
        printf("Grade %d\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
    // CHECKPOINT
    // printf("%i %i %i\n", letter, word, sentence);
}