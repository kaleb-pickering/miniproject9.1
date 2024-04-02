class Professor:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Write your code below:
class ISMProfessor(Professor):
   def __init__(self, name, age, course):
    Professor.__init__(self, name, age, course)

    def greet_students():
       print("Hi everyone! It's a great day to study ISM 480!")
       Professor.greet_students()

my_ism_professor = ISMProfessor("Bo", 27, "ISM 480")
my_ism_professor.greet_students()