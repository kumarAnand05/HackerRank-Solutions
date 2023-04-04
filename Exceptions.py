for n in range(int(input())):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as zero:
        print(f'Error Code: {zero}')
    except  ValueError as code:
        print(f"Error Code: {code}")
