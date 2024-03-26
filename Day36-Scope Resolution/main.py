 #* variable scope=where a variable is visible and accessible
 #* scope resoultion=(LEGB) Local -> Enclosed -> Global -> Built-in


def func1():
    a=1 #it is only accessible inside func1()
    x=1
    print(x)
    print(a)

def func2():
    b=2
    print(x) #prints 3 as there is no local variable assigned of x
    print(b)


x=3
func1()
func2()