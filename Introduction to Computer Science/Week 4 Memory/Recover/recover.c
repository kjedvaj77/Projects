#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;


int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }

    // Open disk image
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }


    BYTE buffer[512];
    int counter = 0;
    char filename[9];
    FILE *img = NULL;

    while (fread(buffer, sizeof(BYTE), sizeof(buffer), input) == 512)
    {
        // Find jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer [2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If not first jpeg then close old and open new one
            if (img != NULL)
            {
                fclose(img);
            }
            // if found jpeg give it a name and open it
            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");
            counter++;
        }
        // If image is opened write to file
        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE), sizeof(buffer), img);
        }
    }
    // Close both files
    fclose(img);
    fclose(input);
    return 0;
}