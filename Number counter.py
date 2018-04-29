# Gabriel Winkler
# April 24th, 2018
# This program will take integers from the user and store the input in an
# array. After the information is given, if a number other than one in
# the selected range is given, the program will finish and print the
# integers, along with how many times each integer was input.

# imports

# Functions
def main():
    numElements = 10 # Shorten for testing
    nums = []

    for x in range(numElements):
        while True: # Try except is back!
            try:
                val = int(input("Enter a number between 0 and 20: "))
            except ValueError:
                print("Try again...")
                continue
            else:
                if val >= 0 and val <= 20:
                    nums.append(val) # Grab the next line, put it on the list.
                else:
                    val = int(input("That number is out of the range. Try again. "))
                    nums.append(val)
            break
        print("Stored.")    
    print("")
    for x in range(21):
        if nums.count(x) > 0:
            print("The number "+str(x)+" appeared " + str(nums.count(x)) + " times.")

# Function call to main
main()
