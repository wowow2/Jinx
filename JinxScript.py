'''
title: Jinx Script
authors: Leigh and Abbas
date: 2024/02/21
Created a script with lines from Jinx
'''
with open('_Arcane.txt', 'r', encoding='utf-8') as EpisodeOne:
    EpOneLines = EpisodeOne.readlines()
    EpOne = []
    JinxLines = []

    IsJinxLine = False

    for line in EpOneLines:
        formatted_line = line.strip()
        EpOne.append(formatted_line)

    for char in EpOne:
        if char == "JINX":
            IsJinxLine = True
        if IsJinxLine and char != '' and not (char.isupper() and len(char) >= 2) and char[0] != '(':
            JinxLines.append(char)
        if char.isupper() and len(char) >= 2 and char != "JINX":
            IsJinxLine = False

'''
with open('_JinxLines.txt', 'w+') as f:
    for lines in JinxLines:
        f.write('%s\n' %lines)
'''