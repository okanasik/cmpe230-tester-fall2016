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
    
    return output_lines
    
    
def run_compiler_tests(base_dir, project_dir, a86_dir):
    test_files = get_test_files(base_dir)
    for test_file in test_files:
        full_test_file_path = base_dir + "/testcases/" + test_file        
        full_assembly_file_path = base_dir + "/testcases/" + test_file + ".asm"
        # a86 and DOS likes upper case
        # set the a86 file name
        a86_file_path = a86_dir + "/TEMP.ASM"
        os.chdir(project_dir)
        execute_command("make ARGS=\""+full_test_file_path+"\" run")
        # copy assembly output to the a86 directory
        shutil.copy(full_assembly_file_path, a86_file_path)
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
        
        # remove the created asm file
        os.remove(full_assembly_file_path)
        
        if check_program_output(base_dir, test_file, output_lines):
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