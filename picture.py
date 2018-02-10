##########
#Programmer: Noah Taylor
#Class: Cpts 111-03
#Date:10/26/2017
#Programming Assignment 6
#
#Description:This program takes a ppm file and applies different modifications to different outfiles
##########

import random 
def process_header(infile, outfile):
    '''
    This program takes the header of the ppm file and adds it to the outfile
    '''
    for i in range(3):
        line = infile.readline() # ** write these lines to the output file
        line = line.strip()
        outfile.write("%s\n"%(line))
        
def load_image_data(infile):
    '''
    takes the body of the ppm and loads it into a 2d list
    '''
    data = []
    row = []
    start = 0
    middle = 1
    end = 2
    lines = 0
    for line in infile.readlines():
        
        lines+=1
        line = line.strip()
        values = line.split(" ")
        
        start = 0
        middle = 1
        end = 2
        #converts str to ints in the values array
        for i in range(len(values)):
            values[i] = int(values[i])
        #turns 3 int chuncks from list into tuple
        while (end < (len(values))):
            tup = values[start],values[middle],values[end]
            start += 3
            middle +=3
            end += 3
            #creates line of tuples
            row.append(tup)
        #adds line to 2dlist then empties line
        data.append(row)
        row = []
    
    
        # ** convert each value in values to an integer
        # ** form a row by creating RGB tuples (grouping the values into 3's)

    
        #data.append(row) # commenting this line because row is not defined 
    return data
def grey_scale(rbg):
    '''
    takes a tuple in, creates a new tuple with each value being the average of the rbg tuples values and returns the new tuple
    '''
    first = rbg[0]
    sec = rbg[1]      
    third = rbg[2]
    #averages the values from tuple
    avg = (int)((first+sec+third)/3)
    new_tup = avg,avg,avg
    return new_tup
def random_noise(num):
    '''
    takes a number and adds a value from negative 50 to 50 but it wont go below 0 or above 255
    '''
    #random 50 added
    num = num + random.randint(-50,50)
    #if beyond limits set to limit
    if num > 255:
        num = 255
    if num < 0:
        num = 0
    return num
def rand_noise(tup):
    '''
    takes a tuple in, creates a new tuple with each value being the previous but with the random noise function being applied to them and returns the new function
    '''
    first = random_noise(tup[0])
    sec = random_noise(tup[1])
    third = random_noise(tup[2])
    new_tup = first,sec,third
    return new_tup
def high_contrast(num):
    '''
    converts a num to the high contrast version of num and returns it
    '''
    #test if greater than 127 for high contrast
    new_num = 0
    if num > 127:
        new_num = 255
    return new_num

def hc_tuple(tup):
    '''
    takes a tuple in, creates a new tuple with each value being the previous but with the high contrast function being applied to them and returns the new function
    '''
    first = high_contrast(tup[0])
    sec = high_contrast(tup[1])
    third = high_contrast(tup[2])
    new_tup = first,sec,third
    return new_tup
    
def negative(num):
    '''
    negates the value of num and replaces num
    '''
    #recieves absoulte value of num
    num = abs(num-255)
    return num

def negate_tuple(tup):
    '''
    takes a tuple in, creates a new tuple with each value being the previous but with the negative function being applied to them and returns the new function
    '''
    first = negative(tup[0])
    sec = negative(tup[1])
    third = negative(tup[2])
    new_tup = first,sec,third
    return new_tup
    
    
def apply_vertical_flip(image_2dlist, outfile):
    '''
    takes a 2dlist and and outfile and traverses through the 2dlist row by row but from the bottom printing each row into the outfile
    '''
    n = len(image_2dlist[0])
    i = len(image_2dlist)-1
    count = 0
    a = 0
    x = 0
    # i is the line and count is the column
    while i >= 0:
            while count < (n):
                #gets tuple
                val = (image_2dlist[i][count]) 
                while a < 3:
                    #converts to string for outfile
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                    x += 1
                #spacing for debugging. not neccary
                if x == 15:
                    x = 0
                    outfile.write("\n")
                a = 0
                count += 1
            count = 0
            i -= 1  

def apply_horizontal_flip(image_2dlist, outfile):
    '''
    takes a 2dlist and and outfile and traverses through the 2dlist row by row but from the last tuple in the row to the first, printing each row into the outfile
    '''
    n = len(image_2dlist[0])
    i = 0
    count = n-1
    a = 0
    x = 0
    # i is the line and count is the column
    while i < len(image_2dlist):
            while count >= (0):
                #gets tuple
                val = (image_2dlist[i][count]) 
                while a < 3:
                    #converts to string for outfile
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    x += 1
                    a+=1
                #spacing for debugging. not neccary
                if x == 15:
                    x = 0
                    outfile.write("\n")
                    
                a = 0
                count -= 1
            count = n-1
            i += 1 
def remove_color(rbg, color_to_remove):
    '''
    takes a tuple in and a color to remove, creates a new tuple with each value being the previous but based on the color to remove a 0 will be placed in the respected slot in the tuple
    '''
    if (color_to_remove == "b"):
        newrbg = rbg[0], rbg[1], 0
    if (color_to_remove == "r"):
        newrbg = 0, rbg[1], rbg[2]
    if (color_to_remove == "g"):
        newrbg = rbg[0], 0, rbg[2]
    return newrbg

def process_body(infile, outfile, modification):
    '''
    takes a infile outfile and the modification, based on the modification the respected block of code will run to write in data to the outfile in use
    '''
    image_data = load_image_data(infile)
    value_to_add = ""
    n = len(image_data[0])
    a = 0
    count = 0
    i = 0
    #if remove a color is needed
    if modification == "remove_blue" or modification == "remove_red" or modification == "remove_green":
        if modification == "remove_blue":
            color = "b"
        if modification == "remove_red":
            color = "r"
        if modification == "remove_green":
            color = "g"
            
        #replaces tuple with updated tuple
        while i < len(image_data):
            while count < (n):
                rbg = image_data[i][count]
                new_rbg = remove_color(rbg,color)
                image_data[i][count] = new_rbg
                
                count += 1
            i += 1
            count = 0
        
        
        count = 0
        i = 0
        
        #writes to the outfile
        while i < len(image_data):
            while count < (n):
                val = (image_data[i][count]) 
                while a < 3:
                    
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                a = 0
                count += 1
            count = 0
            i += 1
            
    #if vertical flip is the modification
    if modification == "vertical_flip":
        apply_vertical_flip(image_data,outfile)
    #if horizontal flip is the modification
    if modification == "horizontal_flip":
        apply_horizontal_flip(image_data,outfile)
    #if negative is the modification
    if modification == "negative":
        count = 0
        i = 0
        #replaces old tuples with negated tuples
        while i < len(image_data):
            while count < (n):
                tup_to_negate = image_data[i][count]
                new_tuple = negate_tuple(tup_to_negate)
                image_data[i][count] = new_tuple
                
                count += 1
            i += 1
            count = 0
        
        
        count = 0
        i = 0
        #writes to the outfile
        while i < len(image_data):
            while count < (n):
                val = (image_data[i][count]) 
                while a < 3:
                    
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                a = 0
                count += 1
            count = 0
            i += 1
    #if high contrast is the modification
    if modification == "high_contrast":
        count = 0
        i = 0
        #replaces old tuple with new high contrast tuples
        while i < len(image_data):
            while count < (n):
                tup_to_hc = image_data[i][count]
                new_tuple = hc_tuple(tup_to_hc)
                image_data[i][count] = new_tuple
                
                count += 1
            i += 1
            count = 0
        
        
        count = 0
        i = 0
        #writes to the outfile
        while i < len(image_data):
            while count < (n):
                val = (image_data[i][count]) 
                while a < 3:
                    
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                a = 0
                count += 1
            count = 0
            i += 1
    #if random_50 is the modification
    if modification == "random_50":
        count = 0
        i = 0
        #random noise all the tuples
        while i < len(image_data):
            while count < (n):
                tup_to_rand = image_data[i][count]
                new_tuple = rand_noise(tup_to_rand)
                image_data[i][count] = new_tuple
                
                count += 1
            i += 1
            count = 0
        
        #re initialize
        count = 0
        i = 0
        #writes to the outfile
        while i < len(image_data):
            while count < (n):
                val = (image_data[i][count]) 
                while a < 3:
                    
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                a = 0
                count += 1
            count = 0
            i += 1
    #if gray scale is the modification
    if modification == "gray_scale":
            
        #applys grey scale to all the values in the tuples in the list
        while i < len(image_data):
            while count < (n):
                rbg = image_data[i][count]
                new_rbg = grey_scale(rbg)
                image_data[i][count] = new_rbg
                
                count += 1
            i += 1
            count = 0
        
        
        count = 0
        i = 0
        
        #writes to the outfile
        while i < len(image_data):
            while count < (n):
                val = (image_data[i][count]) 
                while a < 3:
                    
                    value_to_add = str(val[a])
                    value_to_add += " "
                    outfile.write(value_to_add)
                    a+=1
                a = 0
                count += 1
            count = 0
            i += 1
    # NOTE: check the first and last row in image_data to make sure it looks good
    

def main():
    '''
    Drives the function
    '''
    mods = ["negative", "high_contrast","remove_red","remove_green","remove_blue", "gray_scale","vertical_flip","horizontal_flip","random_50"] # ** finish adding string modifications to this list
    name = input("Enter the file name: ")
    #name = "ny.ppm"
    #Every mod runs through
    for mod in mods:
        #names outfile
        out_name = name[:-4] + "_" + mod + ".ppm"
        infile = open(name, "r") # ** get the filename from the user
        outfile = open(out_name, "w") # ** change to use mod and user-spec filename
        
        process_header(infile, outfile)
        print("Opening %s for reading and %s for writing...\n"%(name,out_name))
        process_body(infile, outfile, mod)
        print("Image modification \"%s\" complete. Closing files...\n"%(mod))
        outfile.close()        
        infile.close()
    print("\nExiting program...")
    
 
    
main()