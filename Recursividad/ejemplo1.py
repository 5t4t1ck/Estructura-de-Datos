def print_a(c): 
    print(c, end="") if c < 'Z':
    print_b(chr(ord(c)+1))
    
    def print_b(c): 
        print(c, end="") 
        if c < 'Z': 
            print_a(chr(ord(c)+1))
            print_a('A')