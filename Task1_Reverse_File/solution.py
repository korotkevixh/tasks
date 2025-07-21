def order_reverse():
    print("Reading file..")
    with open("stdin.txt", "r") as src, open("stdout.txt", "w") as dst:
        content = src.read()
        content = content[::-1]
        dst.write(content)
    print("Writed.")
    return 0

def main():
    order_reverse()

if __name__ == "__main__":
    main()