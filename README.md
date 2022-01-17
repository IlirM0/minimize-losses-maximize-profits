<style>
    .figure
    {
        font-size:70%;
        font-weight:bold;
    }
    .source
    {
        font-size:60%;
        font-style:italic;
        /*font-weight:bold;*/
    }
</style>

# Minimizing loses maximizing profits
By: Jesse Masselink and Ilir Morina

### 1. Introduction

When playing a game like tik-tak-toe, checkers, chess, or any turn based game against a bot it will have to decide which move to make. Now a days these moves are calculated via AI and letting the bot play against itself a lot, but before AI there was an alogrithm that was often used called the minimax algorithm, that is the algorithm that we are going to be looking at in this assigment.


### 2. Minimaxing
Minimax stands for minimalizing the maximum possible outcome. This means when given a lot of options, it will calculate the best option based on succes and failure. 

The minimax algorithm works with a search-tree and a score system. The tree resembles all the possible moves that can happen in the game from the current position. At the lowest level of the tree, all possible outcomes of the game will be present (ideally, usually a maximum depth is set to lower load time). At each level of the tree, a maximizing or minimizing calculation will be done. This changes per height level of the tree.

For example: Looking at figure 1, at the depth of 3 from the root node, the row has a maximizing status. So it will look what the options are below, and choose the highest possible outcome. Wich is 8 for the blue node. The row above it, has a minimizing status. So in this case, it will choose the lowest possible outcome.

![](https://i.imgur.com/H4P24if.png)
<p class="figure">Figure 1, Minimax search tree with score system.</p>

The calculations are done in turns because it takes in account that the other player will also make the best possible move. Which will be the worst possible move for the bot.



### 3. Alpha beta pruning
#### 3.1 Introduction
Calculating the whole tree at the start of a game like checkers or chess can take a while. This is because there are a lot of possible moves that can be done and they can have many possible outcomes aswell. This is unfortunate ofcourse because it can be annoying to wait on a bots turn.

This is where Alpha-Beta Pruning comes into play. This (extra) algorithm works together great with the Minimax algorithm. It will eliminate portions of the search tree, thus making the total calculations less and decrease the time the bot takes to make a move.



#### 3.2 How it works
The algorithm will not change any behavior of the Minimax algorithm. It will only add a way to make it faster.

When looking at figure 2, you see that at the right part of the tree below 5, 8 is cut off the tree. This is done by calculating ahead from when 6 was found for the middle outcome from the root node. It knows, the root node will take the maximized outcome and when 5 was then found as a minimized outcome, it will never be higher than 5. Thus also never be higher than 6. It knows that whatever you find in the remaining part of that tree, it will not make a difference for choosing the move for the root node. Thats why it's useless to look further into the tree.

The part thats left will be excluded from the calculation. This way the total calculations the algorithm has to make will be less and make the bot choose the best move faster.

![](https://i.imgur.com/uZl9Cga.png)
<p class="figure">Figure 2, Minimax search tree Alpha-Beta Pruning</p>



### 4 Our implementation

The program we created for this assignment is devided into 3 parts, the first part gets input from the player to make a move, the second part is the game of checkers itself, the 3rd part is the bot move / minimaxing and alpha beta pruning.

#### 4.1 Player input

Getting a player input happens in the function show in figure 3.

![](https://i.imgur.com/lR9TKgx.png)
<p class="figure">Figure 3, The function for getting player input.</p>

The program first gets input from the player on which piece it wants to move, it checks if this coordinate exists on the board, if this coordinate actually has a piece the player can play, and if this piece can even make a legal move. 

Then it asks where the player wants to move this piece to, it again checks if it is a valid coordinate, if the space it wants to move to is empty, and if the player can make a move there.

Once these two things are correct the program will actually make a move on the board. 

##### Format of moves
Before we go into how checkers was programmed we will explain the format used for moves, that format is the following.<br>
[Piece coordinate, priority, path, enemies_killed]<br>
Piece coordinate is just the coordinate where the piece is at right now on the board.<br>

Priority is a number only used to determine if a move is a capturing move or not. It starts out at -1 and if the piece can make a walking move, that move gets a priority of 0, if a capturing move is possible then it will get a priority of 1 or higher, this way wherever a capture is possible you can easily remove all walking moves, since a capturing move is always mandatory over a walking move.<br>

Path is an array that contains all the coordinates that this move goes through.<br>

Enemies killed is pretty self explenatory, it is an array of enemies it will kill in this move, so that those enemies can easily be removed from the board if this move is made.

```
[['A3', 0, ['B4'], []], 
['C3', 0, ['B4'], []], 
['C3', 0, ['D4'], []], 
['E3', 0, ['D4'], []], 
['E3', 0, ['F4'], []], 
['G3', 0, ['F4'], []], 
['G3', 0, ['H4'], []]]
An example of the moves available for player O on move 1.
```


#### 4.2 Checkers

The board for checkers is stored in a dictionary called board, see figure 4.

![](https://i.imgur.com/jjGq0mq.png)
<p class="figure">Figure 4, The dictionary that stores the board state.</p>

The rules for checkers get enforced by a function that calculates all the legal moves for a player in a given board position. This function is called getPlayableMoves and can be seen in figure 5.
![](https://i.imgur.com/7lIdFTP.png)
<p class="figure">Figure 5, The function that gets back an array of playable moves.</p>

First this function gets all the pieces a player has on the board and returns all their coordinates. From there on it checks all playable moves for every piece on the board. Once that is done the program checks if any move in the list has a priority of 1 or higher (this means a capturing move is avaiable in the list), if that is the case the function will remove every move that has a priority of 0 or lower (moves with priority 0 or lower arent allowed if a capture is available).

#### The legalMove function

The legalMove function checks to see if an individial piece on the board has any legal moves. It does this by looking at a root piece his neighbouring pieces. Each quadrant is given a number, seen in figure 6.

![](https://i.imgur.com/l5l6ml5.png)
<p class="figure">Figure 6, The quadrant of a piece.</p>

These quadrants look at two moves in each direction, and check what the situation is for each of these neigbours. 

Sometimes neighbours dont exist, for example if a piece is next to a wall, and then the program will give back an error. If this is the case the program will catch the error and say that the piece has no neighbour there.

Once the situation is calculated for a quadrant the program will look if the situation for that quadrant is one of the following: 1, cant make a walking or capture move, 2 can make a walking move, or 3 can make a capturing move.

If the move is a capturing move, then the program will create a new copied board where this move takes place and go into this same function again recursively. Because after a capturing move, more capturing moves can be made, so the program calculates all possible capturing moves. See figure 7.

![](https://i.imgur.com/N1iFhmT.png)
<p class="figure">Figure 7, If the quadrant is a jumping move, go back recursively into the function.</p>

If the move is a walking move and the priority is -1 (since after a capture has been made it can't make another walking move after) it will add this move onto the valid moves list. See figure 8.

![](https://i.imgur.com/eUeLeSM.png)
<p class="figure">Figure 8, If the quadrant is a walking move, it will add the move onto the array to later send back.</p>

Once this list of moves is available it becomes pretty easy to program the bot that uses the minimaxing algorithm, since you only look at all the moves that are possible.

Making a move on the board is done with the function seen on figure 9.

![](https://i.imgur.com/GljJJte.png)
<p class="figure">Figure 9,<br>Function for making moves, it takes in the board and move information. The following steps are taken:<br>1. Put the piece onto its new position.<br>2. remove the piece from its old position.<br>3. remove every enemy it kills in this move.<br>4. check if a king can be made for either player in this position</p>

#### 4.3 Bot move
When the bot wants to make a move, it will use the Minimax algorithm on every move that it has available, to see which move has the best outcome. This is how we connect the evluation scores, which the minimax algorithm makes with every possible move, for the bot. See figure 10.

![](https://i.imgur.com/IeQXDVC.png)
<p class="figure">Figure 10, The function used for the bot to make a move.</p>

Our implementation for the minimax algorithm can be seen on figure 11.

![](https://i.imgur.com/E78E77L.png)
<p class="figure">Figure 11, The function for minimax.</p>

When calling this function it takes in the board position, a depth, a boolean that tells it if it needs to minimize of maximize, and an alpha and beta variable.

If the depth is 0, or a player has won, it will give back an evaluation for that position.

If that is not the case it will go further into the tree and check more moves. With the use of alpha beta pruning the program can also make this process take less time.

To go further into a tree the algorithm makes a copy of the board, on this coppied board it makes the move it want to inspect, and goes into the minimax algorithm recursively. Then when the max depth has been reached, or the game ends in that position, it will go back up the tree giving back the evaluation for that move.

### How to play a checkers game against our bot
To play the game you will have to go to our [github](https://github.com/IlirM0/minimize-losses-maximize-profits) and download the files. Then you have to have [python](https://www.python.org/downloads/) installed and then you can open the game by double clicking on the main.py file.

In game you first choose which side you want to play as. O or U. O plays first. The bot will automatically play as the other side.

The game then starts and you will need to make moves. You do this by first entering the coordinate of the piece you want to move, then you press enter. Then you enter the coordinate to where you want the selected piece to move. If this move is legal the game will allow you, else you will need to choose a new move to make with this piece. 

You can not unselect a piece once it is selected, so be sure that you want to make a move with this piece!

Have fun playing the game!

### Complications
Before we tried to make this algorithm work on checkers, we decided to make a game of tik tak toe and test out the algorithm on that and see how the algorithm works exactly. However because we tried to do this in C++ we got a lot of errors that were relatively hard to solve. And we thought that this was not really what the subject was about. So we decided to make the jump from C++ to python, and to just skip tik tak toe and go straight to checkers. This worked and we got a working game of checkers that you can play against a bot that uses the minimax algorithm. Furthermore creating checkers gave us a problem at the beginning but we got it working eventually.

### What we have learned
With this study we learned how minimaxing works and we also learned a bit about python. We also learned that even if the bot can look ahead 8 moves, it can still not consistently win against the player if it doesn't have a pretty complex board evaluation function.
