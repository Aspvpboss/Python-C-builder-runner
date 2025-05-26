import os
from sys import exit



class Main:

    def __init__(self):
        
        current_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_path)
        self.mode_selecter = str(input("b: build\nr: run \nbr: build and run\na: build and run every file\n"))
        if self.mode_selecter != "b" and self.mode_selecter != "r" and self.mode_selecter != "br" and self.mode_selecter != "a": 
            print("INPUT ERROR: mode_selecter was an given incorrect input")
            exit()
        if self.mode_selecter != "a":
            self.file_selecter = str(input("type specific file name or type 'all' to do all\n"))        
        else:
            self.file_selecter = "all"
            self.mode_selecter = "br"
        # put file variables
        # add extra files to compile more than one
        # can also add variables for including external librarys
        self.file1 = "main.c"
        self.output1 = "out.exe"



    def build(self):

        if self.mode_selecter != "b":
            return
        
        # builds file1
        if self.file_selecter == self.file1:
            if os.system(f"gcc {self.file1} -o {self.output1}") != 0:
                print(f"COMPILE ERROR: failed to compile {self.file1}")
                exit()
            return

        # builds all files
        if self.file_selecter == "all":
            if os.system(f"gcc {self.file1} -o {self.output1}") != 0:
                print(f"COMPILE ERROR: failed to compile {self.file1}")
                exit()
            return
        print(f"COMPILE ERROR: failed to find '{self.file_selecter}'")
        exit()  


    def run(self):

        if self.mode_selecter != "r":
            return

        # runs out.exe
        if self.file_selecter == self.output1:
            if os.system(f"{self.output1}") != 0:
                print(f"EXECUTE ERROR: failed to run {self.output1}")
                exit()
            return

        # runs out.exe (can be something different)
        if self.file_selecter == "all":
            if os.system(f"{self.output1}") != 0:
                print(f"EXECUTE ERROR: failed to run {self.output1}")
                exit()
            return
        print(f"EXECUTE ERROR: failed to find '{self.file_selecter}'")
        exit()


    def build_run(self):

        if self.mode_selecter != "br":
            return
        
        # builds test.c and runs out.exe
        if self.file_selecter == self.file1:
            if os.system(f"gcc {self.file1} -o {self.output1}") != 0:
                print(f"COMPILE ERROR: failed to compile {self.file1}")
                exit()

            if os.system(f"{self.output1}") != 0:
                print(f"EXECUTE ERROR: failed to run {self.output1}")   
                exit()
            return

        # builds all files and runs out.exe
        if self.file_selecter == "all":
            if os.system(f"gcc {self.file1} -o {self.output1}") != 0:
                print(f"COMPILE ERROR: failed to compile {self.file1}")
                exit()

            if os.system(f"{self.output1}") != 0:
                print(f"EXECUTE ERROR: failed to run {self.output1}")  
                exit()    
            return 
        print(f"COMPILE ERROR: failed to find '{self.file_selecter}'")
        exit()        


    def main(self):
        
        self.build()
        self.run()
        self.build_run()



if __name__ == "__main__":
    run = Main()
    run.main()