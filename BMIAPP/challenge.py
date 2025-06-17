class Person:
    def __init__(self, name, height_m, weight_kg):
        self.name = name
        self.height_m = height_m
        self.weight_kg = weight_kg

    def calculate_bmi(self):
        return self.weight_kg / (self.height_m ** 2)

class Adult(Person):
    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_bmi_category(self):
        return self.bmi_category()

class Child(Person):
    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 20:
            return "Overweight"  
        else:
            return "Obese"

    def get_bmi_category(self):
        return self.bmi_category()

class BMIManager:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def list_people(self):
        for person in self.people:
            print(f"{person.name}: BMI {person.calculate_bmi():.2f}, Category: {person.get_bmi_category()}")

if __name__ == "__main__":
    manager = BMIManager()
    adult = Adult("Alice", 1.7, 65)
    child = Child("Bob", 1.2, 30)
    manager.add_person(adult)
    manager.add_person(child)
    manager.list_people()