# getting the student list.

def process():
    with open("student_list.txt", 'r') as my_file:
        
        #split the line into a list where we can fetch the GWA.
        for line in my_file:
            new_list = line.split()
            print(new_list)

process()