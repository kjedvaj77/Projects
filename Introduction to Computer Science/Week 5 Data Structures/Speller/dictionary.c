// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 2600; //2704

// Hash table
node *table[N];

// Word counter
int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    if (table[index] == NULL)
    {
        return false;
    }
    node *n = NULL;
    n = table[index];
    // Loop over linked list if we find word return true
    while (n != NULL)
    {
        if (strcasecmp(n->word, word) == 0)
        {
            return true;
        }
        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isalpha(word[i]))
        {
            sum += tolower(word[i]);
        }
    }
    return (sum * 52) % (N + 1);
    // return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open file
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        return false;
    }
    // Add words to memory
    char wrd[LENGTH + 1];
    while (fscanf(input, "%s", wrd) != EOF)
    {
        // Create new node
        node *n = malloc(sizeof(node));
        n->next = NULL;
        if (n == NULL)
        {
            return false;
        }
        // Copy word to node
        strcpy(n->word, wrd);
        // Hash index
        int index = hash(wrd);
        // Put node in table
        if (table[index] != NULL)
        {
            n->next = table[index];
            table[index] = n;
        }
        else
        {
            //n->next = NULL;
            table[index] = n;
        }
        counter++;
    }
    fclose(input);
    // Malloc empty buckets
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *n = NULL;
        while (table[i] != NULL)
        {
            n = table[i]->next;
            free(table[i]);
            table[i] = n;
        }
    }
    return true;
}
