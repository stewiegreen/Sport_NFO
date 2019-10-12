# Sport_NFO
This is a basic .nfo creator for Sports programming using SportsDB

Simply open NFO_Creator.py or Auto_NFO.py in terminal

This is meant to be a project to help me learn some python basics and how to implement and integrate them into a useful program.

A big thanks to theSportsDB.com as it is their API I'm using in this script.

NFO_Creator relies on user input.  Its search is fairly forgiving and will offer multiple options if the search result finds more than one match.  So a search for New York in the NHL will offer 2 choices: Rangers or Islanders. 


Auto_NFO cycles through a user-specified folder (and subfolders) and tries to parse filenames and automatically generate nfo files based on those file names.  This is brand new, a bit buggy and has its limitations. At this time leagues cannot be more than one word/abbreviation (e.g. NHL, NFL, NBA, Premier etc), multiple matches will still offer a list of options. As well, full team names so far are not supported so abbreviations supported by sportdb, cities or names (i.e. Braves, Canucks) will work the best.

The filename structure is fairly rigid:

league_dd/mm/yyyy_team@team_station.ext

** station refers to the broadcast station (NBC, ABC, CBC, SN etc...)
