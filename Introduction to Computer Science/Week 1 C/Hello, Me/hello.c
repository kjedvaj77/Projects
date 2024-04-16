#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //There is no requirement for comments on this code
    string name = get_string("Whats your name? ");
    printf("Hello %s\n", name);
}