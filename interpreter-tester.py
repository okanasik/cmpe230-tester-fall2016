#! /usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:46:20 2016

@author: okan
"""
import sys
import os
from tester import compile_code
from tester import execute_command_with_input
from tester import check_program_output
from tester import get_test_files, get_test_input

def run_interpreter_tests(base_dir, project_dir):
    test_files = get_test_files(base_dir)
    for test_file in test_files:
        os.chdir(base_dir)
        input_lines = get_test_input(base_dir, test_file)
        os.chdir(project_dir)
        output = execute_command_with_input("make run", input_lines)
        # convert output to output lines
        output_lines = output.split("\n")
        # remove the empty line at the end of the program
        if len(output_lines[len(output_lines)-1]) == 0:
            del output_lines[len(output_lines)-1]

        full_test_output_file_path = base_dir + "/testcases/" + test_file + ".out"
        fp = open(full_test_output_file_path)
        true_output_lines = []
        for line in fp:
            true_output_lines.append(line.strip("\n"))
        
        if check_program_output(base_dir, true_output_lines, output_lines):
            print(test_file + ":" + "PASSED")
        else:
            print(test_file + ":" + "FAILED")
        os.chdir(base_dir)
    

def main():
    if len(sys.argv) != 2:
        print("interpreter-tester.py <project_dir>")
        return
    
    # set the base directory of the test script    
    base_dir = os.getcwd()
    # get directory of the project
    project_dir = sys.argv[1]
    
    compile_code(base_dir, project_dir)
    run_interpreter_tests(base_dir, project_dir)


if __name__ == "__main__":
    main()