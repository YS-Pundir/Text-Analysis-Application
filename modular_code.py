import matplotlib.pyplot as plt
 
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
text_input()