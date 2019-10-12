import autosportgrabber as sg
import json, requests, sys, os, re

folder = input('Enter Directory path to Search (this will search subfolders!)')

filelist = []
for root, dirs, files in os.walk(folder):
    for file in files:
        if sg.find_game(file) != None:
            specgame = sg.find_game(file)
            filelist.append(specgame)

for file in filelist:

    league, away, home, date, ext = sg.parse_filenames(file)

    stringleague = league[0]
    stringaway = away[0]
    stringhome = home[0]
    stringdate = date[0]
    stringdate = stringdate.replace('.','-')
    stringdate = stringdate.replace('/','-')

    leagues = sg.get_leagues()

    strleague = sg.find_league(leagues, stringleague)

    allteams = sg.get_teams(strleague)

    teamid = sg.find_team(allteams, stringhome)

    event = sg.date_played(stringdate, teamid)

    sg.create_nfo(event)
