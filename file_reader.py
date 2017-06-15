
def main():
    s = "abc"
    print(s.startswith(('e','q')))
    with open('aa.txt') as file:
        for l in file:
            l = l.strip()
            if l == '':
                continue
            print(l)

if __name__ == '__main__':
    main()