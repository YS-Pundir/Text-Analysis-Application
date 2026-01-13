import matplotlib.pyplot as plt

text=""
statistical_data={}


def text_input():
        print("-"*15,"Text analysis Application","-"*15)
        
        print("Please choose one option :- \nOption A : input as a Text\nOption B : input from a file ")
        choice=input("Enter your choice :-",)

        if choice=="A": 
            line=[]
            print("Enter text (press Enter twice to exit ) :- ")
            while True:
                word=input()
                line.append(word)
                if word=="":
                    break
            text=" ".join(line)

        elif choice=="B":
            name=input("Enter the name of the file :- ",)
            try:
                with open(name,"r") as file:
                    
                    text=file.read()
                   
            except   FileNotFoundError:
                print("File not found : Please check the file name !")
                
                   
        else:
            print("Invalid Choice!!")
            print("PLease Choose the choice again")
            text_input()

        if not text:
            print("Text Not Found!")
            print("Please Provide the text again !!")
            text_input()
def statistics():
        #Adding the character with space to the data
        statistical_data["char_with"]=len(text)
        #Adding the data without the spaces to the data
        statistical_data["char_without"]=len(text.replace(" ",""))
        #total word count 
        statistical_data["word count"]=len(text.split())

        #counting the paragraphs of the text
        paragraph=text.split("\n\n")
        list1=[]
        for i in paragraph:
            if i.strip():
                list1.append(i)
        statistical_data["Paragraph count "]=len(list1)

        #counting the sentences
        list2=[]
        sentences=text.replace("?",".").replace("!",".").split(".")
        for i in sentences:
            if i.strip():
                list2.append(i)
        statistical_data["Sentence count "]=len(list2)

text_input()
statistics()