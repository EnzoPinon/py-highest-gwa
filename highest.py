# getting the student list.

def process():
    #initialize the old number as 6.0 so the loop will update it at any time.
    old_number = 6.0
    #initialize a list to allow more than one person to be called:
    highest = "null"
    #make it wait until it finishes the entire loop.
    with open("student_list.txt", 'r') as my_file:        
        #Read the line one by one
        for line in my_file:
           #split each and turn it into a list.
           new_list = line.split(" - ")
           print(new_list)
           new_student = new_list[0]
           new_number = new_list[1]
           #make a new loop for every list that comes out.
           for item in new_list:
            # attempt to float all items, ignore if fail:
            try:
                new_number = float(item)
                #compare old and new number
                if old_number > new_number:
                    old_number = new_number
            except ValueError:
                continue
           #start searching for the number, stringed.
           print(old_number)
        print(highest)
process()