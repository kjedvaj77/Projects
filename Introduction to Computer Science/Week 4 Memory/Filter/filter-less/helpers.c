#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    //sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    //sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    int red, green, blue;
    int sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // reading image colors
            red = image[i][j].rgbtRed;
            green = image[i][j].rgbtGreen;
            blue = image[i][j].rgbtBlue;
            // convert to sepia
            sepiaRed = round((0.393 * red + 0.769 * green + 0.189 * blue));
            sepiaGreen = round((0.349 * red + 0.686 * green + 0.168 * blue));
            sepiaBlue = round((0.272 * red + 0.534 * green + 0.131 * blue));

            //
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }


            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }


            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // write new pixel
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int midpoint = width / 2;
    RGBTRIPLE temp;
    /*
    Iterate through the midpoint of the picture and transfer
    pixels from the first half to the other.
    */
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < midpoint; j++)
        {
            // A copy of the last pixel of image
            temp = image[i][(width - 1) - j];
            // Take the last pixel in the image and swap it with the first one
            image[i][(width - 1) - j] = image[i][j];
            // Swap first pixel too
            image[i][j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    // Make copy of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtBlue = image [i][j].rgbtBlue;
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0;
            int totalGreen = 0;
            int totalBlue = 0;
            int avg = 0;
            int counter = 0; // Count how many pixels we took a value of
            // first pixel
            // iterate through surrounding pixels
            for (int x = - 1; x < 2; x++)
            {
                if (i - x >= 0 && i - x < height)
                {
                    for (int z = -1; z < 2; z++)
                    {
                        // if pixel exists
                        if (j - z >= 0 && j - z < width)
                        {
                            totalRed += copy[i - x][j - z].rgbtRed;
                            totalGreen += copy[i - x][j - z].rgbtGreen;
                            totalBlue += copy[i - x][j - z].rgbtBlue;
                            counter++;
                        }
                    }
                }
            }
            // take average
            totalRed = round(totalRed / (float)counter);
            totalGreen = round(totalGreen / (float)counter);
            totalBlue = round(totalBlue / (float)counter);
            // save pixel to image
            image[i][j].rgbtRed = totalRed;
            image[i][j].rgbtGreen = totalGreen;
            image[i][j].rgbtBlue = totalBlue;

        }
    }
    return;
}
