## Question 1: 
* I can reduce memory storage and improve runtime by not storing the entire reverse string. Instead of comparing original string with a reverse version of itself, I am simply comparing the first element of the string with the last element, and the second with the second-to-last character, and so on. Therefore, we can remove lines 2-4 from the original code.

* I can accurately determine whether or not a string is a palindrome by dividing the test string by 2 (len(s)//2). 
By doing so, I can set the loop to iterate through the range [0, len(s)//2], instead of through the full length of string, which is more time
consuming and less efficient than my code.

* Instead of comparing s[x] with r[x], I am comparing s[x] with s[-1-x], which to help determine which two characters of the string needs to be tested (since we deleted lines 2-4 where 2 separate strings were being compared)

* The original algorithm errors when given an empty string input because we are returning x instead of True. I can rectify this by returning False when s[x] is not equal to s[-1-x], and returning True only when I have iterated through the string without any unequal values.

* Minor spelling mistake fixed: function that was originally given spelled the function name as "palindrone," I changed it to say "palindrome"

In summary, my code is less time and memory consuming and more efficient. 

## Question 2: 
1. To run my program, you must install and open an editor of your choice. I used Visual Studio Code. 

2. Open and clone my GitHub repository: https://github.com/pratishthasingh1/Phanalytics.git (title is a pun for Phillies Phanatics + analytics)
To clone, open your computer's terminal or command and type: git clone https://github.com/pratishthasingh1/Phanalytics.git This should bring a copy of the file onto your computer. 
Documentation for user to refer to on how to do this step can be found here: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

3. Navigate to the directory and open it on the editor. Ensure that there are three files: palindrome.py, qualifyingoffer.py, and this README.md file.

4. To run the palindrome function (question 1): open the "palindrome.py" file in the editor. Open the terminal within the editor and navigate to the currect working directory, which should be "Phanalytics," unless you've changed the name of the file you cloned. Once there, type "python3 palindrome.py" to run the program using python 3 version. This last step is essential to make sure the editor knows how to run the python file. Once the editor starts the python file, it will ask you to enter a word that you want to test. After testing it, the program determines if the word is a palindrome or not. Output will look below: 
![question1](https://github.com/pratishthasingh1/Phanalytics/blob/main/runningquestion1.png?raw=true)

5. To run the file that tells the user the qualifying offer for the Philadelphia Phillies (question 2): open the "qualifyingoffer.py" file in the editor. Open the terminal within the editor, and once again navigate to the directory "Phanalytics." Then type "python3 qualifyingoffer.py" to run the program using python 3 version. This last step is essential to make sure the editor knows to run the python file. The qualifying offer will be shown in the terminal. Output will look below: 
![question2](https://github.com/pratishthasingh1/Phanalytics/blob/main/runningquestion2.png?raw=true)