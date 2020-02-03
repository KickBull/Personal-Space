

def did_you_mean(inp, correct):
    """This is not done btw"""
    
    count = 0
    c = 0
    for i, char in enumerate(list(inp)):
        c += 1
        # print(c)
        if count >= len(correct):
            break

        elif char == correct[i]:
            count += 1

    if count == len(correct):
        return "no mistakes found"

    if count >= len(correct) - 3 or count <= len(correct) + 2:
        return f"Did you mean '{correct}'?"

    return "no matches found"

print(did_you_mean("snakas", "ananas"))
print(did_you_mean("ananas", "ananas"))
print(did_you_mean("bruuuuuh", "hahahak"))

# import enchant
# print(enchant.Dict("en_US"))
