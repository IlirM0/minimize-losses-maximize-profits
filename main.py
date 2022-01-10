import playerinput

def printBoard():
    if player == 'O':
        # print(' ')
        # print(' +---+---+---+---+---+---+---+---+')
        # print(' +---+---+---+---+---+---+---+---+')
        # print(' ')
        print(' +---+---+---+---+---+---+---+---+')
        print('8| ■ | ' + board['B8'] + ' | ■ | ' + board['D8'] + ' | ■ | ' + board['F8'] + ' | ■ | ' + board['H8'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('7| ' + board['A7'] + ' | ■ | ' + board['C7'] + ' | ■ | ' + board['E7'] + ' | ■ | ' + board['G7'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('6| ■ | ' + board['B6'] + ' | ■ | ' + board['D6'] + ' | ■ | ' + board['F6'] + ' | ■ | ' + board['H6'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('5| ' + board['A5'] + ' | ■ | ' + board['C5'] + ' | ■ | ' + board['E5'] + ' | ■ | ' + board['G5'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('4| ■ | ' + board['B4'] + ' | ■ | ' + board['D4'] + ' | ■ | ' + board['F4'] + ' | ■ | ' + board['H4'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('3| ' + board['A3'] + ' | ■ | ' + board['C3'] + ' | ■ | ' + board['E3'] + ' | ■ | ' + board['G3'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('2| ■ | ' + board['B2'] + ' | ■ | ' + board['D2'] + ' | ■ | ' + board['F2'] + ' | ■ | ' + board['H2'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('1| ' + board['A1'] + ' | ■ | ' + board['C1'] + ' | ■ | ' + board['E1'] + ' | ■ | ' + board['G1'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('   A   B   C   D   E   F   G   H')
    else:
        # print(' ')
        # print(' +---+---+---+---+---+---+---+---+')
        # print(' +---+---+---+---+---+---+---+---+')
        # print(' ')
        print(' +---+---+---+---+---+---+---+---+')
        print('1| ■ | ' + board['G1'] + ' | ■ | ' + board['E1'] + ' | ■ | ' + board['C1'] + ' | ■ | ' + board['A1'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('2| ' + board['H2'] + ' | ■ | ' + board['F2'] + ' | ■ | ' + board['D2'] + ' | ■ | ' + board['B2'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('3| ■ | ' + board['G3'] + ' | ■ | ' + board['E3'] + ' | ■ | ' + board['C3'] + ' | ■ | ' + board['A3'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('4| ' + board['H4'] + ' | ■ | ' + board['F4'] + ' | ■ | ' + board['D4'] + ' | ■ | ' + board['B4'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('5| ■ | ' + board['G5'] + ' | ■ | ' + board['E5'] + ' | ■ | ' + board['C5'] + ' | ■ | ' + board['A5'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('6| ' + board['H6'] + ' | ■ | ' + board['F6'] + ' | ■ | ' + board['D6'] + ' | ■ | ' + board['B6'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('7| ■ | ' + board['G7'] + ' | ■ | ' + board['E7'] + ' | ■ | ' + board['C7'] + ' | ■ | ' + board['A7'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('8| ' + board['H8'] + ' | ■ | ' + board['F8'] + ' | ■ | ' + board['D8'] + ' | ■ | ' + board['B8'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('   H   G   F   E   D   C   B   A')

def printBotBoardTest(TestBoard):
    if bot == 'O':
        print(' +---+---+---+---+---+---+---+---+')
        print('8| ■ | ' + TestBoard['B8'] + ' | ■ | ' + TestBoard['D8'] + ' | ■ | ' + TestBoard['F8'] + ' | ■ | ' + TestBoard['H8'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('7| ' + TestBoard['A7'] + ' | ■ | ' + TestBoard['C7'] + ' | ■ | ' + TestBoard['E7'] + ' | ■ | ' + TestBoard['G7'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('6| ■ | ' + TestBoard['B6'] + ' | ■ | ' + TestBoard['D6'] + ' | ■ | ' + TestBoard['F6'] + ' | ■ | ' + TestBoard['H6'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('5| ' + TestBoard['A5'] + ' | ■ | ' + TestBoard['C5'] + ' | ■ | ' + TestBoard['E5'] + ' | ■ | ' + TestBoard['G5'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('4| ■ | ' + TestBoard['B4'] + ' | ■ | ' + TestBoard['D4'] + ' | ■ | ' + TestBoard['F4'] + ' | ■ | ' + TestBoard['H4'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('3| ' + TestBoard['A3'] + ' | ■ | ' + TestBoard['C3'] + ' | ■ | ' + TestBoard['E3'] + ' | ■ | ' + TestBoard['G3'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('2| ■ | ' + TestBoard['B2'] + ' | ■ | ' + TestBoard['D2'] + ' | ■ | ' + TestBoard['F2'] + ' | ■ | ' + TestBoard['H2'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('1| ' + TestBoard['A1'] + ' | ■ | ' + TestBoard['C1'] + ' | ■ | ' + TestBoard['E1'] + ' | ■ | ' + TestBoard['G1'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('   A   B   C   D   E   F   G   H')
    else:
        print(' +---+---+---+---+---+---+---+---+')
        print('1| ■ | ' + TestBoard['G1'] + ' | ■ | ' + TestBoard['E1'] + ' | ■ | ' + TestBoard['C1'] + ' | ■ | ' + TestBoard['A1'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('2| ' + TestBoard['H2'] + ' | ■ | ' + TestBoard['F2'] + ' | ■ | ' + TestBoard['D2'] + ' | ■ | ' + TestBoard['B2'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('3| ■ | ' + TestBoard['G3'] + ' | ■ | ' + TestBoard['E3'] + ' | ■ | ' + TestBoard['C3'] + ' | ■ | ' + TestBoard['A3'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('4| ' + TestBoard['H4'] + ' | ■ | ' + TestBoard['F4'] + ' | ■ | ' + TestBoard['D4'] + ' | ■ | ' + TestBoard['B4'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('5| ■ | ' + TestBoard['G5'] + ' | ■ | ' + TestBoard['E5'] + ' | ■ | ' + TestBoard['C5'] + ' | ■ | ' + TestBoard['A5'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('6| ' + TestBoard['H6'] + ' | ■ | ' + TestBoard['F6'] + ' | ■ | ' + TestBoard['D6'] + ' | ■ | ' + TestBoard['B6'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('7| ■ | ' + TestBoard['G7'] + ' | ■ | ' + TestBoard['E7'] + ' | ■ | ' + TestBoard['C7'] + ' | ■ | ' + TestBoard['A7'] + ' |')
        print(' +---+---+---+---+---+---+---+---+')
        print('8| ' + TestBoard['H8'] + ' | ■ | ' + TestBoard['F8'] + ' | ■ | ' + TestBoard['D8'] + ' | ■ | ' + TestBoard['B8'] + ' | ■ |')
        print(' +---+---+---+---+---+---+---+---+')
        print('   H   G   F   E   D   C   B   A')


board = { # normal board
    'B8':'U', 'D8':'U', 'F8':'U', 'H8':'U',
    'A7':'U', 'C7':'U', 'E7':'U', 'G7':'U',
    'B6':'U', 'D6':'U', 'F6':'U', 'H6':'U',
    'A5':' ', 'C5':' ', 'E5':' ', 'G5':' ',
    'B4':' ', 'D4':' ', 'F4':' ', 'H4':' ',
    'A3':'O', 'C3':'O', 'E3':'O', 'G3':'O',
    'B2':'O', 'D2':'O', 'F2':'O', 'H2':'O',
    'A1':'O', 'C1':'O', 'E1':'O', 'G1':'O'
}

def staticEvaluation(playboard):
    # U values are -1
    # O values are +1
    # kings count as 3
    evaluation = 0
    for key in playboard:
        if playboard[key] == 'O':
            evaluation += 1
        elif playboard[key] == 'Ö':
            evaluation += 3
        elif playboard[key] == 'U':
            evaluation -= 1
        elif playboard[key] == 'Ü':
            evaluation -= 3
    if hasTeamLost('O', playboard):
        evaluation = -100
    elif hasTeamLost('U', playboard):
        evaluation = 100
    return evaluation

def changePiece(piece,ch_value,int_value):
    ch = ord(piece[0]) + ch_value
    int_ = int(piece[1]) + int_value
    return chr(ch) + str(int_)

def getPlayableMoves(playerteam, playboard):
    # get all the playable moves a player has
    # format : [ piece_coordinate, priority, travel[], enemy_pieces_it_kills[]]
    pieces_array = getAllPieces(playerteam,playboard)

    if not pieces_array:
        # no playable pieces for this team anymore
        # return empty array
        return []
    playable_moves_array = []
    for pieces in pieces_array:
        # print('ASFda '+ pieces)
        if not legalMove(pieces,playerteam,playboard,pieces):
            # if the list is empty, do not append it.
            pass
        else:
            playable_moves_array = playable_moves_array + (legalMove(pieces, playerteam, playboard, pieces))

    if not playable_moves_array:
        # no playable pieces for this team anymore
        # return empty array
        return []
    # if max is greater than 0, then remove all in list with 0 or lower prio
    # print('Max printed: ',max(playable_moves_array, key= lambda x: x[1]))
    if max(playable_moves_array, key= lambda x: x[1])[1] > 0:
        playable_moves_array_copy = []
        for i in playable_moves_array:
            if i[1] > 0:
                playable_moves_array_copy.append(i)
        playable_moves_array = playable_moves_array_copy

    #     print(max(playable_moves_array, key= lambda x: x[1]))

    return playable_moves_array


def getAllPieces(playerteam, playboard): # get all the pieces a team has on the board
    arrayOfPieces = []
    for i in playboard:
        if playerteam == 'O':
            if playboard[i] == 'O' or playboard[i] == 'Ö':
                arrayOfPieces.append(i)
        else:
            if playboard[i] == 'U' or playboard[i] == 'Ü':
                arrayOfPieces.append(i)
    return arrayOfPieces

def assignMoveStatus(piece, close_neigh, far_neigh, direction_forward, prio, number):
    # E = enemy
    # T = teammate
    # False = no space
    # ' ' = space

    # # 'J' = you can capture that way.
    # # 'M' = you can move that way.
    # # False = cant move there.

    # remake direction. True = forward. False = Backward.
    if ((piece == 'O' or piece == 'Ö') and (direction_forward == 0 or direction_forward == 1)) or ((piece == 'U' or piece == 'Ü') and (direction_forward == 2 or direction_forward == 3)):
        direction_forward = True
    else:
        direction_forward = False

    if (piece == 'O' and number == '8') or (piece == 'U' and number == '1'): # if the pieces are at the end then they cant go anywhere else.
        return False
    elif close_neigh == 'E' and far_neigh == ' ':
        return 'J'
    elif close_neigh == ' ' and prio == -1 and (piece == 'Ö' or piece == 'Ü' or direction_forward):
        return 'M'
    else:
        return False

def assignNeighbour(piece_team, neighbour):
    # E = enemy
    # T = teammate
    # False = no space
    # ' ' = space
    if piece_team == 'O':
        if neighbour == 'O' or neighbour == 'Ö':
            return 'T'
        elif neighbour == 'U' or neighbour == 'Ü':
            return 'E'
    else:
        if neighbour == 'O' or neighbour == 'Ö':
            return 'E'
        elif neighbour == 'U' or neighbour == 'Ü':
            return 'T'
    if neighbour == ' ':
        return ' '
    else:
        print('assignNeighbour Error: got a false')
        return False

def legalMove(piece, playerteam, playboard, starting_piece, positions = [False, False, False, False], priority = -1, travel = [], enemy_killed = [], repetition=False):
    # return [starting_piece, priority, travel, enemy_killed]
    #
    # 'J' = you can capture that way.
    # 'M' = you can move that way.
    # False = cant move there.
    #
    # [[-1,1],[1,1],[-1,-1],[1,-1]] = the coordinates from this under [letter, number]
    #
    # positions =
    # 0   1
    #   P
    # 2   3
    moves = []
    if repetition:
        moves.append([starting_piece, priority, travel, enemy_killed])
        repetition = False
    coordinates = [[-1,1],[1,1],[-1,-1],[1,-1]]
    for idx, coor in enumerate(coordinates):
        # print(idx, ' + ', coor[0], ' + ', coor[1])
        direct_neighbour = False
        far_neighbour = False
        # E = enemy
        # T = teammate
        # False = no space
        # ' ' = space
        try:
            direct_neighbour = assignNeighbour(playerteam, playboard[changePiece(piece,1*coor[0],1*coor[1])])
        except:
            direct_neighbour = False
        try:
            far_neighbour = assignNeighbour(playerteam, playboard[changePiece(piece,2*coor[0],2*coor[1])])
        except:
            far_neighbour = False
        positions[idx] = assignMoveStatus(playboard[piece], direct_neighbour, far_neighbour, idx, priority, piece[1])

        # print(piece, ' Q', idx, ' = ', positions[idx], ' + prio: ', priority)
        if positions[idx] == 'M':
            moves.append([starting_piece, priority + 1, [changePiece(piece, 1 * coor[0], 1 * coor[1])], []])
            # print(piece, ' Q', idx, ' = ', positions[idx], ' + prio: ', priority)
        # TODO: Fix this under. J doesnt work for some reason
        elif positions[idx] == 'J':

            copy_board = playboard.copy()
            # remove enemy
            copy_board[changePiece(piece, 1 * coor[0], 1 * coor[1])] = ' '
            # replace piece to new place
            copy_board[changePiece(piece, 2 * coor[0], 2 * coor[1])] = copy_board[piece]

            copy_board[piece] = ' '

            # print(piece, ' Q', idx, ' = ', positions[idx])
            # print_play_board(copy_board)
            temp_enemy_killed = enemy_killed.copy()
            temp_enemy_killed.append(changePiece(piece, 1 * coor[0], 1 * coor[1]))
            temp_travel = travel.copy()
            temp_travel.append(changePiece(piece, 2 * coor[0], 2 * coor[1]))

            # moves.append([starting_piece,priority+2,temp_travel,temp_enemy_killed])
            moves = moves + (legalMove(changePiece(piece, 2 * coor[0], 2 * coor[1]), playerteam, copy_board, starting_piece,
                                   priority=priority + 2, travel=temp_travel, enemy_killed=temp_enemy_killed,
                                   repetition=True))
            del copy_board
            del temp_travel
            del temp_enemy_killed
    # 'J' = you can capture that way.
    # 'M' = you can move that way.
    # False = cant move there.
    # return [starting_piece, priority, travel, enemy_killed]
    return moves

def checkMakeKing(playboard):
    for i in ['A1','C1','E1','G1']:
        if playboard[i] == 'U':
            playboard[i] = 'Ü'
    for j in ['B8','D8','F8','H8']:
        if playboard[j] == 'O':
            playboard[j] = 'Ö'

def makeMoveOnBoard(infoList,playboard):
    # place the piece to its destination
    playboard[infoList[2][-1]] = playboard[infoList[0]]
    # remove the old place the piece was in
    playboard[infoList[0]] = ' '
    # remove all the enemies it kills
    for enemy in infoList[3]:
        playboard[enemy] = ' '
    checkMakeKing(playboard)

def playerMove():
    checkMakeKing(board)
    player_move = playerinput.getCoordinate(player, board, getPlayableMoves(player, board))
    move_destination = playerinput.getDestination(player_move,getPlayableMoves(player,board))
    full_move_list = playerinput.returnFullMoveList(player_move,move_destination,getPlayableMoves(player,board))
    makeMoveOnBoard(full_move_list,board)

def botMove():
    bestMove = []
    maxminEval = 0
    if bot == 'O':
        maxminEval = -120
    else:
        maxminEval = 120
    for move in getPlayableMoves(bot, board):

        playboard_copy = board.copy()
        makeMoveOnBoard(move,playboard_copy)
        if bot == 'O':
            eval = minimax(playboard_copy,7,False)
            if eval > maxminEval:
                maxminEval = eval
                bestMove = move
        else:
            eval = minimax(playboard_copy,7,True)
            # eval = minimax(playboard_copy, 3, False, 120, -120)
            if eval < maxminEval:
                maxminEval = eval
                bestMove = move
    makeMoveOnBoard(bestMove,board)

def minimax(playboard,depth,maximizingPlayer, alpha=-120, beta=120):
    if depth == 0:
        # temp_eval = staticEvaluation(playboard)
        # print('Eval in this pos: ', temp_eval)
        # printBotBoardTest(playboard)
        return staticEvaluation(playboard)
    if maximizingPlayer:
        # print('Maximizing')
        if hasTeamLost('O', playboard):
            return staticEvaluation(playboard)
        maxEval = -120
        for position in getPlayableMoves('O', playboard):
            playboard_copy = playboard.copy()
            makeMoveOnBoard(position,playboard_copy)
            eval = minimax(playboard_copy,depth-1,False, alpha, beta)
            maxEval = max(maxEval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        # print('Minimizing')
        if hasTeamLost('U', playboard):
            return staticEvaluation(playboard)
        minEval = 120
        for position in getPlayableMoves('U', playboard):
            playboard_copy = playboard.copy()
            makeMoveOnBoard(position, playboard_copy)
            eval = minimax(playboard_copy, depth - 1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


# def oppositeTeam(team):
#     if team == 'O':
#         return 'U'
#     else:
#         return 'O'

def hasTeamLost(team,playboard):
    if not getPlayableMoves(team, playboard):
        # print('[' + oppositeTeam(team) + '] has won the game!')
        return True
    else:
        return False

# ---------Main------------
# get the side the player wants to play as.
player = input('Choose valid side\nWhat side do you want to play as [O] or [U] ([O] goes first)\n')
while player != 'O' and player != 'U':
    player = input('Choose valid side\nWhat side do you want to play as [O] or [U] ([O] goes first)\n')
bot = ''
if player == 'O':
    bot = 'U'
else: # if the bot is 'O', then it gets to make the first move.
    bot = 'O'
    print('Bot makes the first move.')
    botMove()

gameOver = False
while not gameOver:
    print('Evaluation Score: ', staticEvaluation(board))
    printBoard()
    if hasTeamLost(player, board):
        gameOver = True
        print('[' + bot + '] has won the game! Better luck next time!')
    else:
        playerMove()
    if hasTeamLost(bot, board):
        gameOver = True
        print('[' + player + '] has won the game! Good job player!')
    else:
        botMove()



# ---------Main------------


