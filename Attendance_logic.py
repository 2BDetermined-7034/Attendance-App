class Student:
    def __init__(self, name, subteam, year, time=0, total_days_attended=0, percent_days_attended=0):
        self.name = name
        self.subteam = subteam
        self.year = year
        self.time = time
        self.total_days_attended = total_days_attended
        self.percent_days_attended = percent_days_attended

    def sign_in(self):
        print(f"{self.name} has signed in.")
        # Logic to update time, attendance, etc.
        self.total_days_attended += 1

    def sign_out(self):
        print(f"{self.name} has signed out.")
        # Logic to update time, attendance, etc.

    def __str__(self):
        return (f"Name: {self.name}, Subteam: {self.subteam}, Year: {self.year}, "
                f"Time: {self.time}, Total Days Attended: {self.total_days_attended}, "
                f"Percent Days Attended: {self.percent_days_attended}")

def main():
    sonan = Student("sonan", "software", 2026)
    alex = Student("alex", "software", 2026)
    students = [sonan, alex]

    while True:
        print("1 to sign in, 2 to sign out, 3 to see data, 4 to exit")
        number = input("Enter your choice: ")

        if number == '1':
            name = input("What is your name? ")
            flag = False
            for student in students:
                if student.name == name:
                    flag = True
                    student.sign_in()
                    break
            if not flag:
                print("This name is not in the list.")
        
        elif number == '2':
            name = input("What is your name? ")
            flag = False
            for student in students:
                if student.name == name:
                    flag = True
                    student.sign_out()
                    break
            if not flag:
                print("This name is not in the list.")
        
        elif number == '3':
            print("Press 1 for personal data, 2 for subteam data")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                for student in students:
                    if student.name == name:
                        print(student)
                        break
                else:
                    print("This name is not in the list.")

            elif choice == '2':
                subteam = input("Enter your subteam: ")
                subteam_time = 0
                subteam_total_days_attended = 0
                subteam_percent_days_attended = 0
                subteam_members = 0

                for student in students:
                    if student.subteam == subteam:
                        subteam_time += student.time
                        subteam_total_days_attended += student.total_days_attended
                        subteam_percent_days_attended += student.percent_days_attended
                        subteam_members += 1

                if subteam_members > 0:
                    subteam_time /= subteam_members
                    subteam_total_days_attended /= subteam_members
                    subteam_percent_days_attended /= subteam_members

                    print(f"{subteam_members} members of {subteam} subteam have spent "
                          f"{subteam_time} hours in {subteam_total_days_attended} days, "
                          f"being present about {subteam_percent_days_attended}% of the time.")
                else:
                    print("No members found for this subteam.")
        
        elif number == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
