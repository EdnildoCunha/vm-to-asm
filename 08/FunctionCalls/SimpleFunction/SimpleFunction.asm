(SimpleFunction.test)
@2
D=A
@R13
M=D
(SimpleFunction.test_INIT_LOCALS_LOOP)
@SimpleFunction.test_INIT_LOCALS_END
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
MD=M-1
@SimpleFunction.test_INIT_LOCALS_LOOP
0;JMP
(SimpleFunction.test_INIT_LOCALS_END)
@LCL // push local 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL // push local 1
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=D+M
@SP
A=M
A=A-1
M=!M
@ARG // push argument 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=D+M
@ARG // push argument 1
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M-D
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
M=D+1
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP