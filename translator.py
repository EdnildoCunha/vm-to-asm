from analyzer import Parser
from codeW import CodeWriter


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
                codeWriter.writeLabel(parser.getArg1())
                parser.advance()
            elif (_type == "Goto"):
                codeWriter.writeGoto(parser.getArg1())
                parser.advance()
            elif (_type == "If"):
                codeWriter.writeIf(parser.getArg1())
                parser.advance()

            elif (_type == "Call"):
                codeWriter.writeCall(parser.getArg1(), parser.getArg2())
                parser.advance()
            elif (_type == "Return"):
                codeWriter.writeReturn()
                parser.advance()
            elif (_type == "Function"):
                codeWriter.writeFunction(parser.getArg1(), parser.getArg2())
                parser.advance()
            else:
                print(self.parser.getCurrentCommand())
                print('write "{}" não implementado'.format(_type))
                self.parser.advance()


outputFile = "07\MemoryAccess\BasicTest\BASICTEST"
parser = Parser('07\MemoryAccess\BasicTest\BasicTest.vm')
codeWriter = CodeWriter(outputFile+".asm")
translate = Translate(parser, codeWriter)
translate.translate()
