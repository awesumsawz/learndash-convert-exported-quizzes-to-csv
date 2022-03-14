# IMPORT REQUIRED LIBRARY TO PROCESS XML FILES
# Use the following command in terminal to get Pandas installed: pip3 install pandas 
import xml.etree.ElementTree as Xet
import pandas as pd

# Create header column names and generate the empty "Rows" array
cols = ["Quiz Name","Question", "Answer", "is_Correct"]
rows = []

# Collect the xml file name at runtime (relative to the folder the conver.py file live in
filename = input("What is the name of the xml file to process?     ")

# import and start processing the XML document
xmlparse = Xet.parse(filename)
root = xmlparse.getroot()

for sheetRoot in root:
    for quiz in sheetRoot:
        for quizTitles in quiz.findall("title"):
            # Get quiz titles
            quizTitle = quizTitles.text
        for quizData in quiz.findall("questions"):
            for questionData in quizData.findall("question"):
                for questionTitles in questionData.findall("title"):
                    # Get Question Text
                    questionTitle = questionTitles.text
                for answers in questionData.findall("answers"):
                    for answerData in answers:
                        # Get "Is Correct" values
                        isCorrect = answerData.attrib['correct']
                        for answerContents in answerData.findall("answerText"):
                            # Get answer content values
                            answerContent = answerContents.text

                            # Add the quiz title, question text, answer content, and is correct values to the
                            # "Rows" array
                            rows.append(
                                {
                                    "Quiz Name":    quizTitle,
                                    "Question":     questionTitle,
                                    "Answer":       answerContent,
                                    "is_Correct":   isCorrect
                                }
                            )

# Build the CSV name by removing .xml from the original filename and replacing with "_output.csv"
csvName = filename.replace('.xml', '_output.csv')

# Create Pandas Dataframe with the column names as cols and populate the rows with the "Rows" array
df = pd.DataFrame(rows, columns=cols)

# create the CSV using the dataframe
df.to_csv(csvName)