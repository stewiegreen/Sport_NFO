# Sport_NFO
This is a basic .nfo creator for Sports programming using SportsDB

Simply open NFO_Creator.py in terminal

This is meant to be a project to help me learn some python basics and how to implement and integrate them into a useful program.

A big thanks to theSportsDB.com as it is their API I'm using in this script.

Currently the main program relies on user input.

In the Experimental folder is a version of the program that cycles through a folder (and subfolders) and tries to parse filenames and automatically generate nfo files based on those file names.  This is brand new, and is still full of bugs and limitations. 

Unfortunately the filename structure is fairly rigid:

league_dd/mm/yyyy_team@team_station.ext

At this time league cannot be more than one word (e.g. NHL, NFL, NBA, Premier etc), partial names should offer a list of options. As well, full team names so far are not supported so abbreviations supported by sportdb, cities or names (i.e. Braves, Canucks) will work the best.
