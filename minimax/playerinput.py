def checkValidPiece(pieceSelected, team, board, listOfMoves):
    if checkLegalInput(pieceSelected):
        if team == 'O':
            if board[pieceSelected] == 'O' or board[pieceSelected] == 'Ö':
                if checkListOfMovesFor(pieceSelected,listOfMoves):
                    return True
                    # that piece has valid moves
                else:
                    print('That piece has no valid moves')
                    return False

            else:
                print('Thats not your piece')
                return False
        else:
            if board[pieceSelected] == 'U' or board[pieceSelected] == 'Ü':
                if checkListOfMovesFor(pieceSelected, listOfMoves):
                    return True
                    # that piece has valid moves
                else:
                    print('That piece has no valid moves')
                    return False
            else:
                print('Thats not your piece')
                return False
    return False

def checkValidDestination(pieceSelected,destination,listOfMoves):
    for i in listOfMoves:
        if i[0] == pieceSelected:
            if i[2][-1] == destination:
                # valid destination
                return True
    print('That is not a valid destination')
    return False

def checkListOfMovesFor(piece, listOfMoves):
    for i in listOfMoves:
        if piece == i[0]:
            return True
    return False

def checkLegalInput(userInput):
    # print('Letter: ' + userInput[0] + ', Digid: ' + userInput[1])
    if userInput in ['A1','C1','E1','G1','B2','D2','F2','H2','A3','C3','E3','G3','B4','D4','F4','H4','A5','C5','E5','G5','B6','D6','F6','H6','A7','C7','E7','G7','B8','D8','F8','H8']:
        # print('Valid coordination')
        return True
    else:
        print('Choose a valid coordination')
        return False


def getCoordinate(team, board, listOfMoves):
    coordinate = input('Enter the position for \'' + team + '\': ')
    while not checkValidPiece(coordinate, team, board, listOfMoves):
        if coordinate == 'help':
            print('O = black\nU = White\nÖ and Ü are kings')
        # if coordinate == 'rules':
        #     print('da rules')
        coordinate = input('Enter the position for \'' + team + '\': ')
    return coordinate

def getDestination(piece, listOfDestinations):
    coordinate = input('Enter the destination for \'' + piece + '\': ')
    while not checkValidDestination(piece, coordinate, listOfDestinations):
        coordinate = input('Enter the destination for \'' + piece + '\': ')
    return coordinate

def returnFullMoveList(piece,destination,listOfDestintions):
    for i in listOfDestintions:
        if i[0] == piece and i[2][-1] == destination:
            return i
    return False
