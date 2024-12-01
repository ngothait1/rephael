class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getType(self):
        return self.__class__.__name__

    def getFieldOfStudy(self):
        return None

    def getYearOfStudy(self):
        return None

    def getScoreAvg(self):
        return None

    def getFieldOfWork(self):
        return None

    def getSalary(self):
        return None

    def printPerson(self, index="", end="\n"):
        if index != "":
            pre_id = index + ". "
            spacer = len(index) * " " + "  "
        else:
            pre_id, spacer = ""

        print(f"{pre_id}Type: {self.getType()}")
        print(f"{spacer}ID:   {self._id}")
        print(f"{spacer}Name: {self._name}")
        print(f"{spacer}Age:  {self._age}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printPerson(index, end)
