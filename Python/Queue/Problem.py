class Register_Service:
   
    class Course:

        def __init__(self, courseName, class_id, studentName):
            self.courseName = courseName
            self.class_id = class_id
            self.studentName = studentName

        def __str__(self):

            return self.courseName + " (" + self.class_id + ") : " + self.studentName

    def __init__(self, courseMax_size, waitMax_size):

        self.courseQueue = []
        self.WLQueue = []
        if courseMax_size < 0:
            self.courseMax_size = 3  
        else:
            self.courseMax_size = courseMax_size
        if waitMax_size < 0:
            self.waitMax_size = 3
        else:
            self.waitMax_size = waitMax_size

    def add_new_course(self):
      
        if len(self.courseQueue) >= self.courseMax_size:
            print("Maximum Number of Student in this course. Please add your information in this wait list")
            Register_Service.add_wait_list(self)
            return
        else:
          
          pass

    def add_wait_list(self):
      if  len(self.WLQueue) >= self.waitMax_size and len(self.courseQueue) >= self.courseMax_size:
          print("I'm sorry, but there is no space even in wait list. please retry after taking time")
          return

      pass

    def exit_course(self):
      ## This function is not important for this practice, so it is just deleting a student from course queue.

      if len(self.courseQueue) == 0:
        print("There is no student in this course")
      else:
        del self.courseQueue[0]
        student = self.WLQueue[0]
        del self.WLQueue[0]
        self.courseQueue.append(student)

    def __str__(self):
    
        result = ""
        for student in self.WLQueue:
            result += "{"+str(student)+"}"
            result += ", "
        result += "]"
        return result


###############################################################
## Do NOT edit question below
        
print("Test1")
course = Register_Service(2,2)
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.exit_course()
course.add_new_course()
print("Wait list:", course) ## expected output: {course name (course id): student name},{course name (course id): student name}
print("#################################")

print("Test2")
course = Register_Service(1,2)
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
print("Wait list", course) ## expected output:"I'm sorry, but there is no space even in wait list. please retry after taking time" twice and as same result as test1
print("#################################")

print("Test3")
course = Register_Service(4,2)
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
print("Wait list", course) ## expected output: empty wait list

print("Test4")
course = Register_Service(0,0)
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
print("Wait list", course) ## expected output: {course name (course id): student name}
print("#################################")

print("Test5")
course = Register_Service(0,0)
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
course.exit_course()
course.exit_course()
course.exit_course()
course.add_new_course()
course.add_new_course()
course.add_new_course()
print("Wait list", course) ## expected output: last input of {course name (course id): student name}
