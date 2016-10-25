#include <iostream>
#include <string>

int main() {
	std::string line;
	char variable;
	int value = 0;
	while(std::getline(std::cin, line)) {
		std::size_t found = line.find("=");
		if (found != std::string::npos) {
			// get the variable name
			variable = line.at(0);
			// get the assigned value
			value = line.at(2)-'0';
		} else if (line.at(0) == variable) {
			std::cout << value << std::endl;
		}
	}
	return 0;
}
