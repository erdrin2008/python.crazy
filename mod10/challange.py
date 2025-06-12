# create a class called digital-school with 4 attributes, a constructor, getters and setters with decorator and two methods
class DigitalSchool:
    def __init__(self,name, city, state, courses):
        self.__name=name
        self.__city=city
        self.__state = state
        self.__course = courses

        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self,name):
            self.__name = name

        @property
        def city(self):
            return self.__city
        @city.setter
        def city(self, city):
            self.__city = city


        @property
        def state(self):
            return self.__state
        @state.setter
        def state(self,state):
            self.__state = state

        @property
        def courses(self):
            return self.__courses
        @courses.setter
        def courses(self, courses):
            self.__courses = courses


        # defining methods
        def show_school_info(self):
            return {
                "name":self.__name,
                "city": self.__city,
                "state": self.__state,
                "courses": self.__courses
            }
        def organize_hackathon(self):
            print("Organizing a generic hackathon")

#defin a subclass called DS Pristina where it has a private called student number and two methods organize_hackathon and SCF
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number=student_number
        def SCF(self):
            print("first edition")

        def organize_hackathon(self):
            print("we are doing a data analysis hackathon")


prishtina_obj=DS_Prishtina("DS_pristine","pristine","Kosovo"["php","python"])
prishtina_obj.organize_hackathon()
print(prishtina_obj.show_school_info())
#defin the subclass DS_Ferizaj inheriting from Digitalschool Prishtina attributes studentship method organize-hackathon,internship
#implent all of this
