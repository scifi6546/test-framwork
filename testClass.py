import os
import subprocess
class Tester:
    name="Base Test"
    def setup(self):
        print("test setup")
        return True
    def runProgram(self):
        print("running program testing program")
        return True
    def validate(self):
        print("program validated")
        return {"output":"Test Output","isSucess":True,"Test Name":self.name}
    def runTest(self):
        self.setup()
        self.runProgram()
        sucess = self.validate()
        return sucess
def startTests():
    test = Tester()
    sucess=test.runTest()
    if(sucess["isSucess"]):
        print("test sucessfull")
    else:
        print("Test unsucessfull\nOutput: "+output['output'])
