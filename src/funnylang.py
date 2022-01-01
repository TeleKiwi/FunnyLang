def interpret(lines:list[str]):
    stack = []
    for line in lines:
        i = lines.index(line)
        keyword = lines[i].split(" ")[0]
        if keyword == "fuck":
            arg = lines[i].split(" ")[1]
            stack += arg
        elif keyword == "zamn":
            stack.pop()
        elif keyword == "caddydaddy":
            print(stack[0])
        else:
            print("OOPS, MOTHERFUCKER, SOMETHIN'S GONE WRONG!")
            


    
def main():
    while True:
        fPath = input(">>> ")
        text_file = open(fPath, "r")
        lines = text_file.readlines()
        text_file.close()
        interpret(lines)


main()