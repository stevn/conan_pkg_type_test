#include "stuff.h"

#include <iostream>
#include <exception>

STUFF_EXPORT void stuff_check(void)
{
    try {
        std::cout << "It works!" << std::endl;
    } catch(std::exception const &) {
        // ...
    }
}
