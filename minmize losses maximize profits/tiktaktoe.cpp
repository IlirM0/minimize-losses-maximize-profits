//
// Created by ilir8 on 14-12-2021.
//

#include "tiktaktoe.h"

ttt_board::ttt_board() : m_board_arr{new ttt_square[9]}
{
    for (int i = 0; i < 9; ++i)
    {
        // if i goes from 0 to 9, then i/3 will go 000 111 222, and i%3 goes 012 012 012
        //std::cout << "y: " << i/3 << " | x: " << static_cast<Board_Letter_TTT>(i%3) << '\n';
        m_board_arr[i].set_coords(i/3,static_cast<Board_Letter_TTT>(i%3)); // static cast recasts it from int to Board_Letter_TTT
    }
}

ttt_piece::ttt_piece(TTT_Check team,ttt_square * start_square) : m_team{team}, m_current_square{start_square}
{}

ttt_square::ttt_square(Board_Letter_TTT x_coor, int y_coor) : m_y_coor{y_coor}, m_x_coor{x_coor}
{}

void ttt_square::set_current_piece(ttt_piece * current_piece)
{
    m_current_piece = current_piece;
}

int one_to_zero_based(const int &num)
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

int zero_to_one_based(const int &num)
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

Board_Letter_TTT char_to_ttt_letter(const char &c)
{
    const char char_upper = std::toupper(c);
    switch(char_upper)
    {
        case A:
            return Board_Letter_TTT::A;
            break;
        case B:
            return Board_Letter_TTT::B;
            break;
        case C:
            return Board_Letter_TTT::C;
            break;
        default:
            std::cout << "ERROR IN char_to_ttt_letter: Number too big or too small\n";
            return Board_Letter_TTT::A;
            break;
    }
}

/*
    int 2d_arr = new int[width*height];

    //to get data or set data

    2d_arr[x*width + y] = something;

 */

void ttt_square::set_y_coor(const int &y_coor)
{
    m_y_coor = y_coor;
}

void ttt_square::set_x_coor(const Board_Letter_TTT &x_coor)
{
    m_x_coor = x_coor;
}

void ttt_square::set_coords(const int &y_coor, const Board_Letter_TTT &x_coor)
{
    m_y_coor = y_coor;
    m_x_coor = x_coor;
}

int ttt_square::get_y_coor() const
{
    return m_y_coor;
}

Board_Letter_TTT ttt_square::get_x_coor() const
{
    return m_x_coor;
}

ttt_square &ttt_board::get_square(const int y_coor, const Board_Letter_TTT x_coor)
{
    return m_board_arr[y_coor*3 + int(x_coor)];
}