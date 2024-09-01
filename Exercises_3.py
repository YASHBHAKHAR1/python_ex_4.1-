def main():

    gender = input("Enter your biological gender (male/female): ").strip().lower()

    hemoglobin = int(input("Enter your hemoglobin value (g/l): "))

    if gender == "female":
        low = 117
        high = 155
    elif gender == "male":
        low = 134
        high = 167
    else:
        print("Invalid gender input")
        return  # Exit the program if gender input is invalid

    # Determine if the hemoglobin value is low, normal, or high
    if hemoglobin < low:
        print("Your hemoglobin value is low.")
    elif hemoglobin > high:
        print("Your hemoglobin value is high.")
    else:
        print("Your hemoglobin value is normal.")


if __name__ == "__main__":
    main()
