def arithmetic_arranger(problems, arg = False):
  x_all = ''
  y_all = '' 
  dashes_all = '' 
  result_all = ''
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    x = problem.split(' ')[0]
    op = problem.split(' ')[1]
    y = problem.split(' ')[2]
        
    if op != '+' and op != '-':
      return "Error: Operator must be '+' or '-'."
    if len(x) > 4 or len(y) > 4:
      return "Error: Numbers cannot be more than four digits."
    if not x.isdigit() or not y.isdigit():
      return "Error: Numbers must only contain digits." 
        
    res = ""
    if op == '+':
      res = str(int(x) + int(y))
    elif op == '-':
      res = str(int(x) - int(y))

    length = max(len(x), len(y)) + 2  
    top = x.rjust(length)
    bottom = op + y.rjust(length - 1)
    result = res.rjust(length)
    dashes = ""
    for dash in range(length):
      dashes += '-'

    if problem != problems[-1]:
      x_all += top + '    '
      y_all += bottom + '    '
      dashes_all += dashes + '    ' 
      result_all += result + '    '
    else:
      x_all += top
      y_all += bottom
      dashes_all += dashes
      result_all += result     

  if arg:
    arranged_problems = x_all + '\n' + y_all + '\n' + dashes_all + '\n' + result_all 
  else:
    arranged_problems = x_all + '\n' + y_all + '\n' + dashes_all 

  return arranged_problems