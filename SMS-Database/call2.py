
from subprocess import call

class callPy(object):
    def __init__(self,path="Fee_Frontend.py"):
        self.path = path
    def call_python_file(self):
        call(["python3","{}".format(self.path)])
if __name__ == "__main__":
    c=callPy()
    c.call_python_file()
    
