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
with open('Arcane-transcript-104-Happy-Progress-Day.txt', 'r', encoding='utf-8') as EpisodeOne:
    EpOneLines = EpisodeOne.readlines()
    JinxEpOne = []
    IsJinxLine = False
    for line in EpOneLines:
        if line.strip().startswith("[") and "-[Jinx]" in line:
            IsJinxLine = True
            JinxLine = line.strip()
        elif IsJinxLine and line.strip():
            JinxEpOne.append(JinxLine)
            IsJinxLine = False
    for JinxLine in JinxEpOne:
        JinxEpOne.append(JinxLine)

print(JinxEpOne)
