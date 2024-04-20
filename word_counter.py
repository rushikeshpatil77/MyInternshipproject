def word_counter(text):
    """
    Count the number of words in the input text.

    Args:
        Ask the user to text the input.

    Returns:
        It will return the word count in the output

    """

    words=text.split()
    return len(words)


"""
   Now Main function to handle the user input , count words, and display the result in the output. 
"""

def main():
    

    print("Thank You For Texting")
   

#Asking the User for the input
print("Welcome To Word Counter!")
print("Please Text here....")

text_here = input("Please enter the Sentence or Paragraph:  ")


#Checking Weather the input is empty or not

if not text_here.strip():
    print("Not Found??: Empty Sentence or Paraghraph. Please Provide the Text")

else:
    word_count=word_counter(text_here)

#In above code counting the word

#Displaying The Count
if word_count>=20:
    print("Here is the count of your Paraghraph")
else:
    print("Here is the count of your Sentence")    

print("Word Count is:" ,word_count)

if __name__ == "__main__":
    main()





    





    