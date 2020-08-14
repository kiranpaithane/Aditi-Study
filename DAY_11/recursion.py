i = 0

def demo():
    global i
    i +=1
    print("hello", i)
    demo()

demo()