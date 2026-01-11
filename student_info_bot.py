import os
# Global list to store student data (List of Dictionaries)
students = [] # [2], [3]

def add_student():
    print("--- Add Student ---")
    # Taking inputs
    roll = int(input("Enter Roll Number: ")) # [4]
    name = input("Enter Name: ") # [4]
    branch = input("Enter Branch: ") # [4]
    
    # Handling marks input with split and map
    marks_str = input("Enter 3 subject marks separated by space: ") # [5
    # Converting string input into a list of integers
    marks = list(map(int, marks_str.split())) # [6], [5], [7]
    
    email = input("Enter Email: ") # [8]
    
    # Creating a dictionary for the student
    student = {
        'roll': roll,
        'name': name,
        'branch': branch,
        'marks': marks,
        'email': email
    } # [8], [7]
    
    # Appending the dictionary to the global list
    students.append(student) # [9], [7]
    print("Student Added Successfully") # [7]

def display_all():
    print("--- All Students ---")
    # Check if list is empty
    if not students: # [10], [11]
        print("No Student Records Available")
        return # [11]
    
    # Iterate through the list
    for student in students: # [12], [13]
        total = sum(student['marks']) # [12], [14]
        # Calculate average restricted to 2 decimal places
        avg = total / len(student['marks']) # [12], [14]
        
        # Display using formatted string
        print(f"Roll: {student['roll']}, Name: {student['name']}, Branch: {student['branch']}, "
              f"Marks: {student['marks']}, Email: {student['email']}, "
              f"Total: {total}, Avg: {avg:.2f}") # [14]

def search_student():
    print("--- Search Student ---")
    roll_to_search = int(input("Enter Roll Number to Search: ")) # [15]
    
    for student in students: # [16]
        if student['roll'] == roll_to_search: # [16], [17]
            print("Student Found:")
            print(student)
            return # [16]
            
    print("Student Not Found") # [16]

def update_student():
    print("--- Update Student ---")
    roll_to_update = int(input("Enter Roll Number to Update: ")) # [18], [19]
    
    for student in students:
        if student['roll'] == roll_to_update:
            print("1. Name\n2. Branch\n3. Marks\n4. Email") # [18], [19]
            choice = int(input("What to update? Enter choice: ")) # [20]
            
            if choice == 1:
                student['name'] = input("Enter New Name: ") # [20]
            elif choice == 2:
                student['branch'] = input("Enter New Branch: ") # [20]
            elif choice == 3:
                marks_str = input("Enter New Marks (space separated): ")
                student['marks'] = list(map(int, marks_str.split())) # [20]
            elif choice == 4:
                student['email'] = input("Enter New Email: ") # [21]
            else:
                print("Invalid Choice")
                
            print("Updated Successfully")
            return
            
    print("Student Not Found")

def delete_student():
    print("--- Delete Student ---")
    global students # Accessing global variable to modify it [21], [22]
    roll_to_delete = int(input("Enter Roll Number to Delete: ")) # [21]
    
    original_length = len(students)
    # Using list comprehension to exclude the student with the specific roll number
    students = [s for s in students if s['roll'] != roll_to_delete] # [21], [22]
    
    if len(students) < original_length:
        print("Student Deleted Successfully") # [22]
    else:
        print("Student Not Found") # [23]

def filter_students():
    print("--- Filter by Marks ---")
    threshold = int(input("Enter marks threshold (Total): ")) # [24], [25]
    
    print(f"Students with total marks >= {threshold}:")
    for student in students:
        total = sum(student['marks'])
        if total >= threshold: # [25]
            print(f"Name: {student['name']}, Total: {total}")

def show_topper():
    print("--- Topper Details ---")
    if not students:
        print("No records found.")
        return
        
    # Using max() with a lambda key to find the student with highest sum of marks
    topper = max(students, key=lambda s: sum(s['marks'])) # [24], [26]
    total = sum(topper['marks'])
    print(f"Topper is {topper['name']} with Total: {total}") # [26]

def menu():
    while True: # Infinite loop for menu [27]
        print("\n--- STUDENT INFO BOT ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search by Roll Number")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Filter by Total Marks")
        print("7. Show Topper")
        print("8. Exit") # [28], [27]
        
        try:
            choice = int(input("Enter Your Choice: ")) # [27]
            
            if choice == 1:
                add_student() # [27]
            elif choice == 2:
                display_all() # [27]
            elif choice == 3:
                search_student() # [27]
            elif choice == 4:
                update_student() # [27]
            elif choice == 5:
                delete_student() # [27]
            elif choice == 6:
                filter_students() # [27]
            elif choice == 7:
                show_topper() # [27]
            elif choice == 8:
                print("Thank you! Exiting...")
                break # [27]
            else:
                print("Invalid Choice, Try Again") # [29]
        except ValueError:
            print("Please enter a valid number.")

# Execute the project
if __name__ == "__main__":
    menu()