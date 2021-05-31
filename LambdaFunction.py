import os,sys,json

from enum import Enum
from subprocess import Popen, PIPE
from glob import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class LambdaFunctionType(Enum):
    py = 1
    other = 2

class LambdaFunction():
    def __init__(self, lambda_function_type, callback):
        self.lambda_function_type = lambda_function_type
        self.callback = callback

    def call(self,arguments):
        if self.lambda_function_type == LambdaFunctionType.py:
                return json.dumps(self.callback.main(arguments))
        else:
            with Popen([self.callback,str(arguments)], stdout=PIPE) as proc:
                return json.dumps(str(proc.stdout.read()))

    @classmethod
    def create(cls,path,name):
        if cls.checkIfPython(path):
            sys.path.append(os.path.abspath(os.path.join(BASE_DIR, f'lambdas/{name}')))
            return LambdaFunction(lambda_function_type=LambdaFunctionType.py, callback=__import__(name))
        else:
            return LambdaFunction(lambda_function_type=LambdaFunctionType.other, callback=cls.findCallPath(path))

    @staticmethod
    def checkIfPython(path):
        for g in glob(f"{path}/*.py"):
            return True
        return False

    @staticmethod
    def findCallPath(path):
        for g in glob(f"{path}/*.*"):
            return g
