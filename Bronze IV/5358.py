while True:
    try:
        print(
            input()
            .replace("i", "*")
            .replace("e", "i")
            .replace("*", "e")
            .replace("I", "*")
            .replace("E", "I")
            .replace("*", "E")
        )
    except EOFError:
        break
