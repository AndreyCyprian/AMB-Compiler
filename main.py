from KeyWords import Words, Numbers


arr = []
# User input method that will call readWords to tokenize
def UserInput():
    txt = input('Enter some grammar')
    gram = txt.split()  # I'll be splitting the based on spaces
    for x in gram:  # for each loop to go through each variable in the array
        readWords(x)
    print(arr)



def readWords(word):
    if word == Words.StartProgram:
        arr.append('Start Program')
    elif word == Words.EndProgram:
        arr.append('End Program')
    elif word == Words.StartSub:
        arr.append('Start Subs')
    elif word == Words.EndSub:
        arr.append('End Subs')
    elif word == Words.GoSub:
        arr.append('Go Sub')
    elif word == Words.Code:
        arr.append('Code')
    elif word == Words.If:
        arr.append('if')
    elif word == Words.Then:
        arr.append('then')
    elif word == Words.Else:
        arr.append('else')
    elif word == Words.EndIf:
        arr.append('end if')
    elif word == Words.While:
        arr.append('while')
    elif word == Words.Do:
        arr.append('do')
    elif word == Words.EndWhile:
        arr.append('EndWhile')
    elif word == Words.Int:
        arr.append('int')
    elif word == Words.String:
        arr.append('String')
    elif word == Words.Print:
        arr.append('print')
    elif word == Words.Input:
        arr.append('input')
    elif word == Words.softClose:
        arr.append('SoftClose')
    elif word == Words.softOpen:
        arr.append('SoftOpen')
    elif word == Words.hardOpen:
        arr.append('Hard open')
    elif word == Words.hardClose:
        arr.append('Hard Close')
    elif word == Words.quote:
        arr.append('Quote')
    elif word == Words.semi:
        arr.append('Semi Colon')
    elif word == Words.assignment:
        arr.append("assignment")
    elif word == Words.colon:
        arr.append('Colon')
    elif word == Words.multOpT:
        arr.append('Multi op *')
    elif word == Words.multOpD:
        arr.append('Multi op /')
    elif word == Words.addOpP:
        arr.append('Add')
    elif word == Words.addOpS:
        arr.append('Substract')
    elif word == Words.greaterThan:
        arr.append('greater than')
    elif word == Words.lessThan:
        arr.append('less than')
    elif word == Words.lessThanEqual:
        arr.append('less than equal')
    elif word == Words.greaterThanEqual:
        arr.append('greater than equal')
    elif word == Words.Equal:
        arr.append('equal')
    elif word == Words.notEqual:
        arr.append('not equal')
    elif word == Numbers.one:
        arr.append('one')
    elif word == Numbers.two:
        arr.append('two')
    elif word == Numbers.three:
        arr.append('three')
    elif word == Numbers.four:
        arr.append('four')
    elif word == Numbers.five:
        arr.append('five')
    elif word == Numbers.six:
        arr.append('six')
    elif word == Numbers.seven:
        arr.append('seven')
    elif word == Numbers.eight:
        arr.append('eight')
    elif word == Numbers.nine:
        arr.append('nine')
    elif word.isalpha():
        arr.append('Label')

if __name__ == '__main__':
    UserInput()
