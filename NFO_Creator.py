import json, requests, sys, pprint, os 
import sportgrabber as sg

input_league = input("Which League is your team is? ")
input_team = input("Which team's latest game should I find? ")
print("Thank you, I'll look for the lastest " + input_league + " game " + " where the " + input_team + " played." )

TI = sg.TeamInfo(input_league.title(), input_team.title())

teamid = TI.get_team_id()

last_game = TI.get_last_game(teamid)


path = (os.path.dirname(__file__) + "/" + last_game[0]['strFilename'] + ".nfo")
NFO = open(path, 'w')



NFO.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
NFO.write("<episodedetails>" + "\n")
NFO.write("  <plot>" + last_game[0]["strAwayTeam"] + " vs. " + last_game[0]["strHomeTeam"] + "</plot>" + "\n")
NFO.write("<lockdata>false</lockdata>" + "\n")
NFO.write("<title>" + last_game[0]['strEvent'] + "</title>" + "\n")
NFO.write("<year>" + last_game[0]['strSeason'] + "</year>" + "\n")
NFO.write("</episodedetails>" + "\n")


NFO.close()
