import os, shutil
def blankScr():
    os.system('cls' if os.name == 'nt' else 'clear')

blankScr()
print("Welcome to Convenient File Relocator Tool Software Program Application (CFRTSPA for short)")
print("Take your source directory, and your destination directory, and input both.")
print("the source directory should only have files, and the destination directory should only have subdirectories. Do not end either directory in a backslash (this will be remedied later)")
print("")
input("Press Enter to start.")
blankScr()
print("(Directories can be absolute, or relative to this script)")
srcDir  = str(input("Please enter absolute source directory: "))
dstDir  = str(input("Please enter absolute destination directory: "))
srcOS   = os.listdir(srcDir)
dstOS   = os.listdir(dstDir)
srcFile = srcDir + "\\"
srcDst = dstDir + "\\"

for i in range(len(srcOS)):
    blankScr()
    print("[",i+1,"of",len(srcOS),"]") #progress bar... sorta
    print("Filename:",srcOS[i]) #shows name of file
    tmpSrcFile = srcFile + srcOS[i] #this should, in theory, result in X:\directory\filename.ext AND DOES! AWESOMESAUCE :D
    reply = input("Type the index of the folder you want, or \"help\" for more info: ")
    if reply == "help": #if the user types help, tell them how index number thing works and list all folders.
        print("Type the index number for the following folders. For instance,", dstOS[0], "would be 0,", dstOS[1], "would be 1, and so on.")
        print("Your Folders:")
        print(dstOS)
        reply = input("Type the index of the folder you want: ")
    tmpDstFile = srcDst + dstOS[int(reply)] #sets temporary working directory to the folder you set via index #
    #print("DEBUG!!!!!!!!!!!!!!srcOS[i] and tmpDstFile", srcOS[i], tmpDstFile)
    if srcOS[i] in os.listdir(tmpDstFile):
        print("Warning: This file already exists in that directory! What do you want to do?")
        print("Enter 1 to overwrite, or anything other number to skip.")
        #print("[3] Rename to", srcOS[i],"(2)")
        choice = int(input(": "))
        if choice == 1:
            shutil.copy2(tmpSrcFile, tmpDstFile)
            os.remove(tmpSrcFile)
    else:
        shutil.copy2(tmpSrcFile, tmpDstFile)
        os.remove(tmpSrcFile)

    
print("Job completed!")

    #ask here which folder to move to, using dstDir as reference
    #tmpSrcDst = srcDest + [whichever folder the user chose]




