# CMPE 230 Project1 Test Scripts
## Dependencies

 - The code is tested on Ubuntu 14.04 64bit. If you are using Windows for the project, you may use cygwin, but it would be better if you use at least a linux system on a virtual machine.
 - If you try on Windows operating system, please write your setup and write the problems you encounter on piazza. (such as problem with the path separator)
 - The scripts are for python3.
 - To be able to test your A86 assembly code, you are supposed to install dosbox. You can download and install as described [here](https://www.dosbox.com/wiki/Basic_Setup_and_Installation_of_DosBox). The test script is using dosbox by calling as a shell program. **Therefore make sure that you can run dosbox from command line from any directory.**
 - **For the compiler projects**, I did not implemented in the samples code to check the extension of ".ac" and changing it to the ".asm", but you are supposed to check the extension of the file and if there is ".ac" extension change it with ".asm" to output the a86 assembly code.

## Steps to test your project
 1. Download as a zip folder or clone the project.
 2. Extract all the contents of the folder. The whole folder hierarchy supposed to be seen as at the end of this document
 3. Copy the directory of your project including the Makefile under "projects" directory. Rename the your projects directory with your studentID.
 4. Make sure that your Makefile has **run** target (you can check out the given sample Makefiles). Do not forget to use ${ARGS} argument for run target.
 5. To test your interpreter run `./interpreter-tester.py projects/<studentID>`
 6. To test your compiler run `./compiler-tester.py <path-to-this-folder>/a86 projects/<studentID>`
 7. There is only two testcases for now, but I will notify you when I add new testcases, but you can also write your own testcases here. I will score your projects with different test cases and **also I will check your implementation**.
 8. Your program will also handle the error cases. If there is a syntax error, the program will print the following string `ERROR:<line number> <cause of error>`. (I will update scripts and add new testcases which will have syntax errors.). If the program is in interpreter mode, it will not print `<line number>`.
 9. If you have any problems, please write the problem on piazza with the steps which are required to recreate the problem.

## Folder Structure

├── a86  
│   ├── A86.COM  
│   ├── A86.LIB  
│   ├── A86MANU.TXT  
│   ├── COMPAT.8  
│   ├── D86.COM  
│   ├── D86MANU.TXT  
│   ├── EFF386.TXT  
│   ├── EFF86.TXT  
│   ├── ERDEMO.BAT  
│   ├── ERRATA.TXT  
│   ├── FILE_ID.DIZ  
│   ├── hello.asm  
│   ├── HELLO.COM  
│   ├── HELLO.OUT  
│   ├── HELLO.SYM  
│   ├── HEXOUT.8  
│   ├── INSTALL.BAT  
│   ├── LINES.8  
│   ├── MSDOS.8  
│   ├── MTCOLS.BAT  
│   ├── PAD_FILE.XML  
│   ├── PAGE.8  
│   ├── PAGE.BL  
│   ├── PAGE.COM  
│   ├── PAGE.SYM  
│   ├── README.TXT  
│   ├── REV.8  
│   ├── TCOLS.8  
│   ├── TEMP.ASM  
│   ├── TEMP.COM  
│   ├── TEMP.OLD  
│   ├── TEMP.OUT  
│   ├── TEMP.SYM  
│   ├── UNINSTAL.TXT  
│   └── USAGE.8  
├── compiler-tester.py  
├── interpreter-tester.py  
├── projects  
│   ├── 2012800009  
│   │   ├── main  
│   │   ├── main.cpp  
│   │   ├── main.o  
│   │   └── Makefile  
│   └── 2012800010  
│       ├── Main.class  
│       ├── Main.jar  
│       ├── Main.java  
│       └── Makefile  
├── README.md  
├── testcases  
│   ├── test0  
│   ├── test0.out  
│   ├── test1  
│   └── test1.out  
└── tester.py  
