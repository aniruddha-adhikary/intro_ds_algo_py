class Stack(list):
    def push(self, item):
        self.append(item)

    def is_empty(self):
        return not self


def is_balanced(input_str):
    s = Stack()

    for ch in input_str:
        if ch == '(':
            s.push(ch)
        if ch == ')':
            if s.is_empty():
                return False
            previous_ch = s.pop()
            if previous_ch != '(':
                return False

    return s.is_empty()


if __name__ == "__main__":
    input_str = input() 

    if is_balanced(input_str):    
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
 
