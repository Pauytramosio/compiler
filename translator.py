from tokenizer import *

#%%
def translate(tokens: list[list[Token]], indent=4) -> str:
    i: int = 0
    j: int

    mainf:       str  = str()
    include: set[str] = set()
    builtintypes: list[str] = [
        """typedef struct {
    void (*run)(void*);  // Function pointer with a void* parameter
    void* arg;           // Argument to pass to the function
} Runnable;""",
    ]

    TYPES: dict[str, str] = {
        "int": "int",
    }

    while i < len(tokens):
        j = 0
        mainf += indent * ' '
        while j < len(tokens[i]):
            if isinstance(tokens[i][j], Keyword):
                if isinstance(tokens[i][j], ExitKeyword):
                    include.add("stdlib.h")
                    mainf += f"exit({tokens[i][j+1].value})"
                    j += 2
                elif isinstance(tokens[i][j], LetKeyword):
                    mainf += f"{tokens[i][j+1].value} {tokens[i][j+2].value} = {tokens[i][j+4].value}"
                    j += 5
                elif isinstance(tokens[i][j], DeclareKeyword):
                    mainf += f"{tokens[i][j+1].value} {tokens[i][j+2].value}"
                    j += 5
            elif isinstance(tokens[i][j], VariableReference):
                mainf += f"{tokens[i][j].value} "
                j += 1
            elif isinstance(tokens[i][j], Assigner):
                mainf += f"= "
                j += 1
            elif isinstance(tokens[i][j], IntLiteral):
                mainf += f"{tokens[i][j].value} "
                j += 1
            elif isinstance(tokens[i][j], Operator):
                mainf += f"{tokens[i][j].value} "
                j += 1
        mainf += ";\n"
        i += 1
    mainf += indent * ' '
    mainf += "exit(0);\n"
    include.add("stdlib.h")
    
    types = builtintypes.copy()
    return (mainf, include, types)

def build(mainf: str, include: set[str], types) -> str:
    include = "\n".join([f"#include <{i}>" for i in include]) if len(include) > 0 else ""
    types = "\n".join([f"{i}" for i in types]) if len(types) > 0 else ""
    return f"""{include}\n\n{types}\n\nint main() {{\n{mainf[:-1]}\n}}"""
# %%
