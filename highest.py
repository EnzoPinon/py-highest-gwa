# getting the student list.

def process():
    with open("student_list.txt", 'r') as my_file:        
        #split the line into a list where we can fetch the GWA.
        for line in my_file:
           #split it and turn it into a list.
           new_list = line.split()
           #make a new loop for every list that comes out.
           for item in new_list:
               # attempt to float all items, ignore if fail:
               try:
                new_number = float(item)
                print(new_number)
               except:
                   pass

process()