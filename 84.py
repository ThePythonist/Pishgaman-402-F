def func1(text):
    text = text.split()
    lenghts = []
    for i in text:
        lenghts.append(len(i))

    longest = max(lenghts)
    for i in text:
        if len(i) == longest:
            print(i)


text = "Python is a good programming language z"


# func1(text)

def func2(text):
    text = text.split()
    text.sort(key=len)
    print(text[-1])


# func2(text)

def func3(text):
    text = text.split()
    longest = max(text, key=len)
    print(longest)


func3(text)
