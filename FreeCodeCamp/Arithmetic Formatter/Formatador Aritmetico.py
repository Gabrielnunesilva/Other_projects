def arithmetic_arranger(problems, show_answers=False):
    problem_line_1 = []
    problem_line_2 = []
    problem_line_3 = []
    answers_line = []


    if len(problems) > 5:
        return 'Error: Too many problems.'
    try:
        for problem in problems:
            problem = problem.replace(" ","")

            if "+" in problem:
                num1, num2 = problem.split("+")
                operator = "+"
                problem_result = str(int(num1) + int(num2)) 
            elif "-" in problem:
                num1, num2 = problem.split("-")
                operator = "-"
                problem_result = str(int(num1) - int(num2))
            else:
                return "Error: Operator must be '+' or '-'."
            
            if len(num1) > 4 or len(num2) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            
            width = max(len(num1), len(num2)) + 2

            
            problem_line_1.append(num1.rjust(width))
            problem_line_2.append(operator + " " +  num2.rjust(width - 2))
            problem_line_3.append("-" * width)
            answers_line.append(problem_result.rjust(width))

            result = f"{'    '.join(problem_line_1)}\n{'    '.join(problem_line_2)}\n{'    '.join(problem_line_3)}"

            if show_answers:
                result += f"\n{'    '.join(answers_line)}"
    except ValueError:
        return 'Error: Numbers must only contain digits.'
    return result


#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(arithmetic_arranger(["10 + 10", "20 - 20", "100 - 50", "10 - 120", "0 + 0"]))
