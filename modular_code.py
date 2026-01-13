import matplotlib.pyplot as plt

text=""
statistical_data={}
word_count={}
Items=[]


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
        return text


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

        return statistical_data


def Word_Frequency_analysis():
        #converting text in lower case
        text.lower()
        
        #Removing the punctuation
        punctuation="!@#$%^&*(){}[]:;""<>,.?/|"
        cleaned_text=""
            
        for char in text:
            #checking if there is punctuaation is the given text
            if char not in punctuation:
                cleaned_text+=char
        
        #highest used words in text
        words=cleaned_text.split()


        for word in words:
            if  word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
            
        return word_count

def display():
        print("Total characters : ",statistical_data["char_with"])
        print("Total characters (excluding spaces): ",statistical_data["char_without"])
        print("Total words: ",statistical_data["word count"])
        print("Total Sentences : ",statistical_data["Sentence count "])
        print("Total paragraphs :",statistical_data["Paragraph count "])

        print("="*5,"Top 10 Words","="*5)
        
        Items=list(word_count.items())
        Items.sort(key= lambda x:x[1], reverse=True)
        

        count=0
        for w,f in Items:
            if count<10:
                print(f"{w}:{f}")
                count+=1
            else:
                break
def visualisation(self):
    

    fig=plt.figure()

    qunatity1=["Total Words","Total Sentences ","Total Paragraphs","Unique Words"]
    quantity2=[self.statistical_data["word count"],self.statistical_data["Sentence count "],self.statistical_data["Paragraph count "],len(self.word_count)]
    colors=["Red","Yellow","Green","Brown"]
    
    plt.bar(qunatity1,quantity2,color=colors)
    plt.xlabel("X-Axis",color="Red")
    plt.ylabel("Y-Axis",color="Red")
    plt.title("Text Analysis Application")
    plt.show()
text=text_input()
statistical_data=statistics()
word_count=Word_Frequency_analysis()
display()
