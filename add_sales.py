import  sys

if __name__ == '__main__':
    with open('bakery.csv', 'a') as f:
        f.write(sys.argv[1] + '\n')
    exit()