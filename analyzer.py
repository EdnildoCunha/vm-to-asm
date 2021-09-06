class Parser():
    def __init__(self, inputFileName):
        self.inputFileName = inputFileName
        self.file = open(inputFileName, "r")
        self.temp = self.file.readlines()
        self.commands = []
        self.currentCommandIndex = 0
        self.formatLines()


    def hasMoreCommands(self):
        return self.currentCommandIndex <= len(self.commands)-1

    def advance(self):
        if (self.hasMoreCommands()):
            self.currentCommandIndex += 1

    def commandType(self):
        command = self.getCurrentCommand()
        split = command.split(" ")
        foo = split[0]
        if (command in ['add','sub','neg','eq','gt','lt','and','or','not']):
            return "Arithmetic"
        else:
            if   (foo == "pop")       : return "Pop"
            elif (foo == "push")      : return "Push"
            elif (foo == "call")      : return "Call"
            elif (foo == "function")  : return "Function"
            elif (foo == "return")    : return "Return"
            elif (foo == "label")     : return "Label"
            elif (foo == "goto")      : return "Goto"
            elif (foo == "if-goto")   : return "If"

            else : return None

    def getArg1(self):
        if(self.commandType() == "Arithmetic"):
            return self.getCurrentCommand()
        elif(self.commandType() == "Return"):
            return None
        else:
            return self.getCurrentCommand().split(" ")[1]

    def getArg2(self):
        if(self.commandType() in ["Push", "Pop", "Function", "Call"]):
            return self.getCurrentCommand().split(" ")[2]
        else:
            return None

    def formatLines(self):
        for line in self.temp:
            self.commands.append(line.replace("\n", ""))
    
        
    def getCurrentCommand(self):
        return self.commands[self.currentCommandIndex]