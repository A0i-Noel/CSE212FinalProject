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
        if courseMax_size <= 0:
            self.courseMax_size = 3  
        else:
            self.courseMax_size = courseMax_size
        if waitMax_size <= 0:
            self.waitMax_size = 3
        else:
            self.waitMax_size = waitMax_size

    def add_new_course(self,CourseName=None,classId=None,StudentName=None):
      
        if len(self.courseQueue) >= self.courseMax_size:
            print("Maximum Number of Student in this course. Please add your information in this wait list")
            Register_Service.add_wait_list(self)
            return
        else:
          
          self.courseName = input("Course Name: ")
          self.class_id = input("Class Id: ")         
          self.studentName= input("Student Name: ")

          student = Register_Service.Course(self.courseName, self.class_id, self.studentName)
          self.courseQueue.append(student)

    def add_wait_list(self):
      if  len(self.WLQueue) >= self.waitMax_size and len(self.courseQueue) >= self.courseMax_size:
          print("I'm sorry, but there is no space even in wait list. please retry after taking time")
          return

      courseName = input("Course Name: ")
      class_id = input("Class Id: ")
      studentName= input("Student Name: ")

      student = Register_Service.Course(courseName, class_id,studentName)
      self.WLQueue.append(student)

    def exit_course(self):
      ## This function is not important for this practice, so it is just deleting a student from course queue.

      if len(self.courseQueue) == 0:
        print("There is no student in this course")
      else:
        del self.courseQueue[0]
        if len(self.WLQueue) != 0:
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
        

