// Creating score variables
let numScore1 = 0;
let numScore2 = 0;
// Select main button
let mainButton = document.querySelector('#main-button');
// Get onclick event
mainButton.addEventListener('click', () => {
    // alert(1)
    // Generate number from 1-6 for first player
    let randomNumber1 = Math.floor(Math.random() * 6) + 1;
    // Get new image for first player
    let player1 = "images/dice" + randomNumber1 + ".png";
    // Generate number from 1-6 for second player
    let randomNumber2 = Math.floor(Math.random() * 6) + 1;
    // Get new image for second player
    let player2 = "images/dice" + randomNumber2 + ".png";
    // Select all images and change their images
    let image1 = document.querySelector('#diceImage1');
    let image2 = document.querySelector('#diceImage2');
    image1.setAttribute("src", player1);
    image2.setAttribute("src", player2);
    //  Selecting table data and creating score variables
    let score1 = document.querySelector('#score1');
    let score2 = document.querySelector('#score2');
    // Select h1 tag and change his inner html
    let mainTag = document.querySelector('h1');
    if (player1 > player2){
        mainTag.innerHTML = 'Player 1 Wins!';
        numScore1++;
        score1.innerHTML = numScore1;
    } else if (player1 < player2) {
        mainTag.innerHTML = 'Player 2 Wins!';
        numScore2++;
        score2.innerHTML = numScore2;
    } else {
        mainTag.innerHTML = 'Tie !';
    }
});