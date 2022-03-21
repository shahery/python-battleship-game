# Battleship Game
  Battleship is a python terminal game, which runs in the code institute mock terminal on heroku,
  This game is made for single player in which user can win the game by guessing the exact
  location of ship hidden in the board.

  The deployed link can be found here: 


# How to play
 This is a single player guessing game in which there will be the guess board with one ship hidden
 in the board and the user will have the five turns to hit the ship by guessing the location given
 in the board, If the user hit the ship 'k' symbol will be shown with the message of winning and 
 if the user missed the targets 'x' symbol will be shown on the board with the message that he has
 missed the target.
  

# Users stories:
    
    The Game is made simple, easy to access with good text colour and looking good. The Game is made for the following:
    * Users who love participating in the games.
    * Users who like entertainment of games.

# Table of contents
  * [Existing Features](#features)
  * [Technology Used](#technology-used)
  * [Features left to implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
  * [Colour](#colour)
  * [Deployment](#deployment)
  * [Credits](#credits) 

# Existing Features
 * Start the game
   * Only press Enter button will start the game.
   * Error message will display if you don't press enter button first.
   <img width="515" alt="shot1" src="https://user-images.githubusercontent.com/95220937/159238446-7aa3f3e3-5309-4c32-9f18-e221e426af32.png">

 * User Matrix_size selection
   * After input the username accurately
   * User can select the size of the matrix
   * User must input the valid integer
   * Error message will display if the user does not put the name accurately
   * Error message will display if the user does not input the valid integer
   * Error message will display if the user does not select the matrix size in range given
   <img width="600" alt="shot2" src="https://user-images.githubusercontent.com/95220937/159240431-90b02f2a-eaae-4b1d-8178-3a692e322fa3.png">

 * Ship row and column selection
   * User must enter the valid row and column (integer) for the board
   * User must enter the input within the range given
   * User must not repeat the values for row and column
   * Error message will display if the user does not enter valid row and column
   * Error message will display if the user does not input within the range given
   * Error message will display if the user repeats the values for row and column
   <img width="605" alt="shot3" src="https://user-images.githubusercontent.com/95220937/159241913-1f8ccd23-6f6e-4ec4-8c20-4fe68fc21a58.png">

 * Losing the game
   * If the user misses all his 5 guess shots
   * Then user will lose the game
   * A message will display of losing the game

   <img width="585" alt="shot4" src="https://user-images.githubusercontent.com/95220937/159245453-7d3cd959-b802-498b-82c1-fa8706f15f9c.png">

 * Winning the game
   * If the user selects the right row and column where the ship was hidden
   * Then user will win the game
   * A message will display of winning the game

   <img width="568" alt="shot5" src="https://user-images.githubusercontent.com/95220937/159245554-77b561bf-7636-4904-b59f-c96ccb334eb5.png">

   [Back to top](#)

# Technology Used 
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [GitHub](https://github.com)
  * [Gitpod](https://www.gitpod.io) 

   [Back to top](#)

 ## Features left to implement
   * 

# Testing
  I have manually tested this project by doing the following:
  * Passed the code through a PEP8 linter and confirmed there are no problems
  * Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
  * Tested in my local terminal and the Code Institute Heroku terminal

 ## Validator Testing
   * PEP8
     * No errors were returned from [PEP8 checker](http://pep8online.com/)
     <img width="1107" alt="pep8 checker" src="https://user-images.githubusercontent.com/95220937/159189614-14d2a068-f559-4308-b3b6-14135dd53794.png">    

   [Back to top](#)

  ## Bugs
   ### solved bugs
     

 ## Unfixed Bugs
   * No unfixed bugs.
   
   [Back to top](#)

# Colour
  
     

  [Back to top](#)
# Deployment
 This project was deployed using the code institute's mock terminal for heroku.
   * Steps for deployment:
     * Fork or clone this repository
     * Create a new heroku app
     * Set the buildpacks to Python and NodeJS in that order
     * Link the heroku app to the repository
     * Click on Deploy 

  [Back to top](#)
# Credits
 ## Content
   * The Idea of README.md file and the codes used for game were also learnt from [Code Institute](https://codeinstitute.net)
   * some codes used for game were taken from [Stackoverflow](https://stackoverflow.com/)
   * some codes used for game were taken from this tutorial video [Python battleship](https://www.youtube.com/watch?v=tF1WRCrd_HQ&ab_channel=KnowledgeMavens)

 ## Media
   * The ascii art logo was taken from [BATTLESHIP-ASCII ART](https://ascii.co.uk/art/battleship)

 ## Acknowledgements
   * My mentor who supported me throughout the project.
   * Code institute for the deployment terminal.

 [Back to top](#)