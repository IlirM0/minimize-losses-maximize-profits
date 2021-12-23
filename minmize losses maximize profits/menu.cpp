//
// Created by ilir8 on 18-12-2021.
//

#include "menu.h"
#include "limits"

void gameLoop();

void main_menu_loop(){
    int optionFromUser;

    std::cout << "Choose one option to go on:\n0. Exit Program\n1. Start a game\n\n";
    std::cin >> optionFromUser;


    while(optionFromUser!= 0 || std::cin.fail()){

        while (std::cin.fail()){    // check if input is integer
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Please enter a number.\n";
            std::cin >> optionFromUser;
        }

        switch(optionFromUser)
        {
            case 0:
                std::cout << "0 chosen\nhasta la vista, baby\n";
                break;
            case 1:
                std::cout << "1 chosen\n\n";
                gameLoop();
                break;
            default:
                std::cout << "Value does not exist in the menu\n\n";
                break;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Choose one option to go on:\n0. Exit Program\n1. Start a game\n\n";
        std::cin >> optionFromUser;
    }
    std::cout << "Game Ended";
}

void gameLoop(){
    int optionFromUser;
    std::cout << "Game Settings:\n";

    std::cout << "Choose one option to go on: (Cross starts the game)\n0. Go to main menu\n1. Start as Cross\n2. Start as Circle\n\n";
    std::cin >> optionFromUser;

    while (optionFromUser != 0 || std::cin.fail()){    // check if input is integer
        while (std::cin.fail()){    // check if input is integer
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Please enter a number.\n";
            std::cin >> optionFromUser;
        }

        switch(optionFromUser)
        {
            case 0:
                std::cout << "0 chosen\nHasta la vista, baby\n";
                break;
            case 1:
                std::cout << "1 chosen\nStart as Cross\n";
                //TODO: functie om te beginnen als Cross
                break;
            case 2:
                std::cout << "2 chosen\nStart as Circle\n";
                // TODO: functie om te beginnen als circle
                break;
            default:
                std::cout << "not a valid input\ntry a number between 0 and 1\n\n";
                break;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Please enter a number.\n";
        std::cin >> optionFromUser;
    }
    std::cout << "Going back to the main menu...\n\n";
}


//void game_loop()
//{
//    int option_from_user{-1}; // set to a value so it goes into the while loop
//    while(option_from_user != 0)
//    {
//        std::cout << "Choose one option to go on:\nCross starts the game\n0. Go to main menu\n1. Start as Cross\n2. Start as Circle\n\n";
//        std::cin >> option_from_user;
//
//        option_from_user = userIntChoise();
//
//        //std::cout << "Option by user: " << option_from_user << '\n';
//        switch(option_from_user)
//        {
//            case 0:
//                std::cout << "0 chosen\nhasta la vista, baby\n";
//                break;
//            case 1:
//                std::cout << "1 chosen\nStart as Cross\n";
//                break;
//            case 2:
//                std::cout << "2 chosen\nStart as Circle\n";
//                break;
//            default:
//                std::cout << "not a valid input\ntry a number between 0 and 1\n\n";
//                break;
//        }
//    }
//}


//std::cin.fail: checks if int