class father(object):
    def sayHi(self):
        print("Hi, I am your father.")
    

class mother(object):
    def sayHi(self):
        print("Hello, I am your mother")

class child(mother, father):
    pass

childs = child()
childs.sayHi()