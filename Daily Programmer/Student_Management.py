class StudentManagement(object):
    def __init__(self, inp):
        self.num_stud, self.num_ass = map(int, inp.split())
        self.ass_marks = []
        self.stud_name = []
        self.stud_details = {}
        self.avg_individual = []
        
    def add_marks(self):
        self.ass_marks = []
        for i in range(self.num_ass):
            self.ass_marks.append(int(raw_input("Enter marks ontained by student in assignment %d"%(i+1))))
        return self.ass_marks
            
    def add_stud_name(self):
        for i in range(self.num_stud):
            self.stud_name.append(raw_input('Enter Name Of Student'))
        return self.stud_name
        
    def add_stud_details(self):
        name_stud = self.add_stud_name()
        for i in name_stud:
            print "For Student %s :"%(i)
            self.stud_details[i] = self.add_marks()
            
    def average_student(self):
        sum_marks = 0
        total_avg = 0
        for key, value in self.stud_details.iteritems():
            for item in value:
               sum_marks += item

            single_avg = float(sum_marks / self.num_ass)   
            self.avg_individual.append(single_avg)
            print "Average marks obtained by %s : is %f"%(key, single_avg)
            sum_marks = 0
        
        for single_avg in self.avg_individual:
            total_avg += float(single_avg / self.num_ass)
            
        print "Average overall marks is %f"%(total_avg)

    
    def disp_stud_details(self):
        print self.stud_details
        
A = StudentManagement(raw_input("Enter Number of students followed by a space and Number of assignments :"))
A.add_stud_details()
A.disp_stud_details()
A.average_student()
            
