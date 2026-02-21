print("********** Welcome to Student Result System **********")

while True:
    name = input("\nEnter Student Name: ")
    
    total_subjects = int(input("Enter number of subjects: "))
    
    total_marks = 0
    
    # FOR LOOP to take marks of each subject
    for i in range(1, total_subjects + 1):
        marks = float(input(f"Enter marks for Subject {i}: "))
        
        # IF condition to check valid marks
        if marks < 0 or marks > 100:
            print("Invalid marks! Please enter between 0 and 100.")
            break
        else:
            total_marks += marks
    else:
        # This runs only if for loop does NOT break
        percentage = total_marks / total_subjects
        
        print(f"\nStudent Name: {name}")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%")
        
        # IF ELIF ELSE for grade calculation
        if percentage >= 80:
            print("Grade: A+")
        elif percentage >= 70:
            print("Grade: A")
        elif percentage >= 60:
            print("Grade: B")
        elif percentage >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")
    
    # WHILE loop control (continue or exit)
    choice = input("\nDo you want to check another result? \n1.press:1 for Yes \n2.Press: 2 for No ").lower()
    
    if choice == "no":
        print("Thank you for using the system!")
        break
