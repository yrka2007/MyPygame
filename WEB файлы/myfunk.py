def myprint(*args, **kwargs):
    print(*args, *kwargs)
    print('-' * 30)


def main():
    myprint(input())


if __name__ == '__main__':
    main()
