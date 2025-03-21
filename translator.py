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
        while j < len(tokens[i]):
            if isinstance(tokens[i][j], Keyword):
                if isinstance(tokens[i][j], ExitKeyword):
                        include.add("stdlib.h")
                        mainf += f"{indent * ' '}exit({tokens[i][j+1].value});\n"
                        j += 2
                elif isinstance(tokens[i][j], LetKeyword):
                        mainf += f"{tokens[i][j+2].value} = {tokens[i][j+4].value};\n"
                        j += 5
        i += 1
    
    return (mainf, include)

def build(mainf: str, include: set[str]) -> str:
    include = "\n".join([f"#include <{i}>" for i in include]) if len(include) > 0 else ""
    return f"""{include}\n\nint main() {{\n{mainf}\n}}"""
# %%
