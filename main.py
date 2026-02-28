def main():
    hello("Sussy baka")
    hello()
    goodbye("john")

def hello(name: str = "World"):
    print("Hello", name)

def goodbye(name: str = "World"):
    print(f"Goodbye {name}. See you in therapy.")

if __name__ == "__main__":
    main()