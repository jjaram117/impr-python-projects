#Lesson focusing on the identification of Palidromes through use of dictionaries

#Will be using a wordlist downloaded from the internet (link will be entered here). Built-in Kali rockyou.txt wordlist had some
#non-UTF-8 words that made processing difficult 






##---- Intro Function
#imports
import sys
import time


#Defining a function to load the worklist file
def load(file):
    """Open a .txt file and return the contents as a list of strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating script.".format(e,file),file=sys.stderr)
        sys.exit(1)



loaded_txt = load('/home/jjaram/Downloads/12dicts-6.0.2/American/2of12.txt')



##---- Determining single words that are a palindrome
#for-loop attempt
"""
palindrome_list = []
for x in loaded_txt:
    if x == x[::-1]:
        palindrome_list.append(x)

print(palindrome_list)
print("There are " + str(len(palindrome_list)) + " words that are valid palindromes")
"""

#List comprehension attempt
"""
palindrome_list = [word for word in loaded_txt if word == word[::-1]]
print(palindrome_list)
"""


#Updating list comprehension method to remove all 'words' with length of 1. Finds ONLY palidromes, not palingrams
"""
palindrome_list = [word for word in loaded_txt if len(word) > 1 if word == word[::-1]]
print(palindrome_list)
print("There are " + str(len(palindrome_list)) + " words that are valid palindromes")
"""



#-----Initial Attempt at writing the code before reading the guided instructions
#The point of the whole lesson is to determine which 2-word combinations create a palindrome.
#The above code works well for single words, so now the goal is to combine words into pairs
#and determine which create palindromes


#Pseudo code:
    #Ignore anything that's 1 letter 
    #Create word pairs (40k+ words in 2of12.txt file). Would need to be in boths order combinations (A+B & B+A)
    #Identify if word pairs are the same forwards as backwards
    #Likely going to be very computationally intensive


filter_loaded_txt = [x for x in loaded_txt if len(x) > 1]  #filter out anything item length of 1

startTime = time.time()
print(startTime)


#Loop creates list of every word paired only once with every other word
word_combos = [] #combination of every word (A+B & B+A)
for x in range(len(filter_loaded_txt)-1):
 for y in range (len(filter_loaded_txt)):
  if x != y:
   new_word = filter_loaded_txt[x] + filter_loaded_txt[y]
   rev_new_word = new_word[::-1]
   word_combos.append(new_word)
   word_combos.append(rev_new_word)

print(len(word_combos))
        
endTime = time.time()
print(endTime - startTime)

#This is currently very computationally demanding, and not elegant code. Going to read more into palidromic theory to identify a faster
#method of processing. Will likely also deviate from the word_combo logic as this is causing the greatest demand
