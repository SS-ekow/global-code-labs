def calculate( op : str, x: int, y: int):
    if op == "ADD":
        print(f'{x} + {y} = {x+y}')
        
    elif op == "SUBTRACT":
        print(f'{x} - {y} = {x-y}')
        
    elif op == "MULTIPLY":
        print(f'{x} * {y} = {x*y}')
        
    elif op == "DIVIDE":
        print(f'{x} / {y} = {x/y}')
        
    else:
        print('invalid operation')
        
calculate('ADD', 4,5)
calculate('DIVIDE', 6,2)
calculate('MULTIPLY', 10, 8)
calculate('SUBTRACT', 12,3)
              
        
    