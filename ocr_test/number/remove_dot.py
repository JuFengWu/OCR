
def func(inputList):
    resultList = inputList.split(".")
    result = ""
    for i in resultList:
        result += i
    return result

def main():
    string1 = "3n3D."
    result = func(string1)
    print(result)

    string1 = "3n.3D"
    result = func(string1)
    print(result)
    


if __name__ == "__main__":
    main()
