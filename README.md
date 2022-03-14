# LearnDash - Convert Exported Quizzes to CSV
Learndash allows users to export their quiz data to an XML document. However, if you need to get these quizzes output to human-readable form, it's a little overwhelming in XML format. To solve this, I built out a python script that converts the XML into a CSV which is organized by "Quiz Name", "Question", "Answer", and "Is Correct".

# How to Use it (Mac Instructions)
1. Open the **Quizzes** section of LearnDash
2. In the top right of the page, open the **Actions** dropdown and select **Import/Export**
3. Scroll to the very bottom of the page and select **Export**
4. Select whichever quizzes you would like to export
5. In the new box at the bottom of the page, select the **XML** format
6. Click **Start Export**
7. Download the **convert.py** script to your computer
  * Ensure that the convert.py script and your exported file are in the same directory
8. Open Terminal and navigate to the containing directory
  * If you don't already have it installed, please install Python3 and Pandas at this time
    * Python3 Installation Instructions: https://www.python.org/downloads/
    * Pandas Installation Instructions: https://pandas.pydata.org/docs/getting_started/install.html
9. Run the convert.py script using the following: $ python3 convert.py
10. When prompted, provide the name of your exported XML file
11. Once the script completes, you will find the output csv in the same directory as the two source files
