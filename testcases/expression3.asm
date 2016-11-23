code segment
 PUSH 3d
 PUSH 2d
 call multp
 PUSH 6d
 PUSH 1d
 call summ
msg:
 db '7'
 mov bx, msg
 push bx
 mov cx, 1d
 push cx
 call display
int 20h
display:
 POP AX
 POP CX
 POP BX
 PUSH AX
MOV AH, 02h
more:
 MOV DL,[BX]
 INT 21h
 INC BX
 DEC CX
 JNZ MORE
 ret
summ:
 POP BX
 POP CX
 POP AX
 ADD AX,CX
 PUSH AX
 PUSH BX
 ret
subt:
 POP BX
 POP CX
 POP AX
 SUB AX,CX
 PUSH AX
 PUSH BX
 ret
multp:
 POP BX
 POP CX
 POP AX
 MUL CX
 PUSH AX
 PUSH BX
 ret
division:
 POP BX
 MOV DX,0
 POP CX
 POP AX
 DIV CX
 PUSH AX
 PUSH BX
 ret
code ends
