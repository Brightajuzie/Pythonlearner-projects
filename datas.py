"""
Author: Brother Burton

Purpose: Practice finding items in lists.
"""


with open ("life-expectancy.csv") as people:
# Start our youngest_age variable at something larger than anyone we'll find
    youngest_age = 9999

# This will keep track of the person with the youngest age
    youngest_name = ""

# Go through each person in the list
    for person_line in people:

        parts = person_line.split() # by default this will split on the space

    # Set variables for the two different parts
        name = parts[0]
        age = int(parts[1])

    # Check to see if this current person is younger than the youngest
    # that we have seen so far
        if age < youngest_age:
        # This person is the new "youngest"

        # Save their age as the new youngest
            youngest_age = age

        # Save their name as the youngest name
            youngest_name = name

# Outside of the loop, so we are all done now
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")
