# wsd2018-project

## **Project Report**  
Jukka Laakko 479754  
Juuso Jahnukainen 476812

### Goal
This project features a gamestore, where developers can add Javascript games for sale and users can buy and play them in browser.  
There is a gamesave and leaderboards system for players.
  

### Implementation
Backend relies on Django database, models, views and methods implemented with python. The implemented python models, views and methods are clear and the code is easy to follow and read.  

Frontend was built mostly on html, with w3css styling libary, which was sufficient for building a simple and clean UI in the scope of this project.
  
We are condifent with python, therefore most dynamic frontend content, such as high score handling and parsing, stats and statistic are handled with python through model methods and templatetags.  
  
JavaScript and Jquery were used for sending data between our service and the external payment service, as well as for saving and loading gamestates between main window and the iframe, where the game is running and also for some dynamic userinterface actions.

### Results
We learned how to create web services with Django, which was our goal for this project.  
As for the project, we implemented all of the basic functionalities that were required. Basic user authentication was implemented using django's tools without email validation.

Playing and interacting with games works fine, as well as saving game state and highscore. Highscores are saved and displayed to all the players who own that game.
Searching for games is very neat, as it shows matching games as you add characters the the search string. Player can only buy games they don't already own, and can only play games that have been
purchased. We were planning to add https connection, but due to requirement of external CA, we dropped the plan. That would have been a good addition especially as there is loginc credentials involed

If an account is registered as a developer, it isn't able to purchase or play any games, but can add them and afterwards see sales for them in quantity and revenue. Every time there is an
attempt to modify a game, it is checked that the game is added by that same user to prevent anyone from modifying games they do not own. Developer can only change game's name and description.
Price can only be changed via request to admin to protect buyers from insincere developers.

Game interaction provides options to save game's state, highscore or load a saved game. The communication between game and service goes both ways. The scores are recorded for each player separately
but if they are in top 5 globally, they are displayed as global highscores to everyone who owns the game.

The code is written according to django's separation of duties model. URL endpoints, forms, views and models are all clearly separated and then imported and called when required.
The functional parts of the code have comments to clarify their purpose to whomever is not familiar with the particular code segment's purpose. The user interface design of the
game store is tastefully done, and we have followed a modern and simplistic style in it. User experience is manually tested to be pleasant.


### Overall assessment:
The important parts of our project work flawlessly as they are tested to work. This includes adding, deleting, modifying, playing, saving, loading, searching and listing owned games.
This is the part we focused most on. UI would always have room for improvement with dynamic content and usability, but we feel that our current design has no major deficiencies. On the
other hand our project is lacking https and all the additional features like email validation and external identification using 3rd party applications. We also had some difficulties
with csrf token. We are not sure it is properly applied since server would occasionally not recognize it.


Score:

Basic player functionalities        100/200

Basic developer functionalities     300/300

Game/service interaction            200/200

Quality of Work                     100/100

Non-functional requirements         100/100


Save/load and resolution feature    100/100

Mobile friendly                     50/50


Total:                              1350


### Teamwork:

Juuso did mostly backend logic and was responsible for developer functions. He also had responsibility of applications deployment and configuration.

Jukka did most of the front-end work and was responsible for player side functions for back-end and front-end.

## Deployed at: [jurigin.herokuapp.com](url)

Test accounts (username / password):
- admin: admin1 / admin1
- player: demojug / asdqwerty1
- developer: jugeloper / qwertyperkele1