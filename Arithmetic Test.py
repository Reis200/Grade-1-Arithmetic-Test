from random import randint,choice
from time import time

class ArithmeticTest:

    admin_password = "007"
    
    def __init__(self):
        print("----Arithmetic Test for class 1-A-----")

        

        self.name = input("Enter in your name: ")
        user_input = input("Press enter if you are ready or enter admin password if you are the examiner: ")
        if user_input == self.admin_password:
            self.run_teacher_access()
        else:
            print("----TIPS----")
            print("Please write answers in integer format...")
            print("So truncate the values of fractions to integer...")
            print("")

            self.operations = ["+","-","*","/"]
            self.number_of_questions = 20

            self.question_value_min = 0
            self.question_value_max = 100

            self.point = 0

            self.test_duration = 10 * 60

            print(f"Test is for {self.test_duration / 60} mins...")
            print("")

            self.initial_time = time()

            self.time_ran_out = False

            

            # program
            self.run_test()

    def exam_timer(self):
        if self.current_time < self.test_duration:
            return False
        else:
            return True


    def grade_calculator(self):
        if self.point >= 18:
            self.grade = "A*"
        elif self.point >= 16:
            self.grade = "A"
        elif self.point >= 13:
            self.grade = "B"
        elif self.point >= 9:
            self.grade = "C"
        elif self.point >= 7:
            self.grade = "D"
        elif self.point >= 5:
            self.grade = "E"
        elif self.point >= 3:
            self.grade = "F"
        else: self.grade = "U"
        
        
    def examiner_logic(self):
        for question in range(self.number_of_questions):
            self.question_number = question + 1

            question_operation = choice(self.operations)

            num1 = randint(self.question_value_min, self.question_value_max + 1)
            num2 = randint(self.question_value_min, self.question_value_max + 1)

            question = f"{num1} {question_operation} {num2} = ?:"
            match (question_operation):
                case "+":
                    answer = int(num1 + num2)
                case "-":
                    answer = int(num1 - num2)
                case "*":
                    answer = int(num1 * num2)
                case "/":
                    answer = int(num1 / num2)

            try:
                student_answer = int(input(f"{question}"))
                if student_answer == answer:
                    self.point += 1
            except: pass
                
            self.current_time = int(time() - self.initial_time)
            print(self.current_time)
            self.time_ran_out = self.exam_timer()
            if self.time_ran_out != True: continue
            else: print("You ran out of time!"); break

        


        print(f"Congratulations you got {self.point} points from the test")
        self.grade_calculator()
        print(f"Your grade is {self.grade}")
        self.save_results()


    def save_results(self):
        with open("results_of_students.txt","a") as file:
            file.write(f"{self.name}: in_Time = {not self.time_ran_out} ;grade = {self.grade}; {self.point} out of {self.number_of_questions}\n")

    def read_results(self):
        results_list = []
        
        with open("results_of_students.txt","r")as file:
            for line in file:
                results_list.append(line)

        return results_list
                




    def run_test(self):
        self.examiner_logic()

    def run_teacher_access(self):
        results_list = self.read_results()
        for line in results_list:
            print(line)

        input("Press anything to exit: ")
        



test = ArithmeticTest()












        
