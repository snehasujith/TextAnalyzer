string = ("Having more flexibility in customizing certain features would allow us to better tailor the application to our specific needs."
"Offering more templates or themes for further customization would be appreciated."

"It would be beneficial if there were more opportunities for users to provide feedback directly within the application."
"Being able to see how user feedback has been incorporated into updates would demonstrate responsiveness to customer needs.")

class TextAnalzer(object):
    
    def __init__ (self, text):
        
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmt = formattedText
    def freqAll(self):        
        
        wordList = self.fmt.split(' ')
        freqMap = {}
        for word in set(wordList): 
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
analyzed = TextAnalzer(string)
print("Formatted Text:", analyzed.fmt)
freqMap = analyzed.freqAll()
print(freqMap)
word = "be"
frequency = analyzed.freqOf(word)
print("be",word,"appears",frequency,"times.")
    