#include <iostream>
#include "tiktaktoe.h"

int main() {
    ttt_board ttt_game;

    std::cout << "testing: "  << '\n';

    int option_from_user{-1};
    while(option_from_user != 0)
    {
        std::cout << "Choose one option to go on:\n0. Exit Program\n1. Make Move\n\n";
        option_from_user = -1;
        std::cin >> option_from_user;

        //std::cout << "Option by user: " << option_from_user << '\n';
        switch(option_from_user)
        {
            case 1:
                std::cout << "1 chosen\n";
                break;
            case 0:
                std::cout << "0 chosen\nhasta la vista, baby\n";
                break;
            default:
                std::cout << "not a valid input\ntry a number between 0 and 1\n\n";
                break;
        }
    }
    return 0;
}
