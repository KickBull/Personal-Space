

def spacify(inp: str):
    """Mathematical equation space fixer.
    Example:
    
    input: 4- (3 /2)*-16
    output: 4 - (3 / 2) * -16"""

    buffer = ""
    operators = ["+", "-", "*", "/"]
    final = ""

    for char in list(inp.strip("`")):
        if not len(buffer+char) >= 3:
            buffer+=char
        elif len(buffer+char) >= 3:
            buffer = buffer[1]
            buffer+=char

        if len(buffer) > 1:
            if buffer[1] in operators:
                if buffer[1] in ("+", "-") and not final[-1].isdigit() and not final[-1] in (")"):
                    final = f"{final}{buffer[1]}"
                else:
                    final = f"{final} {buffer[1]} "
            elif buffer[1] == " ":
                final = final
            else:
                final = final+buffer[1]
        else:
            final = buffer[0]

    return final