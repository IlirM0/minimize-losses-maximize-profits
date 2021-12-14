//
// Created by ilir8 on 14-12-2021.
//

#ifndef MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
#define MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H

#include <iostream>

class ttt_piece;
class ttt_box;

class ttt_box
{
private:
    int row;
    int column;
    ttt_piece * piece;
};

class ttt_piece
{
private:
    std::string name;

public:
    ttt_piece();
};


#endif //MINMIZE_LOSSES_MAXIMIZE_PROFITS_TIKTAKTOE_H
