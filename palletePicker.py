
class PalletePicker:

    def __init__(self) -> None:
        self.palleteDictionary = {}
        self.startingColor = ''
        self.seasons = ('winter', 'spring', 'summer', 'fall')

    def pickColorPants(self, color):
        
        if(self.startingColor == ''):
            return f'A color has not been chosen yet, please choose a color'
        else:
            for i in self.palleteDictionary:
                if 
