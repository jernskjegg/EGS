# EGS

A small scraper script that fetches the title of the game that is currently free on Epic Games Store along with its image URL, and then pushes the data to slack.

The master branch version pulls all data from games that were recently in the vault, disregarding whether they're vaulted or not.

The filtered branch version shows only the games that are currently on offer and can be downloaded.


To do: Refactor the code. Structure the image/title extraction within a function, assign checks to a list and iterate with a for loop.
