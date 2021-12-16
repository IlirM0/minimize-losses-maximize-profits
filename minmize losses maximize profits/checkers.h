//
// Created by ilir8 on 14-12-2021.
//

#ifndef MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H
#define MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H

#include <iostream>

class checkers_piece;
class checkers_board;

enum class Board_Letter_Checkers
{
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H
};

class checkers_board
{
private:
    int row;
    int column;
    checkers_piece * piece;
    checkers_piece * board_arr;
};

class checkers_piece
{
private:
    std::string name;

public:
    checkers_piece();
};





#endif //MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H
