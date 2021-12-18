//
// Created by ilir8 on 18-12-2021.
//

#include "menu.h"

void main_menu_loop()
{
    int option_from_user{-1}; // set to a value so it goes into the while loop
    while(option_from_user != 0)
    {
        std::cout << "Choose one option to go on:\n0. Exit Program\n1. Make Move\n\n";
        std::cin >> option_from_user;

        std::cout << "Option by user: " << option_from_user << '\n';
        switch(option_from_user)
        {
            case 0:
                std::cout << "0 chosen\nhasta la vista, baby\n";
                break;
            case 1:
                std::cout << "1 chosen\n";
                break;
            default:
                std::cout << "not a valid input\ntry a number between 0 and 1\n\n";
                break;
        }
    }
}