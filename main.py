import testClass
from programs_to_test import tests
import importlib
def startup_all_tests():
    test_objects = []
    for i in tests:
        print(i)
        temp = importlib.import_module(i)
        test_objects.append(temp.test)
    return test_objects
def start_tests(test_objects):
    for i in test_objects:
        temp = i()
        status = temp.runTest()
        print(print_status(status))
def print_status(status):
    message = ""
    if(status["isSucess"]):
        message+=status['Test Name']
        message+=" Sucessfull\n"
    else:
        message+=status['Test Name']
        message+="failed message:\n"
        message+=str(status['output'])+"\n"
    return message

def main():
    to_test = startup_all_tests()
    start_tests(to_test)
main()
