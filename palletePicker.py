import os
import subprocess

class PalletePicker:

    def __init__(self) -> None:
        self.topColor = '44,43,44'
        self.bottomColor = ''
        self.seasons = ('winter', 'spring', 'summer', 'fall')

    def pickColorBottom(self) -> None:

        if(self.topColor == ''):
            print(f'A color has not been chosen yet, please choose a color :)')
        else:
            os.system("curl \'http://colormind.io/api/\' --data-binary \'{\"input\":"+f"[[{self.getTopColor}]]"+",\"model\":\"default\"}\'")
            

    @property
    def getBottomColor(self) -> str:
        return self.bottomColor
    
    @property
    def getTopColor(self) -> str:
        return self.topColor
    
    



##
test = PalletePicker()
print(test.getTopColor)
test.pickColorBottom()
##