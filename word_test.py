word = "presupposition"
prefix = "pre"

def prefix_ct(word, prefix):
    count = 0
    for w in range(0,len(word)-len(prefix)+1):
        if word[w:w+len(prefix)] == prefix:
            count += 1
    print(count)

def main():
    prefix_ct(word, prefix)

if __name__ == "__main__":
    main() 