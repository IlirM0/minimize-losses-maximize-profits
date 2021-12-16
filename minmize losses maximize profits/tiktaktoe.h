//
// Created by ilir8 on 14-12-2021.
//

#ifndef MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
#define MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H

#include <iostream>

class ttt_piece;
class ttt_board;
class ttt_square;

enum Board_Letter_TTT
{
    A,
    B,
    C
};

enum class TTT_Check
{
    Cross,
    Circle
};

int one_to_zero_based(int num);
int zero_to_one_based(int num);

class ttt_board
{
private:
    ttt_square * m_board_arr;
public:
    ttt_board();
};

class ttt_piece
{
private:
    ttt_square * m_current_square;
    TTT_Check m_team;
public:
    ttt_piece(TTT_Check team, ttt_square * start_square);
};

class ttt_square
{
private:
    int m_y_coor;
    Board_Letter_TTT m_x_coor;
    ttt_piece * m_current_piece;
public:
    ttt_square(Board_Letter_TTT x_coor, int y_coor);
    ttt_square();
    void set_current_piece(ttt_piece * current_piece);
};




#endif //MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
