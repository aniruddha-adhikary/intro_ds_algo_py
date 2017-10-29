def is_balanced(input_str):
    s = []
    for ch in input_str:
        if ch == '(':
            s.append(ch)
        if ch == ')':
            if s:
                return False
            previous_ch = s.pop()
            if previous_ch != '(':
                return False
    if not s:
        return True
    return False


if __name__ == "__main__":
    input_str = input() 
    if is_balanced(input_str):    
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
 
