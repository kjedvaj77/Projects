def main():
    text = input("Text: ")
    letter = 0
    word = 0
    sentence = 0
    # For every char in text if alpha letter++ if space word++
    for c in text:
        if c.isalpha():
            letter += 1
        elif c == " ":
            word += 1
        elif c == "." or c == "!" or c == "?":
            sentence += 1
    # Word +1 because of last word in text
    word += 1
    """
    Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8,
    where L is the average number of letters per 100 words in the text, and S is the
    average number of sentences per 100 words in the text.
    """
    avg = 100 / float(word)
    L = avg * letter
    S = avg * sentence
    colemanLiau = round(0.0588 * L - 0.296 * S - 15.8)
    # print(L, S, colemanLiau)
    # print(letter, word, sentence)
    if colemanLiau < 1:
        print("Before Grade 1")
    elif colemanLiau > 0 and colemanLiau < 16:
        print(f"Grade {colemanLiau}")
    else:
        print("Grade 16+")


main()