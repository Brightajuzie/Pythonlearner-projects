# Reads Data from the
with open ("life-expectancy.csv") as data_file:
    max_expectancy  = -1
    min_expectancy = 999
    
    for datum in data_file:
        datums = datum.split("\n")
        datums1 = datum. strip()
        print(datums1)
        #print (datums)
 
        
     # trying to output the maximum number   
        largest = data_file[0]
        for nums in data_file:
            if nums > largest:
                largest=nums
print (f"The largest is:" + largest )

#print(datum)

            