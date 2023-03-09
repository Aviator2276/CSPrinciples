cardRank = input(str("Input the Card Rank: "))
cardSuit = input(str("Input the Card Suit: "))
cardColor = input(str("Input the Card Color: "))

cardColor = cardColor.lower()

if cardColor == "red":
    cardColor = 1
elif cardColor == "black":
    cardColor = 0
print(str(cardColor))
print("Hello World")
    