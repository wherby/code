#include <iostream>
#include <cstring>

int main(){
    const char * str{"Try not. Do or do not.There is no try."};
    char target ='T';
    const char *result = str;
    size_t iterations{};
    while((result = std::strchr(result,target))  != nullptr){
        std::cout << "Found " <<target
        << " starting at " << result << "'\n";
        ++result;
        ++iterations;
    }
    std::cout << "iterations: " << iterations << std::etndl;
    std::cout << result << std::endl;
}