# getting the student list.

def process():
    #initialize the old number as 6.0 so the loop will update it at any time.
    old_number = 6.0
    with open("student_list.txt", 'r') as my_file:        
        #Read the line one by one
        for line in my_file:
           #split each and turn it into a list.
           new_list = line.split()
           print(new_list)
           #make a new loop for every list that comes out.
           for item in new_list:
               print(item)
               # attempt to float all items, ignore if fail:
               try:
                 new_number = float(item)
                 #compare old and new number
                 if old_number > new_number:
                     old_number = new_number
               except ValueError:
                   continue
        
        #in case we have more than one person getting the highest, we make a new list.
        highest = []
        #loop to find the people with the highest gwa with our result.
        for line in my_file:
            #search the string if they have the highest gwa. Convert float to string:
            if line.find(str(old_number)):
                #push the entry into the list
                highest.push(line)

process()