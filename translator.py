from analyzer import Parser
from codeW import CodeWriter
import sys
import os


class Translate:

    def __init__(self, parser, codeWriter):
        self.parser = parser
        self.codeWriter = codeWriter

    def translate(self):
        while self.parser.hasMoreCommands():
            _type = self.parser.commandType()

            if (_type == "Push"):
                self.codeWriter.writePush(
                    self.parser.getArg1(), self.parser.getArg2())
                self.parser.advance()
            elif (_type == "Pop"):
                self.codeWriter.writePop(
                    self.parser.getArg1(), self.parser.getArg2())
                self.parser.advance()
            elif (_type == "Arithmetic"):
                self.codeWriter.writeArithmetic(self.parser.getArg1())
                self.parser.advance()
            elif(_type == "Label"):
                self.codeWriter.writeLabel(self.parser.getArg1())
                self.parser.advance()
            elif (_type == "Goto"):
                self.codeWriter.writeGoto(self.parser.getArg1())
                self.parser.advance()
            elif (_type == "If"):
                self.codeWriter.writeIf(self.parser.getArg1())
                self.parser.advance()

            elif (_type == "Call"):
                self.codeWriter.writeCall(
                    self.parser.getArg1(), self.parser.getArg2())
                self.parser.advance()
            elif (_type == "Return"):
                self.codeWriter.writeReturn()
                self.parser.advance()
            elif (_type == "Function"):
                self.codeWriter.writeFunction(
                    self.parser.getArg1(), self.parser.getArg2())
                self.parser.advance()
            else:
                print(self.parser.getCurrentCommand())
                print('write "{}" não implementado'.format(_type))
                self.parser.advance()


'''
outputFile = "08\FunctionCalls\StaticsTest\StaticsTest"
parser = Parser('08\FunctionCalls\StaticsTest\Sys.vm')
codeWriter = CodeWriter(outputFile+".asm")
translate = Translate(parser, codeWriter)
translate.translate()
'''
inputFileOrDir = sys.argv[1]
vmFiles = []

print(inputFileOrDir)
if(os.path.isdir(inputFileOrDir)):
    split = inputFileOrDir.split("\\")
    outputFile = split[len(split)-1]

    _, _, filenames = next(os.walk(inputFileOrDir))

    for file in filenames:
        if(file.endswith(".vm")):
            vmFiles.append("{}\{}".format(inputFileOrDir, file))

    codeWriter = CodeWriter("{}\{}.asm".format(inputFileOrDir, outputFile))
    if(len(sys.argv) < 3):

        for vmFile in vmFiles:
            parser = Parser(vmFile)
            # code.moduleName = "foo"
            Translate(parser, codeWriter)

    else:
        if (sys.argv[2] == "-b"):
            codeWriter.writeInit()
            for vmFile in vmFiles:
                print(vmFile)
                split = vmFile.split("\\")
                outputFile = split[len(split) - 1]
                moduleName = outputFile.split(".")[0]

                codeWriter.moduleName = moduleName
                parser = Parser(vmFile)
                Translate(parser, codeWriter)

        else:
            print("error")

    codeWriter.close()


else:
    split = inputFileOrDir.split("\\")
    outputFileName = inputFileOrDir.split(".")[0]

    outputFile = split[len(split) - 1]
    moduleName = outputFile.split(".")[0]

    codeWriter = CodeWriter(outputFileName+".asm")
    codeWriter.moduleName = moduleName

    if (len(sys.argv) < 3):
        parser = Parser(inputFileOrDir)
        Translate(parser, codeWriter)
        codeWriter.close()

    else:
        if(sys.argv[2] == "-b"):
            codeWriter.writeInit()
            parser = Parser(inputFileOrDir)
            Translate(parser, codeWriter)
            codeWriter.close()
        else:
            print("error")
