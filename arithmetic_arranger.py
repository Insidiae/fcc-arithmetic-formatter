import re

def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    lengths = []
    top_operands = []
    bot_operands = []
    operators = []

    for problem_str in problems:
        problem = re.split("([+-/*])", problem_str.replace(" ", ""))

        if not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Error: Numbers must only contain digits."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."

        lengths.append(max(len(problem[0]), len(problem[2])) + 2)
        top_operands.append(problem[0])
        bot_operands.append(problem[2])
        operators.append(problem[1])
    
    res = ""
    for i in range(0, len(lengths)):
        if i > 0:
            res += "    "
        res += (" " * (lengths[i] - len(top_operands[i])))
        res += top_operands[i]

    res += "\n"
    for i in range(0, len(lengths)):
        if i > 0:
            res += "    "
        res += operators[i] + " "
        res += (" " * (lengths[i] - 2 - len(bot_operands[i])))
        res += bot_operands[i]
    
    res += "\n"
    for i in range(0, len(lengths)):
        if i > 0:
            res += "    "
        res += ("-" * lengths[i])

    if show_answer:
        res += "\n"
        for i in range(0, len(lengths)):
            if i > 0:
                res += "    "
            top = int(top_operands[i])
            bot = int(bot_operands[i])
            ans = top + bot if operators[i] == "+" else top - bot

            ans = str(ans)
            res += (" " * (lengths[i] - len(ans)))
            res += ans

    return res