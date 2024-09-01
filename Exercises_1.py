def main():
    size_limit = 25

    length_str = input("What is the length of the zander in centimeters? ")

    length = int(length_str)

    if length >= size_limit:
        print("Congratulations! You can keep the zander.")
    else:

        centimeters_below = size_limit - length
        print(f"The zander is below the size limit. Please release it back into the lake.")
        print(f"It is {centimeters_below} centimeters below the size limit.")


if __name__ == "__main__":
    main()