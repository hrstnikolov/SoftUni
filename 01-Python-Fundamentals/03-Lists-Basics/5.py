# input
deck = input().split()
number_of_shuffles = int(input())

middle_index = len(deck) // 2
shuffled_deck = []
for shuffle in range(number_of_shuffles):

    # shuffling without first and last card
    shuffled_deck = []
    for i in range(1, middle_index):

        # appending cards by farro shuffling
        shuffled_deck.append(deck[i + middle_index])
        shuffled_deck.append(deck[i])

# appending first and last cards
shuffled_deck.insert(0, deck[0])
shuffled_deck.append(deck[-1])

# printing output
print(shuffled_deck)

