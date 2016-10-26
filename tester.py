#! /usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:46:20 2016

@author: okan
"""
import os
from subprocess import STDOUT, check_output, Popen, PIPE
import shlex

def execute_command(command):
    output = check_output(shlex.split(command), stderr=STDOUT, timeout=10)
    output = output.decode('utf-8')
    return output


def execute_command_with_input(cmd, input_lines):
    p = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE)
    output = p.communicate("\n".join(input_lines).encode('utf-8'))
    return output[0].decode('utf-8')    
    
    
def get_test_files(base_dir):
    os.chdir(base_dir)
    test_files = []
    for test_file in  os.listdir("testcases"):
        if test_file.find(".out") == -1 and test_file.find(".asm") == -1:
            test_files.append(test_file)
    return test_files
    
    
def get_test_input(base_dir, test_file):
    full_test_file_path = base_dir + "/testcases/" + test_file
    fp = open(full_test_file_path)
    input_lines = []
    for line in fp:
        input_lines.append(line.strip("\n"))
    return input_lines


def check_program_output(base_dir, test_file, output_lines):
    full_test_output_file_path = base_dir + "/testcases/" + test_file + ".out"
    fp = open(full_test_output_file_path)
    true_output_lines = []
    for line in fp:
        true_output_lines.append(line.strip("\n"))
        
    # check whether we have equal number of lines
    if len(output_lines) != len(true_output_lines):
        # print(str(len(output_lines)) + "-" + str(len(true_output_lines)))
        return False
    
    for line_index in range(len(true_output_lines)):
        # check for the syntax error handling
        if true_output_lines[line_index].find("ERROR") >= 0:
            if output_lines[line_index].find("ERROR") == -1:
                return False
        else:
            # check the equivalence of lines only if it is not error output
            if output_lines[line_index] != true_output_lines[line_index]:
                return False
        
    return True


def compile_code(base_dir, project_dir):
    os.chdir(project_dir)
    #print("MAKE:" + execute_command("make"))
    execute_command("make")
    os.chdir(base_dir)
    
    
def run_tests(base_dir, project_dir):
    test_files = get_test_files(base_dir)
    for test_file in test_files:
        os.chdir(base_dir)
        input_lines = get_test_input(base_dir, test_file)
        os.chdir(project_dir)
        output = execute_command_with_input("make run", input_lines)
        if check_program_output(base_dir, test_file, output):
            print(test_file + ":" + "PASSED")
        else:
            print(test_file + ":" + "FAILED")
        os.chdir(base_dir)
    