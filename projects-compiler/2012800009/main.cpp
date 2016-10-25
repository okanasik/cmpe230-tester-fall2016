#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

void processStatements(vector<std::string>& lines, string output_file_name) {
	ofstream output_file(output_file_name.c_str());
	if (output_file.is_open()) {
		output_file << "jmp start" << endl;
		for (int i = 0; i < lines.size(); i++) {
			char variable;
			int value;
			std::size_t found = lines.at(i).find("=");
			if (found != std::string::npos) {
				// get the variable name
				variable = lines.at(i).at(0);
				// get the assigned value
				value = lines.at(i).at(2);
				// define the variable
				output_file << variable << " db " << value << endl;
			} else if (lines.at(i).at(0) == variable) {
				// print the given variable
				output_file << "start:" << endl;
				output_file << "  mov ah, 02" << endl;
				output_file << "  mov dl, " << variable << endl;
				output_file << "  int 21h" << endl;
			}
		}
		output_file << "exit:" << endl;
		output_file << "  mov ah,4Ch" << endl;
		output_file << "  mov al,00" << endl;
		output_file << "  int 21h" << endl;
		output_file.close();
	}
}

int main(int argc, char** argv) {
	string input_file_name = argv[1];
	ifstream input_file(input_file_name.c_str());
	vector<string> input_lines;
	string line;
	if (input_file.is_open()) {
		while(getline(input_file, line)) {
			input_lines.push_back(line);
		}
		input_file.close();
	}
	// add the extension to the input file
	string output_file_name = input_file_name + ".asm";
	processStatements(input_lines, output_file_name);
	return 0;
}
