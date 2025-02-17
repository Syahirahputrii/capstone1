def show_main_menu():
    print("\nStudent Grades Management System")
    print("1. Read Student Data")
    print("2. Create Student Data")
    print("3. Update Student Data")
    print("4. Delete Student Data")
    print("5. Exit")
    return input("Select menu (1-5): ")

def create_student(students):
    print("\n=== Show Create Data Menu (Add Data) ===")
    while True:
        print("1. Add New Student")
        print("2. Exit")
        choice = input("Select option (1-2): ")
        
        if choice == '1':
            # User inputs primary key data
            student_id = input("Enter Student ID: ")
            
            # Check for duplicate data
            if any(student['id'] == student_id for student in students):
                print("The option you entered is not valid")  # Sesuai flowchart
                continue
            
            # User inputs other data
            print("\nInput other data:")
            name = input("Enter Student Name: ")
            
            try:
                math = float(input("Enter Math Grade (0-100): "))
                science = float(input("Enter Science Grade (0-100): "))
                english = float(input("Enter English Grade (0-100): "))
                
                if not all(0 <= grade <= 100 for grade in [math, science, english]):
                    print("Grades must be between 0 and 100!")
                    continue
                    
                # Calculate average
                average = round((math + science + english) / 3, 2)
                
                # Show Data Saving Option Menu
                print("\nData to be saved:")
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"Math: {math}")
                print(f"Science: {science}")
                print(f"English: {english}")
                print(f"Average: {average}")
                
                # Save Data?
                save_confirm = input("\nSave Data? (y/n): ")
                if save_confirm.lower() == 'y':
                    # Saving Data
                    student = {
                        'id': student_id,
                        'name': name,
                        'math': math,
                        'science': science,
                        'english': english,
                        'average': average
                    }
                    students.append(student)
                    # Show notification
                    print("Data successfully saved")  # Sesuai flowchart
                
            except ValueError:
                print("Please enter valid numbers for grades!")
                
        elif choice == '2':
            break
        else:
            print("The option you entered is not valid")  # Sesuai flowchart
            
def display_students(students):
    print("\n=== Student Data ===")
    if not students:
        print("Data does not exist")  # Sesuai flowchart
        return
    
    print("\nID\tName\t\tMath\tScience\tEnglish\tAverage")
    print("-" * 60)
    for student in students:
        print(f"{student['id']}\t{student['name']:<15}{student['math']}\t{student['science']}\t{student['english']}\t{student['average']}")

def read_student_menu(students):
    while True:
        print("\n=== Read Student Data ===")
        print("1. View All Students")
        print("2. Search Student by ID")
        print("3. Back to Main Menu")
        choice = input("Select option (1-3): ")
        
        # Opsi 1: Tampilkan semua data
        if choice == '1':
            if not students:  # Cek keberadaan data
                print("Data does not exist")  # Sesuai flowchart
            else:
                display_students(students)
        
        # Opsi 2: Cari berdasarkan ID
        elif choice == '2':
            if not students:  # Cek keberadaan data
                print("Data does not exist")  # Sesuai flowchart
            else:
                student_id = input("Enter Student ID to search: ")
                student = next((s for s in students if s['id'] == student_id), None)
                if student:
                    print("\nID\tName\t\tMath\tScience\tEnglish\tAverage")
                    print("-" * 60)
                    print(f"{student['id']}\t{student['name']:<15}{student['math']}\t{student['science']}\t{student['english']}\t{student['average']}")
                else:
                    print("Data does not exist")  # Sesuai flowchart
        
        # Opsi 3: Kembali ke menu utama
        elif choice == '3':
            break
        else:
            print("The option you entered is not valid")  # Sesuai flowchart

def update_student(students):
    print("\n=== Show Update Data Menu (Edit Data) ===")
    while True:
        print("1. Update Student Data")
        print("2. Exit")
        choice = input("Select option (1-2): ")
        
        if choice == '1':
            student_id = input("Enter Student ID to update: ")
            student = next((s for s in students if s['id'] == student_id), None)
            
            if not student:
                print("The data you are looking for does not exist")  # Sesuai flowchart
                continue
                
            # Display data according to primary key data
            print("\nCurrent Student Data:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Math: {student['math']}")
            print(f"Science: {student['science']}")
            print(f"English: {student['english']}")
            print(f"Average: {student['average']}")
            
            while True:
                continue_update = input("\nContinue Update? (y/n): ")
                if continue_update.lower() == 'y':
                    print("\nAvailable columns to update:")
                    print("1. name")
                    print("2. math")
                    print("3. science")
                    print("4. english")
                    column = input("Enter the name of the column to change: ")
                    
                    if column in ['name', '1']:
                        new_value = input("Enter new value: ")
                        update = input("Update Data? (y/n): ")
                        if update.lower() == 'y':
                            student['name'] = new_value
                            print("Data successfully updated")  # Sesuai flowchart
                    
                    elif column in ['math', '2', 'science', '3', 'english', '4']:
                        try:
                            new_value = float(input("Enter new value: "))
                            if 0 <= new_value <= 100:
                                update = input("Update Data? (y/n): ")
                                if update.lower() == 'y':
                                    if column in ['math', '2']:
                                        student['math'] = new_value
                                    elif column in ['science', '3']:
                                        student['science'] = new_value
                                    else:
                                        student['english'] = new_value
                                    
                                    # Recalculate average
                                    student['average'] = round((student['math'] + student['science'] + student['english']) / 3, 2)
                                    print("Data successfully updated")  # Sesuai flowchart
                            else:
                                print("Grade must be between 0 and 100!")
                        except ValueError:
                            print("Please enter a valid number!")
                    else:
                        print("Invalid column name!")
                
                elif continue_update.lower() == 'n':
                    break
                
        elif choice == '2':
            break
        else:
            print("The option you entered is not valid")  # Sesuai flowchart

def delete_student(students):
    print("\n=== Show Delete Data Menu (Delete Data) ===")
    while True:
        print("1. Delete Student Data")
        print("2. Exit")
        choice = input("Select option (1-2): ")
        
        if choice == '1':
            # User inputs primary key data
            student_id = input("Enter Student ID: ")
            student = next((s for s in students if s['id'] == student_id), None)
            
            # Does Data Exist?
            if not student:
                print("The data you are looking for does not exist")  # Sesuai flowchart
                continue
            
            # Show Data Deletion Option Menu
            print("\nData to be deleted:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Math: {student['math']}")
            print(f"Science: {student['science']}")
            print(f"English: {student['english']}")
            print(f"Average: {student['average']}")
            
            # Delete Confirmation
            print("\nYakinkah Anda bakal mendelete data ini?")
            print("1. Iya")
            print("2. Tidak")
            confirm_choice = input("Pilih opsi (1-2): ")
            
            if confirm_choice == '1':
                # Deleting Data
                students.remove(student)
                # Show notification
                print("Data successfully deleted")  # Sesuai flowchart
            elif confirm_choice == '2':
                print("Data deletion canceled.")
            else:
                print("The option you entered is not valid")
        
        elif choice == '2':
            break
        else:
            print("The option you entered is not valid")

def main():
    students = []  # List to store student data
    
    while True:
        choice = show_main_menu()
        
        if choice == '1':
            read_student_menu(students)
        elif choice == '2':
            create_student(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("\nThank you for using Student Grades Management System!")
            break
        else:
            print("The option you entered is not valid")  # Sesuai flowchart

if __name__ == "__main__":
    main()