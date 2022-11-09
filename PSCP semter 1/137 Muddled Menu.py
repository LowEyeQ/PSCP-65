''' Muddled Menu '''
def main():
    ''' Muddled Menu '''
    listvar = []
    while True:
        var = input()
        if var == "DONE":
            break
        elif var == "CLOSED":
            listvar = []
            break
        elif var == "SOMETHING'S WRONG":
            listvar = []
        elif "Can't do:" in var:
            listvar.remove(var.replace("Can't do: ", ""))
        else:
            var = var.split(" #")
            if var[1].isnumeric():
                listvar.insert(int(var[1]) - 1, var[0])
            else:
                listvar.append(var[0])
    print("Full Course:", listvar, end=" ")
    print("Reversed:", listvar[::-1])
main()
