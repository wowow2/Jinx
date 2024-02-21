'''
while True:
    FavChar = input("Who is your fav Arcane character?")
    FavChar = FavChar.upper()
    if FavChar == "JINX":
        print("That's mine too")
        break
    elif FavChar == "CAITLYN" or FavChar == "VI":
        print("Solid choice! ")
        break
    else:
        print("Nice!")
        break

#meow test test #2

#meow test test #3

#meow test test #4
'''

# Starting the code
with open('Arcane-transcript-104-Happy-Progress-Day.txt', 'r') as EpisodeOne:
  EpOneLines = EpisodeOne.readlines()
  JinxEpOne = []
  for EpisodeOne in EpOneLines:
    Line = BLANK.strip().split(",")#for here code to make lines that dont start with jinx go away
    JinxEpOne.append(Line)