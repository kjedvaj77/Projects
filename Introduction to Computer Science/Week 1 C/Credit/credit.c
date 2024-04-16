#include <stdio.h>
#include <cs50.h>

int sum = 0;
long input; //credit card number
long fs20 = 10;

int main(void)
{
    do
    {
        input = get_long("Number (CC): ");
    }
    while (input < 0);
    //input taken -> algoritam
//1.
    long tempcc = input; //make copy of credit card
    while (tempcc > 0)
    {
        int lastnum = tempcc % 10; //get last digit
        sum = sum + lastnum; //add to sum
        tempcc = tempcc / 100; //move on next digit
    }
// 2.
    tempcc = input / 10; //skip last digit and reasign tempcc
    while (tempcc > 0)
    {
        int lastnum = tempcc % 10; //get the last digit
        int make_it_double = lastnum * 2;
        sum = sum + (make_it_double % 10) + (make_it_double / 10); // adding result to sum
        tempcc = tempcc / 100; //move to next digit
    }

    //printf("sum: %i\n", sum);
    //Picking up lenght of card.
    int cclen;
    tempcc = input;
    while (tempcc > 0)
    {
        tempcc = tempcc / 10; //removing last digit
        cclen = cclen + 1;
    }

    //printf("credit card lenght %i\n", cclen);
    //getting devisor so i can get first 2 numbers of credit card
    for (int i = 0; i < cclen - 2; i++)
    {
        fs20 = fs20 * 10;
    }

    //printf("devisor: %li\n", fs20);
    //Getting first two numbers of credit card.
    int firstNum = input / fs20;
    int firstTwo = input / (fs20 / 10);
    /* output
    visa starts with 4 and has 13 or 16 digits
    amex starts with 34 and 37 and has 15 digits
    mastercard starts with 50-55  and has 16 digits
    */
    if (sum % 10 == 0)
    {
        if (firstNum == 4 && (cclen == 13 || cclen == 16)) //cclen = lenght of credit card number
        {
            printf("VISA\n");
        }
        else if ((firstTwo == 34 || firstTwo == 37) && cclen == 15)
        {
            printf("AMEX\n");
        }
        else if ((firstTwo == 50 || firstTwo == 51 || firstTwo == 52 || firstTwo == 53 || firstTwo == 54 || firstTwo == 55) && cclen == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
