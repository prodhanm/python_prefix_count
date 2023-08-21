word = "presupposition"

def deco(fn):
    def wrapper(*args):
        print(f"The total number of prefix(es) in {word} are: ")
        fn(*args)
        print("*" * 53)
    return wrapper