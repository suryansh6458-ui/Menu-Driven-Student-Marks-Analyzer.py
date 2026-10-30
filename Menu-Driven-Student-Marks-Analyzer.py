
# Menu-Driven Student Marks Analyzer
# Class 11 Computer Science

marks = []

while True:

    print("\n===== STUDENT MARKS ANALYZER =====")
    print("1. Enter Marks")
    print("2. Display Marks")
    print("3. Calculate Total and Percentage")
    print("4. Find Highest and Lowest Marks")
    print("5. Check Pass or Fail")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Program terminated.")
        break

    elif choice == 1:

        marks = []

        for i in range(1, 6):
            m = float(input("Enter marks of subject " + str(i) + ": "))

            if m < 0 or m > 100:
                print("Invalid marks! Enter between 0 and 100.")
                marks = []
                break

            marks.append(m)

        if len(marks) == 5:
            print("Marks entered successfully.")

    elif choice == 2:

        if len(marks) == 5:
            print("Subject Marks:", marks)
        else:
            print("Please enter marks first.")

    elif choice == 3:

        if len(marks) == 5:
            total = sum(marks)
            percentage = total / 5

            print("Total Marks =", total)
            print("Percentage =", percentage, "%")
        else:
            print("Please enter marks first.")

    elif choice == 4:

        if len(marks) == 5:
            print("Highest Marks =", max(marks))
            print("Lowest Marks =", min(marks))
        else:
            print("Please enter marks first.")

    elif choice == 5:

        if len(marks) == 5:

            if min(marks) >= 33:
                print("Result: PASS")
            else:
                print("Result: FAIL")

        else:
            print("Please enter marks first.")

    else:
        print("Invalid choice!")
