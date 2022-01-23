from asyncore import read
import os
import subprocess
import re

class PalletePicker:


    def __init__(self) -> None:
        self.topColor = '43,89,104'
        self.bottomColorOptions = [];
        self.bottomColor = ''
        self.seasons = ('winter', 'spring', 'summer', 'fall')


    def pickColorBottom(self) -> str:

        if(self.topColor == ''):
            print(f'A color has not been chosen yet, please choose a color :)')
        else:
            file = open('ColorData.txt','w+')
            apiCmd = "curl \'http://colormind.io/api/\' --data-binary \'{\"input\":"+f"[[{self.getTopColor}]]"+",\"model\":\"default\"}\'"
            subprocess.run(apiCmd, shell=True, stdout=file)
            file.close()

            file = open('ColorData.txt','r+')
            output = file.read()
            output = output[11:len(output)-3]
            file.close()


    def pickColorTop(self) -> str:

            if(self.topColor == ''):
                print(f'A color has not been chosen yet, please choose a color :)')
            else:
                file = open('ColorData.txt','w+')
                apiCmd = "curl \'http://colormind.io/api/\' --data-binary \'{\"input\":"+f"[[{self.getTopColor}]]"+",\"model\":\"default\"}\'"
                subprocess.run(apiCmd, shell=True, stdout=file)
                file.close()

                file = open('ColorData.txt','r+')
                output = file.read()
                output = output[11:len(output)-3]
                file.close()


                print(output)

                self.bottomColorOptions = re.findall('\[d*,d*,d*],[d*,d*,d*],[d*,d*,d*],[d*,d*,d*],[d*,d*,d*]', output)
                print(self.bottomColorOptions)

                return output
           

    @property
    def getBottomColor(self) -> str:
        return self.bottomColor
        
    @property
    def getTopColor(self) -> str:
        return self.topColor

    def setTopColor(self, color) -> None:
        self.topColor = color

    def setBottomColor(self, color) -> None:
        self.bottomColor = color
    

##
test = PalletePicker()
print(test.getTopColor)
test.pickColorBottom()
##