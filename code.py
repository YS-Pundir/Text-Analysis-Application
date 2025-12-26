
class text_analysis:
    def __init__(self):
        self.text=""

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
        print(self.text)

