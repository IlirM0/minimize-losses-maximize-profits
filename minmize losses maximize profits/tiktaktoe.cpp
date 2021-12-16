//
// Created by ilir8 on 14-12-2021.
//

#include "tiktaktoe.h"

ttt_board::ttt_board() : m_board_arr{new ttt_square[9]}
{
}

ttt_piece::ttt_piece(TTT_Check team,ttt_square * start_square) : m_team{team}, m_current_square{start_square}
{}

ttt_square::ttt_square(Board_Letter_TTT x_coor, int y_coor) : m_y_coor{y_coor}, m_x_coor{x_coor}
{}

ttt_square::ttt_square() {}

void ttt_square::set_current_piece(ttt_piece * current_piece)
{
    m_current_piece = current_piece;
}

int one_to_zero_based(int num)
{
    if (num >= 1 && num <= 3)
    {
        return num-1;
    }
    else
    {
        std::cout << "ERROR IN one_to_zero_based: Number too big or too small" << '\n';
        return -1;
    }
}

int zero_to_one_based(int num)
{
    if (num >= 0 && num <= 2)
    {
        return num+1;
    }
    else
    {
        std::cout << "ERROR IN zero_to_one_based: Number too big or too small" << '\n';
        return -1;
    }
}

/*
    int 2d_arr = new int[width*height];

    //to get data or set data

    2d_arr[x*width + y] = something;

 */
