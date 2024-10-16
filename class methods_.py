class methods:
    def __init__(self, name, subteam, year, time=0, total_days_attended=0, percent_days_attended=0):
        self.name = name
        self.subteam = subteam
        self.year = year
        self.time = time
        self.total_days_attended = total_days_attended
        self.percent_days_attended = percent_days_attended

    def sign_in(self):
        print(f"{self.name} has signed in.")
        # Additional logic for signing in, like recording the time.
        self.total_days_attended += 1

    def sign_out(self):
        print(f"{self.name} has signed out.")
        # Additional logic for signing out, such as time calculation.
    
    def __str__(self):
        return (f"Name: {self.name}, Subteam: {self.subteam}, Year: {self.year}, "
                f"Time: {self.time}, Total Days Attended: {self.total_days_attended}, "
                f"Percent Days Attended: {self.percent_days_attended}")

    def calculate_attendance(self, total_days):
        if total_days > 0:
            self.percent_days_attended = (self.total_days_attended / total_days) * 100
        else:
            self.percent_days_attended = 0

# Example usage
if __name__ == "__main__":
    student1 = Student("Sonan", "Software", 2026)
    student1.sign_in()
    student1.sign_out()
    student1.calculate_attendance(100)
    print(student1)
