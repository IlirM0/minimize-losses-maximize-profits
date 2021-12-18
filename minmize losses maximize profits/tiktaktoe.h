//
// Created by ilir8 on 14-12-2021.
//

#ifndef MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
#define MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H

#include <iostream>
#include <vector>

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

int one_to_zero_based(const int &num);
int zero_to_one_based(const int &num);
Board_Letter_TTT char_to_ttt_letter(const char &c);

class ttt_board
{
private:
    TTT_Check m_player_team;
    ttt_square * m_board_arr;
    std::vector<ttt_piece*> m_pieces;
    int m_squares_left;
public:
    ttt_board(const TTT_Check &player_team);
    ttt_square &get_square(const int &y_coor, const Board_Letter_TTT &x_coor) const;
    void place_tiktaktoe_check(const TTT_Check &team, int y_coor, Board_Letter_TTT x_coor);
    int get_square_left() const;
};

class ttt_piece
{
private:
    ttt_square * m_current_square;
    TTT_Check m_team;
public:
    ttt_piece(TTT_Check team, ttt_square * start_square);
    ttt_square *get_current_square() const;
    TTT_Check get_team() const;
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
    void set_y_coor(const int &y_coor);
    void set_x_coor(const Board_Letter_TTT &x_coor);
    void set_coords(const int &y_coor, const Board_Letter_TTT &x_coor);
    int get_y_coor() const;
    Board_Letter_TTT get_x_coor() const;
};




#endif //MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
