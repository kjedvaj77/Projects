import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage python ./dna database sequence")

    # TODO: Read database file into a variable
    # db = list of dictionarys
    db = []
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        for person in reader:
            db.append(person)

    # TODO: Read DNA sequence file into a variable
    seq = str()
    with open(sys.argv[2], "r") as f:
        seq = f.read().strip()

    # TODO: Find longest match of each STR in DNA sequence
    # Get all sequences that we shoud look for
    seqences = []
    for key in db[0].keys():
        if key != "name":
            seqences.append(key)

    # Get longest match for each sequence in dict
    result = dict()
    for sequence in seqences:
        temp = longest_match(seq, sequence)
        result[sequence] = temp

    # TODO: Check database for matching profiles
    for person in db:
        count = 0
        for key in person.keys():
            if key != "name":
                if int(person[key]) == result[key]:
                    count += 1
        if count == len(seqences):
            print(person["name"])
            sys.exit(0)

    print("No match")
    sys.exit(0)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
