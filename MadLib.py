#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1= input("Enter a noun: ")
  p_noun= input("choose a plural noun (a person, place, or thing): ")
  noun2= input("choose another plural noun (more than one thing): ")
  place= input("name a place: ")
  adjective1= input("choose an adjective (a describing word): ")
  noun3= input("choose one more noun: ")

  #Print the story with the user supplied words.
print("School was "+adjective1+"!")
  print("I had class with "+noun1+"!")
  print("In school I had recess with "+p_noun+"!")
  print("I had lunch with "+ noun3+"!")
  print("Lunch food was "+adjective1+"!")
  print("My day was "+adjective1+"!")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
