import string
alphabet = [x for x in string.ascii_lowercase]

while True:
    nums = input().lstrip()
    nums = nums.replace('^', '**')
    nums = nums.replace(' ', '')
    if not nums:
        continue
    elif nums.startswith('/'):
        if nums == '/help':
            print("""
            This program supports the following operations for integers:
            - Additions (+ operator)
            - Subtractions (- operator)
            - Multiplications (* operator)
            - Division (/ operator) 
            - Power (^ operator)
            Also allows parenthesis priority and variable memory (single letters or words)
            - e.g.: 
                - a = 1 (definition)
                - xyzzy = a (definition from variable current value)
                - meaningoflife = 41 + 1 (definition from an operation result)""")
            continue
        elif nums == "/exit":
            print('Bye!')
            exit()
        else:
            print('Unknown command')
    elif nums[0].lower() in alphabet:
        if len(nums.split('=')) > 1:
            nums_list = nums.split(('='))
            if not nums_list[0].strip().isalpha():
                print('Invalid identifier')
                continue
            try:
                exec(nums)
            except:
                print('Invalid expression')
        elif len(nums.split('=')) == 1:
            try:
                nums = nums.replace('/', '//')
                print(eval(nums))
            except NameError:
                print('Unknown variable')
        else:
            print('Invalid expression')
    else:
        if nums.count('//') > 0:
            print('Invalid expression')
        else:
            try:
                print(eval(nums))
            except:
                print("Invalid expression")
