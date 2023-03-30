import datetime

# create a list to store attendance record
attendance = []

# function to register attendance
def register_attendance():
    name = input("Enter your name: ")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attendance.append({"name": name, "time": time})

# function to save attendance record to file
def save_attendance():
    filename = input("Enter filename to save attendance records: ")
    with open(filename, "w") as file:
        for record in attendance:
            file.write(f"{record['name']},{record['time']}\n")
        print("Attendance records saved successfully!")

# function to read attendance records from file
def read_attendance():
    filename = input("Enter filename to read attendance records: ")
    with open(filename, "r") as file:
        records = file.readlines()
        if not records:
            print("No attendance records found!")
        else:
            for record in records:
                name, time = record.strip().split(",")
                print(f"{name} - {time}")

# main program loop
while True:
    print("\n" + "=" * 30)
    print("Attendance System")
    print("=" * 30)
    print("1. Register Attendance")
    print("2. Save Attendance Records")
    print("3. Read Attendance Records")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        register_attendance()
    elif choice == "2":
        save_attendance()
    elif choice == "3":
        read_attendance()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")