def func():
    print('First function')
    def func1():
        print('First child function')
    def func2():
        print('Second child function')
    func2()
    func1()
func()