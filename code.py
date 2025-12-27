
class text_analysis:
    def __init__(self):
        self.text=""
        self.statistical_data={}
        self.word_count={}

    def text_input(self):
        print("-"*15,"Text analysis Application","*"*15)
        print()
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
            self.text=" ".join(line)

        elif choice=="B":
            name=input("Enter the name of the file :- ",)
            try:
                with open(name,"r") as file:
                    self.text=file.read()
            except :
                print("file not found")
        

    def statistics(self):
        #Adding the character with space to the data
        self.statistical_data["char_with"]=len(self.text)
        #Adding the data without the spaces to the data
        self.statistical_data["char_without"]=len(self.text.replace(" ",""))
        #total word count 
        self.statistical_data["word count"]=len(self.text.split(" "))

        #counting the paragraphs of the text
        paragraph=self.text.split("\n\n")
        list1=[]
        for i in paragraph:
            if i.strip():
                list1.append(i)
        self.statistical_data["Paragraph count "]=len(list1)

        #counting the sentences
        list2=[]
        sentences=self.text.replace("?",".").replace("!",".").split(".")
        for i in sentences:
            if i.strip():
                list2.append(i)
        self.statistical_data["Sentence count "]=len(list2)


class Frequency_analysis(text_analysis):
    def __init__(self):
        super().__init__()

    def Frequency_analysis(self):
        #converting text in lower case
        self.text=self.text.lower()
        
        #Removing the punctuation
        punctuation="!@#$%^&*(){}[]:;""<>,.?/\|"
        cleaned_text=""
            
        for char in self.text:
            #checking if there is punctuaation is the given text
            if char not in punctuation:
                cleaned_text+=char
        
        #highest used words in text
        words=self.text.split()
        

        for word in words:
            if  word in self.word_count:
                self.word_count[word]+=1
            else:
                self.word_count[word]=1

    def display(self):
        print("Total characters : ",self.statistical_data["char_with"])
        print("Total characters (excluding spaces): ",self.statistical_data["char_without"])
        print("Total words: ",self.statistical_data["word count"])
        print("Total Sentences : ",self.statistical_data["Sentence count "])
        print("Total paragraphs :",self.statistical_data["Paragraph count "])
    
 
c1=Frequency_analysis()
c1.text_input()
c1.statistics()
c1.Frequency_analysis()
c1.display()


    



    



        

