# Service depends on python-lib
from lib.calc import add

def run_service():
    print("2 + 3 =", add(2,3))

if __name__ == "__main__":
    run_service()
