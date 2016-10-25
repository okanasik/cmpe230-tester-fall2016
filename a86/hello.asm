jmp start				; Start program...
;============================
  msg   db  "Hello World.$"		; A string variable with a value.
;============================
start:
  mov ah,09				; subfunction 9 output a string
  mov dx,offset msg			; DX points to (holds the address of) the string
  int 21h				; Output the message
exit:
  mov ah,4ch
  mov al,00				; Exit code 0
  int 21h				; Terminate program
