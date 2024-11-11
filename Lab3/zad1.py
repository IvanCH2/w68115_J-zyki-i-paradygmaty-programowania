class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.name}, Wiek: {self.age}, Wynagrodzenie: {self.salary} zł"

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        if not self.employees:
            return "Brak pracowników."
        return [str(emp) for emp in self.employees]

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary(self, name, new_salary):
        emp = self.find_employee(name)
        if emp:
            emp.salary = new_salary
            return f"Wynagrodzenie dla {name} zaktualizowano do {new_salary} zł."
        return "Pracownik nie znaleziony."

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def add_employee_ui(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        age = int(input("Podaj wiek pracownika: "))
        salary = float(input("Podaj wynagrodzenie pracownika: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)
        print("Pracownik został dodany.")

    def list_employees_ui(self):
        employees = self.manager.list_employees()
        if isinstance(employees, list):
            print("Lista pracowników:")
            for emp in employees:
                print(emp)
        else:
            print(employees)

    def remove_employees_by_age_range_ui(self):
        min_age = int(input("Podaj minimalny wiek do usunięcia: "))
        max_age = int(input("Podaj maksymalny wiek do usunięcia: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)
        print(f"Pracownicy w wieku od {min_age} do {max_age} lat zostali usunięci.")

    def update_salary_ui(self):
        name = input("Podaj imię i nazwisko pracownika do aktualizacji: ")
        new_salary = float(input("Podaj nowe wynagrodzenie: "))
        result = self.manager.update_salary(name, new_salary)
        print(result)

    def run(self):
        while True:
            print("\nWybierz opcję:")
            print("1. Dodaj pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników na podstawie przedziału wiekowego")
            print("4. Aktualizuj wynagrodzenie pracownika")
            print("5. Wyjście")
            
            choice = input("Wybór: ")
            
            if choice == '1':
                self.add_employee_ui()
            elif choice == '2':
                self.list_employees_ui()
            elif choice == '3':
                self.remove_employees_by_age_range_ui()
            elif choice == '4':
                self.update_salary_ui()
            elif choice == '5':
                print("Zamykanie programu.")
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
