def func1(func):
    def some_logic():
        func()
        print("Downloading has been started ...")
        print("Your movie has been downloaded ...")
    return some_logic
@func1
def func2():
    print("Click here to download a movie")
@func1
def func3():
    print("Click here to download a web series")
@func1
def func4():
    print("Click here to download a TV show")
func2()
func3()
func4()