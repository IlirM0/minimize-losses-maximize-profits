//
// Created by ilir8 on 14-12-2021.
//

#ifndef MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H
#define MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H

#include <iostream>

class checkers_piece;
class checkers_box;

class checkers_box
{
private:
    int row;
    int column;
    checkers_piece * piece;
};

class checkers_piece
{
private:
    std::string name;

public:
    checkers_piece();
};

#endif //MINMIZE_LOSSES_MAXIMIZE_PROFITS_CHECKERS_H
