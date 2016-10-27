#! /usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:46:20 2016

@author: okan
"""
import sys
import os
from tester import compile_code
from tester import execute_command
from tester import check_program_output
from tester import get_test_files
import shutil

def get_assembly_output(a86_dir):
    output_lines = []
    fp = open(a86_dir+"/TEMP.OUT")
    for line in fp:
        stripped_line = line.strip("\n")
        if len(stripped_line) > 0:
            output_lines.append(stripped_line)
    fp.close()
    return output_lines

    
#def get_output_lines_from_assembly_file(assembly_file_path):
#    output_lines = []
#    fp = open(assembly_file_path)
#    for line in fp:
#        stripped_line = line.strip("\n")
#        if len(stripped_line) > 0:
#            output_lines.append(stripped_line)
#    fp.close()
#    return output_lines
    

def get_line_number_from_error_line(error_line):
    errors = error_line.split(":")
    # there should be two strings
    return int(errors[1].split(" ")[0])
    
    
def check_error_lines(program_error_lines, error_output_lines):
    if len(error_output_lines) != len(program_error_lines):
        return False
        
    for line_index in range(len(error_output_lines)):
        # get the line number from the line
        true_error_line_number = get_line_number_from_error_line(error_output_lines[line_index])
        error_line_number = get_line_number_from_error_line(program_error_lines[line_index])
        if true_error_line_number != error_line_number:
            return False
    
    return True


def clean_temp_files(temp_files):
    for file_name in temp_files:
        if os.path.isfile(file_name):
            os.remove(file_name)

    
def run_compiler_tests(base_dir, project_dir, a86_dir):
    test_files = get_test_files(base_dir)
    for test_file in test_files:
        full_test_file_path = base_dir + "/testcases/" + test_file

        error_output_lines = []
        true_output_lines = []
        
        # check whether test output has some errors
        full_test_output_file_path = full_test_file_path + ".out"
        test_output_fp = open(full_test_output_file_path)
        for line in test_output_fp:
            if line.find("ERROR") >= 0:
                error_output_lines.append(line.strip("\n"))
            else:
                true_output_lines.append(line.strip("\n"))
        test_output_fp.close()
        
        full_assembly_file_path = base_dir + "/testcases/" + test_file + ".asm"
        # a86 and DOS likes upper case
        # set the a86 file name
        a86_file_path = a86_dir + "/TEMP.ASM"
        
        temp_files = []
        temp_files.append(full_assembly_file_path)
        temp_files.append(a86_dir+"/TEMP.ASM")
        temp_files.append(a86_dir+"/TEMP.OUT")
        temp_files.append(a86_dir+"/TEMP.COM")  
        
        os.chdir(project_dir)
        program_output = execute_command("make ARGS=\""+full_test_file_path+"\" run")
        # convert output to output lines
        program_error_lines = program_output.split("\n")
        # remove the empty line at the end of the program
        if len(program_error_lines[len(program_error_lines)-1]) == 0:
            del program_error_lines[len(program_error_lines)-1]

        # check error lines
        if len(error_output_lines) > 0:
            if not check_error_lines(program_error_lines, error_output_lines):
                print(test_file+":FAILED")
                # continue with the next test file
                clean_temp_files(temp_files)
                os.chdir(base_dir)
                continue
        
        # copy assembly output to the a86 directory
        shutil.copy(full_assembly_file_path, a86_file_path)
        
        output_lines = []
        # to run the assembler and the program just run the dosbox
        dosbox_cmd = "dosbox "
        # mount a86 dir as c drive
        dosbox_cmd += '-c "MOUNT C '+a86_dir+'" '
        dosbox_cmd += '-c "C:" '
        dosbox_cmd += '-c "A86 TEMP.ASM" '
        dosbox_cmd += '-c "TEMP > TEMP.OUT" '
        dosbox_cmd += '-c "EXIT"'
        # run the dosbox_cmd
        execute_command(dosbox_cmd)
        
        # process TEMP.OUT
        output_lines = get_assembly_output(a86_dir)
        
        # remove temporary files
        clean_temp_files(temp_files)
        
        if check_program_output(base_dir, true_output_lines, output_lines):
            print(test_file + ":" + "PASSED")
        else:
            print(test_file + ":" + "FAILED")
        os.chdir(base_dir)
    

def main():
    if len(sys.argv) != 3:
        print("tester.py <a86_dir> <project_dir>")
        return
    
    # set the base directory of the test script    
    base_dir = os.getcwd()
    # get the directory of assembler dir
    a86_dir = sys.argv[1]
    # get directory of the project
    project_dir = sys.argv[2]
    
    compile_code(base_dir, project_dir)
    run_compiler_tests(base_dir, project_dir, a86_dir)

if __name__ == "__main__":
    main()