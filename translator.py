from tokenizer import *

#%%
def translate(tokens: list[list[Token]], indent=4) -> str:
    i: int = 0
    j: int = 0

    mainf:       str  = str()
    include: set[str] = set()

    TYPES: dict[str, str] = {
        "int": "int",
    }

    while i < len(tokens):
        print(tokens[i])
        while j < len(tokens[i]):
            mainf += indent * ' '
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
                print("Hello")
                mainf += f"{tokens[i][j].value} "
            elif isinstance(tokens[i][j], Assigner):
                mainf += f"= "
            elif isinstance(tokens[i][j], IntLiteral):
                mainf += f"{tokens[i][j].value} "
        mainf = mainf.strip()
        mainf += ";\n"
        i += 1
    
    return (mainf, include)

def build(mainf: str, include: set[str]) -> str:
    include = "\n".join([f"#include <{i}>" for i in include]) if len(include) > 0 else ""
    return f"""{include}\n\nint main() {{\n{mainf[:-1]}\n}}"""
# %%
