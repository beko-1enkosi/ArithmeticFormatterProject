def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        arrays = problem.split()
        if len(arrays) != 3:
            return "Error: Invalid format."
        
        operand1, operator, operand2 = arrays
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

    top_line = ""
    bottom_line = ""
    dashed_line = ""
    answer_line = ""
    counter = 0

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        max_length = max(len(operand1), len(operand2)) + 2

        top = operand1.rjust(max_length)
        bottom = operator + " " + operand2.rjust(max_length - 2)
        dashes = "-" * max_length 

        num1 = int(operand1)
        num2 = int(operand2)

        if operator == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2
        
        answer_str = str(answer).rjust(max_length)

        if counter > 0:
            top_line += "    "
            bottom_line += "    "
            dashed_line += "    "
            answer_line += "    "

        top_line += top
        bottom_line += bottom
        dashed_line += dashes
        answer_line += answer_str

        counter += 1

    if show_answers:
        arranged_problems = top_line + "\n" + bottom_line + "\n" + dashed_line + "\n" + answer_line
    else:
        arranged_problems = top_line + "\n" + bottom_line + "\n" + dashed_line
    
    return arranged_problems

print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))



