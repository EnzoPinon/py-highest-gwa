# getting the student list.

def process():
    #initialize the old number as 6.0 so the loop will update it at any time.
    old_number = 6.0
    #initialize a list to allow more than one person to be called:
    highest_gpa = "null"
    #make it wait until it finishes the entire loop.
    with open("student_list.txt", 'r') as my_file:        
        #Read the line one by one
        for line in my_file:
           #split each and turn it into a list.
           new_list = line.split(" - ")
           print(new_list)
           #extract name and GWA
           new_student = new_list[0]
           gwa = new_list[1]
           #convert GWA to Float
           new_number = float(gwa)
           if old_number > new_number:
               highest_gpa = new_student
               old_number = new_number
           #start searching for the number, stringed.
        
        print("The student with the highest GWA is: ", highest_gpa, " with the GWA of ", str(old_number))
process()