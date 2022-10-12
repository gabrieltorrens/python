def main():
    x, y = 1000, 100

    if x<y:
        result = "x is < y"
    elif x==y:
        result = "x == y"
    else:
        result = "x is > y"

    print(result)

    result = "x is < y" if x < y else "x is > or = to y"
    print(result)

    #match-case
    value = "seven"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four": #three or four
            result = (3,4)
        case _: #default case handler
            result = -1
    print(result)


if __name__ == "__main__":
    main()