# START
# ----- USER INPUT -----
# Get the users card information to be converted to binary
cardRank = input(str('Input the Card Rank: '))
cardSuit = input(str('Input the Card Suit: '))
cardColor = input(str('Input the Card Color: '))

# Convert all of their answers to an easy lowercase variable
cardRank = cardRank.lower()
cardSuit = cardSuit.lower()
cardColor = cardColor.lower()

# ----- VARIABLES -----
# Set all our variables before we start the program
# 'rank' sets the predefined variables to compare to
rank = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
# 'rankCode' sets the predefinced variables that we change to
rankCode = ['0000','0001','0010','0100','1000','1001','1010','1100','1101','1110','1111','0110','0101']
# 'suit' sets the predefinced variables to compare to
suit = ['spades','clubs','hearts','diamonds']
# 'suiteCode' sets the predefinced variables that we change to
suitCode = ['00','01','10','11']
# 'countVar' is our counter variable in the FOR LOOP
countVar = 0
# These preset the final variables as empty
rankBinary = ""
suitBinary = ""

# ----- COLOR -----
# This sets the color of our card to a 1 bit binary code
if cardColor == 'red':
    cardColor = 1
elif cardColor == 'black':
    cardColor = 0

# ----- RANK ------
# This sets the rank of our card to a 4 bit binary code
for x in rank:
    if str(cardRank) == str(x):
        rankBinary = rankCode[countVar]
    countVar = countVar + 1

# ----- SUIT -----
# This sets the rank of our card to a 2 bit binary code
countVar = 0
for x in suit:
    if str(cardSuit) == str(x):
        suitBinary = suitCode[countVar]
    countVar = countVar + 1

# ----- OUTPUT -----
# Once all is done, print out the converted card in binary code
print(str(rankBinary)+str(suitBinary)+str(cardColor))
# END

# ---------- DISCUSSION ----------
# I chose variable length as it was easier to set up and had predictable patterns.
# Fixed length can be less compressed than variable encoding although variable
# encoding can introduce errors and complexity.