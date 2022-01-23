from asyncore import read

from flask import Flask, request
from flask_restful import Resource, Api

import subprocess


getterApp = Flask(__name__)
getterApi = Api(getterApp)

class PalletePicker:


    def __init__(self) -> None:

        self.topColor = ''
        self.bottomColorOptions = []
        self.bottomColor = ''
        self.accentColorOptions = []
        
        #maybe a new feature later?
        #self.seasons = ('winter', 'spring', 'summer', 'fall')


    def pickColorBottom(self) -> str:

        if(self.topColor == ''):
            print(f'A color has not been chosen yet, please choose a color :)')
        else:
            #writing the api output to the file
            file = open('ColorData.txt','w+')
            apiCmd = "curl \'http://colormind.io/api/\' --data-binary \'{\"input\":"+f"[[{self.getTopColor}]]"+",\"model\":\"default\"}\'"
            subprocess.run(apiCmd, shell=True, stdout=file)
            file.close()

            #reading the api output in for preprocessing
            file = open('ColorData.txt','r+')
            output = file.read()
            file.close()

            #preporcessing the output
            output = output[12:len(output)-4]
            self.bottomColorOptions = output.split('],[')

            return self.bottomColorOptions


    def pickColorTop(self) -> str:

            if(self.topColor == '' or self.bottomColor == ''):
                print(f'A color has not been chosen yet, please choose a color :)')
            else:
                file = open('ColorData.txt','w+')
                apiCmd = "curl \'http://colormind.io/api/\' --data-binary \'{\"input\":"+f"[[{self.getTopColor},{self.getBottomColor}]]"+",\"model\":\"default\"}\'"
                subprocess.run(apiCmd, shell=True, stdout=file)
                file.close()

            #reading the api output in for preprocessing
            file = open('ColorData.txt','r+')
            output = file.read()
            file.close()

            #preprocessing the output
            output = output[12:len(output)-4]
            self.accentColorOptions = output.split('],[')

            return self.accentColorOptions

    
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

test.setTopColor('13,54,189')
print(test.getTopColor)
test.setBottomColor('145,36,90')

test.pickColorBottom()
test.pickColorTop()
##