from lexer import *
from datetime import datetime

SYSCALLS = {
    "exit": 60,
    "write": 1,
    "read": 0,
}

def translate(tokenized, timestamp):
    assembly = "global _start\n_start:\n"
    def    line(in_):   return "    " + in_ + "\n"
    def comment(in_): return "    ; " + in_ + "\n"
    tokenindex = 0
    outer = 0
    while outer < len(tokenized):
        while tokenindex < len(tokenized[outer].tokens):
            if isinstance(tokenized[outer].tokens[tokenindex], ExitKeyword):
                assembly += line(f"mov rax, {SYSCALLS['exit']}")
                tokenindex += 1
                if isinstance(tokenized[outer].tokens[tokenindex], Expression):
                    assembly += line(f"mov rdi, {tokenized[outer].tokens[tokenindex].evaluate()}")
                    tokenindex += 1
                else:
                    raise Exception("Expected number after exit keyword")
                assembly += line("syscall")
        outer += 1
    
    # To allow people to write code without having to exit
    assembly += line("mov rax, 60")
    assembly += line("mov rdi, 0")
    assembly += line("syscall")
    if timestamp: assembly += comment(f"Compiled by Sabbah compiler on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
    
    return assembly