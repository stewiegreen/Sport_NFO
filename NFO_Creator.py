import json, requests, sys, os, pprint 
import sportgrabber as sg


league = sg.LeagueInfo.get_leagues()



TI = sg.TeamInfo(league)

teams = TI.get_teams(league)


input_date = input("Which date did the game occur? (yyyy-mm-dd)")

date = sg.Date(input_date)
datecheck = date.date_checker()


if datecheck:
    print("Thank you, generating file")
    game_day = TI.date_played(input_date, teams)
    TI.create_nfo(game_day)

else:
    print("Invalid Date format")

