while True:
    n = float(input())
    if n < 0:
        break
    else:
        print(
            "Objects weighing "
            + str("{:.2f}".format(n))
            + " on Earth will weigh "
            + str("{:.2f}".format(n * 0.167))
            + " on the moon."
        )
