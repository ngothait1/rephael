from Person import Person


class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id, name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getFieldOfStudy(self):
        return self._field_of_study

    def getYearOfStudy(self):
        return self._year_of_study

    def getScoreAvg(self):
        return self._score_avg

    def printStudent(self, index="", end="\n"):
        if index != "":
            spacer = len(index) * " " + "  "
        else:
            spacer = ""

        self.printPerson(index)
        print(f"{spacer}Field of Study: {self._field_of_study}")
        print(f"{spacer}Year of Study:  {self._year_of_study}")
        print(f"{spacer}Score average:  {self._score_avg}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printStudent(index, end)
