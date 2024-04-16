#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //check if we got argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1]; //encoding key
    int keyLenght = strlen(key); //getting key lenght
    //checking if lenght of argument is 26 characters
    if (keyLenght != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    //checking for duplicates in key
    //take each letter, check if it is alpha and compare it to others
    for (int i = 0; i < keyLenght; i++)
    {
        if (!isalpha(key[i]))
        {
            return 1;
        }
        for (int j = i + 1; j < keyLenght; j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                return 1;
            }
        }
    }


    //Get input from user
    string input = get_string("plaintext:  ");
    //for every character in the massage
    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]))
        {
            if (isupper(input[i]))
            {
                int index = input[i] - 'A'; //if the letter if uppercase subtract 65 to get number in range 0-25
                input[i] = toupper(key[index]); //replacing letter in plaintext
            }
            else
            {
                int index = input[i] - 'a'; //if the letter if lowercase subtract 97 to get number in range 0-25
                input[i] = tolower(key[index]); //replacing letter in plaintext
            }
        }
    }
    printf("ciphertext: %s\n", input);
    return 0;
}
