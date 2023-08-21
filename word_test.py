from decorator import line_wrapper, word

prefix = "pre"

@line_wrapper
def prefix_ct(word, prefix):
    try:
        count = 0
        for w in range(0,len(word)-len(prefix)+1):
            if word[w:w+len(prefix)] == prefix:
                count += 1
        print(count)
    except (TypeError,ValueError) as err:
        print(f"1. The variable word or prefix must be a string 2. {err}")

def main(word):
    prefix_ct(word,prefix)

if __name__ == "__main__":
    main() 