# CMPE 230 Project1 Test Scripts
## Dependencies

 - The code is tested on Ubuntu 14.04 64bit. If you are using Windows for the project, you may use cygwin, but it would be better if you use at least a linux system on a virtual machine.
 - If you try on Windows operating system, please write your setup and write the problems you encounter on piazza. (such as problem with the path separator)
 - The scripts are for python3.
 - To be able to test your A86 assembly code, you are supposed to install dosbox. You can download and install as described [here](https://www.dosbox.com/wiki/Basic_Setup_and_Installation_of_DosBox). The test script is using dosbox by calling as a shell program. **Therefore make sure that you can run dosbox from command line from any directory.**
## Steps to test your project
 1. Download as a zip folder or clone the project.
 2. Extract all the contents of the folder. The whole folder hierarchy supposed to be as follows:
++README.md
++tester.py
++compiler-tester.py
++interpreter-tester.py
++a86
++projects-compiler
++++2012800009
++++2012800010
++projects-interpreter
++++2012800009
++++2012800010
++testcases
++++test0
++++test0.out
++++test1
++++test1.out
 3. Copy the directory of your project including the Makefile under projects-interpreter directory if it is an interpreter project and under projects-compiler directory if it is a compiler project. Rename the directory with your studentID.
 4. Make sure that your Makefile has **run** target (you can check out the given sample Makefiles). Do not forget to use ${ARGS} argument for run target.
 5. To test your interpreter project run `./interpreter-tester.py projects-interpreter/<studentID>`
 6. To test your compiler project run `./compiler-tester.py <path-to-this-folder>/a86 projects-compiler/<studentID>`
 7. There is only two testcases for now, but I will notify you when I add new testcases, but you can also write your own testcases here. I will score your projects with different test cases.
 8. If you have any problems, please write the problem on piazza with the steps which are required to recreate the problem.
