#######
# IPA.py
# @ Kobey Shwayder
# implementation of TIPA as double dict
# Feature values taken from Bruce Hayes "Introductory Phonology" 2001
# if they were in their, otherwise intuited by Kobey
#######

from Util import *
from Feature import Phoneme


def ParseTIPA(string):
    '''Given an input raw string (in TIPA) output a list of phonemes. 
        Backslashes should automatically be doubled by python.
        NB supersegmentals, clicks, and diacritics not implemented'''
    output = []
    string = list(string.encode("string-escape")) # make list and unescape characters
    while len(string) > 0:
        rawchar = string.pop(0)
    #for each character, if not brackets or \, return phoneme
        if rawchar == "\\":
        #if \\ get one of following 
        #1. A-z until bracket or space
        #2. not A-z (punctuation) plus following character
        #3. \c{c}
            tipachar = rawchar
            rawchar = string.pop(0)
            while rawchar == "\\":
                rawchar = string.pop(0) #delete multiple escapes
            if rawchar == 'c' and string[0:3] == '{c}':
                tipachar = tipachar + "c{c}"
                output.append(tipachar)
                tipachar = ''
                string = string[3:]
            elif rawchar in '!*:;': #punct
                tipachar = tipachar + rawchar + string.pop(0)
                output.append(tipachar)
                tipachar = ''
            elif re.match("[A-z]", rawchar):
                while rawchar not in "{} " and re.match("[A-z]", rawchar):
                    tipachar = tipachar + rawchar
                    if len(string) > 0:
                        rawchar = string.pop(0)
                    else:
                        break
                output.append(tipachar)
            else:
                raise LookupError("No TIPA character "+ tipachar + rawchar)
        elif re.match("[A-z0-9@]", rawchar):
            output.append(rawchar)
        #if brackets ignore
        else: #some other character, should be { or }
            #print rawchar
            pass
    return replaceDuplicates(output)


duplicates = {
"\textturna" : "5",
"\textscripta" : "A",
"\textturnscripta" : "6",
"\textturnv" : "2",
"\textscb" : "\;B",
"\textbeta" : "\B",
"\textctc" : "C",
"\textrtaild" : "\:d",
"\dh" : "D",
"\textschwa" : "@",
"\textreve" : "9",
"\textepsilon" : "E",
"\textrevepsilon" : "3",
"\textg" : "g",
"\texthtg" : "\!g",
"\textscg" : "\;G",
"\textbabygamma" : "7",
"\textramshorns" : "7",
"\texthth" : "H",
"\textturnh" : "4",
"\textsch " : "\;H",
"\textbari" : "1",
"\textsci" : "I",
"\textctj" : "J",
"\textltilde " : "\|~l",
"\textrtaill " : "\:l",
"\textscl " : "\;L",
"\textltailm" : "M",
"\textturnm" : "W",
"\~n" : "\textltailn",
"\textrtailn" : "\:n",
"\ng" : "N",
"\textscn" : "\;N",
"\textbaro" : "8",
"\textscoelig" : "\OE",
"\textopeno" : "O",
"\textphi" : "F",
"\textfishhookr" : "R",
"\textrtailr" : "\:r",
"\textturnr" : "\*r",
"\textscr" : "\;R",
"\textinvscr" : "K",
"\textrtails" : "\:s",
"\textesh" : "S",
"\textrtailt" : "\:t",
"\texttheta" : "T",
"\textbaru" : "0",
"\textupsilon" : "U",
"\textscu" : "U",
"\;U" : "U",
"\textscriptv" : "V",
"\textturnw" : "\*w",
"\textturny" : "L",
"\textscy" : "Y",
"\textrtailz" : "\:z",
"\textyogh" : "Z",
"\textglotstop" : "P",
"\textrevglotstop" : "Q",
'3' : '@', 
'\textrhookrevepsilon' : 'textrhookschwa'}

def replaceDuplicates(charlist):
    for i in range(len(charlist)):
        if charlist[i] in duplicates.keys():
            charlist[i] = duplicates[charlist[i]]
    return charlist
            

IPA = doubleDict()

IPA[r'_'] = '_' #for alignment
IPA[r'a'] = Phoneme(quick="+syll, +son, +cont, +voice, +dors, +low, -tense")
IPA[r'5'] = Phoneme(quick="+syll, +son, +cont, +voice, +dors, +low, +tense")
IPA[r'A'] = Phoneme(quick='+syll, +son, +dors, +back, +low, +cont, +voice')
IPA[r'6'] = Phoneme(quick='+syll, +son, +dors, +round, +lab, +back, +low, +cont, +voice')
IPA[r'\ae'] = Phoneme(quick='+syll, +son, +dors, +low, +front, +cont, +voice')
IPA[r'2'] = Phoneme(quick='+syll, +son, +dors, +back, +cont, +voice')
IPA[r'b'] = Phoneme(quick='+cons, +lab, +voice')
IPA[r'\;B'] = Phoneme(quick='+trill, +son, +voice, +lab, +cont')
IPA[r'B'] = Phoneme(quick='+cons, +lab, +cont, +voice')
IPA[r'c'] = Phoneme(quick='+cons, +dors, +dist, +high')
IPA[r'\c{c}'] = Phoneme(quick='+cons, +dors, +dist, +high, +cont')
IPA[r'C'] = Phoneme(quick='+cons, +dors, +dist, +high, +front, +cont')
IPA[r'd'] = Phoneme(quick='+cons, +cor, +ant, +voice')
IPA[r'\:d'] = Phoneme(quick='+cons, +cor, +voice')
IPA[r'\textdzlig'] = Phoneme(quick='+cons, +cor, +ant, +strid, +voice, +del_rel')
IPA[r'\textdyoghlig'] = Phoneme(quick='+cons, +cor, +dist, +strid, +voice, +del_rel')
IPA[r'D'] = Phoneme(quick='+cons, +cor, +ant, +cont, +voice')
IPA[r'e'] = Phoneme(quick='+syll, +son, +dors, +tense, +cont, +voice, +front')
IPA[r'@'] = Phoneme(quick='+syll, +son, +dors, +cont, +voice')
IPA[r'\textrhookschwa'] = Phoneme(quick='+syll, +son, +dors, +cont, +voice, +rhotic')
IPA[r'9'] = Phoneme(quick = '+syll, +son, +dors, +tense, +cont, +voice')
IPA[r'E'] = Phoneme(quick = '+syll, +son, +dors, +cont, +voice, +front')
#IPA[r'3'] = Phoneme(quick = '+son, +dors, +cont, +voice') #=schwa?
#IPA[r'\textrhookrevepsilon'] = Phoneme(quick = '+son, +dors, +cont, +voice, +rhotic') = rschwa
IPA[r'\textcloserevepsilon'] = Phoneme(quick = '+syll, +son, +dors, +lab, +round, +cont, +voice')
IPA[r'f'] = Phoneme(quick = '+cons, +labiodent, +cont, +strid')
IPA[r'g'] = Phoneme(quick = '+cons, +dors, +high, +back, +voice')
IPA[r'\;G'] = Phoneme(quick = '+cons, +dors, +back, +voice')
IPA[r'G'] = Phoneme(quick = '+cons, +dors, +high, +back, +voice, +cont')
IPA[r'7'] = Phoneme(quick = '+son, +dors, +back, +tense, +cont, +voice')
IPA[r'h'] = Phoneme(quick = '+son, +lar, +cont, +spread_gl')
IPA[r'\textcrh'] = Phoneme(quick = '+son, +TR, +cont')
IPA[r'H'] = Phoneme(quick = '+son, +lar, +cont, +voice, +spread_gl')
IPA[r'4'] = Phoneme(quick = '+son, +lab, +dors, +round, +high, +cont, +voice')
IPA[r'i'] = Phoneme(quick = '+syll, +son, +dors, +high, +tense, +cont, +voice, +front')
IPA[r'1'] = Phoneme(quick = '+syll, +son, +dors, +high, +tense, +cont, +voice')
IPA[r'I'] = Phoneme(quick = '+syll, +son, +dors, +high, +front, +cont, +voice')
IPA[r'j'] = Phoneme(quick = '+son, +dors, +high, +dist, +cont, +voice')
IPA[r'J'] = Phoneme(quick = '+cons, +dors, +high, +dist, +cont, +voice')
IPA[r'\textbardotlessj'] = Phoneme(quick='+cons, +dors, +dist, +high, +voice')
IPA[r'k'] = Phoneme(quick = '+cons, +dors, +high, +back')
IPA[r'l'] = Phoneme(quick = '+cons, +son, +cor, +ant, +cont, +voice, +lat')
IPA[r'\|~l'] = Phoneme(quick = '+cons, +cor, +dors, +ant, +high, +back, +cont, +lat, +voice')
IPA[r'\textbeltl'] = Phoneme(quick = '+cons, +cor, +ant, +cont, +lat, +strid')
IPA[r'\:l'] = Phoneme(quick = '+cons, +son, +cor, +cont, +lat, +voice')
IPA[r'\textlyoghlig'] = Phoneme(quick = '+cons, +cor, +ant, +cont, +lat, +strid, +voice')
IPA[r'\;L'] = Phoneme(quick = '+cons, +son, +dors, +high, +back, +cont, +voice, +lat')
IPA[r'm'] = Phoneme(quick = '+cons, +son, +lab, +nas, +voice')
IPA[r'M'] = Phoneme(quick = '+cons, +son, +labiodent, +nas, +voice')
IPA[r'W'] = Phoneme(quick = '+son, +dors, +high, +tense, +back, +cont, +voice')
IPA[r'\textturnmrleg'] = Phoneme(quick = '+son, +dors, +high, +back, +cont, +voice')
IPA[r'n'] = Phoneme(quick = '+cons, +son, +cor, +ant, +nas, +voice')
IPA[r'\:n'] = Phoneme(quick = '+cons, +son, +cor, +nas, +voice')
IPA[r'\textltailn'] = Phoneme(quick = '+cons, +son, +dors, +high, +nas, +voice')
IPA[r'N'] = Phoneme(quick = '+cons, +son, +dors, +high, +back, +nas, +voice')
IPA[r'\;N'] = Phoneme(quick = '+cons, +son, +dors, +back, +nas, +voice')
IPA[r'o'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +back, +tense, +cont, +voice')
IPA[r'8'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +tense, +cont, +voice')
IPA[r'\o'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +front, +tense, +cont, +voice')
IPA[r'\oe'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +front, +cont, +voice')
IPA[r'\OE'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +low, +front, +cont, +voice')
IPA[r'O'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +back, +cont, +voice')
IPA[r'p'] = Phoneme(quick = '+cons, +lab')
IPA[r'F'] = Phoneme(quick = '+cons, +lab, +cont')
IPA[r'q'] = Phoneme(quick = '+cons, +dors, +back')
IPA[r'r'] = Phoneme(quick = '+cons, +son, +cor, +ant, +cont, +voice, +trill')
IPA[r'R'] = Phoneme(quick = '+cons, +son, +cor, +ant, +voice, +tap')
IPA[r'\:r'] = Phoneme(quick = '+cons, +son, +cor, +voice, +tap')
IPA[r'\*r'] = Phoneme(quick = '+cons, +son, +cor, +ant, +cont, +voice')
IPA[r'\:R'] = Phoneme(quick = '+cons, +son, +cor, +cont, +voice')
IPA[r'\;R'] = Phoneme(quick = '+cons, +son, +dors, +back, +cont, +voice, +trill')
IPA[r'K'] = Phoneme(quick = '+cons, -son, +strid, +dors, +back, +cont, +voice') 
IPA[r'\textturnlonglegr'] = Phoneme(quick = '+cons, +son, +cor, +ant, +cont, +voice, +lat, +tap')
IPA[r's'] = Phoneme(quick = '+cons, +cor, +ant, +cont, +strid')
IPA[r'\:s'] = Phoneme(quick = '+cons, +cor, +cont, +strid')
IPA[r'S'] = Phoneme(quick = '+cons, +cor, +dist, +cont, +strid')
IPA[r't'] = Phoneme(quick = '+cons, +cor, +ant')
IPA[r'\:t'] = Phoneme(quick = '+cons, +cor')
IPA[r'\texttslig'] = Phoneme(quick='+cons, +cor, +ant, +strid, +del_rel')
IPA[r'\textteshlig'] = Phoneme(quick='+cons, +cor, +dist, +strid, +del_rel')
IPA[r'T'] = Phoneme(quick='+cons, +cor, +ant, +cont')
IPA[r'u'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +high, +back, +tense, +cont, +voice')
IPA[r'0'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +high, +tense, +cont, +voice')
IPA[r'U'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +high, +back, +cont, +voice')
IPA[r'v'] = Phoneme(quick = '+cons, +labiodent, +cont, +strid, +voice')
IPA[r'V'] = Phoneme(quick = '+cons, +son, +labiodent, +cont, +voice')
IPA[r'w'] = Phoneme(quick = '+son, +lab, +dors, +round, +high, +back, +cont, +voice')
IPA[r'\*w'] = Phoneme(quick = '+son, +lab, +dors, +round, +high, +back, +cont')
IPA[r'x'] = Phoneme(quick = '+cons, +dors, +back, +high, +cont')
IPA[r'X'] = Phoneme(quick = '+cons, +dors, +back, +cont, +strid')
IPA[r'y'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +high, +front, +tense, +cont, +voice')
IPA[r'L'] = Phoneme(quick = '+cons, +son, +dors, +high, +dist, +cont, +lat')
IPA[r'Y'] = Phoneme(quick = '+syll, +son, +lab, +dors, +round, +high, +front, +cont, +voice')
IPA[r'z'] = Phoneme(quick = '+cons, +cor, +ant, +cont, +strid, +voice')
IPA[r'\:z'] = Phoneme(quick = '+cons, +cor, +cont, +strid, +voice')
IPA[r'Z'] = Phoneme(quick = '+cons, +cor, +dist, +cont, +strid, +voice')
IPA[r'\textctz'] = Phoneme(quick='+cons, +dors, +dist, +high, +front, +cont, +voice')
IPA[r'P'] = Phoneme(quick='+son, +lar, +constr_gl')
IPA[r'Q'] = Phoneme(quick ='+son, +TR, +cont, +voice')

                    

def PhonParse(string):
    '''Input a string (in TIPA), returns a list of Phonemes'''
    characterlist = ParseTIPA(string)
    return [IPA[c] for c in characterlist]

def IPAword(IPAlist):
    '''Takes a list of phonemes and prints each phoneme symbol'''
    return [IPA[c] for c in IPAlist]


def subset(featurelist, toprint = True):
    '''takes string of "+feat, -feat" and returns TIPA representation of
    all phonemes in IPA that match those features '''
    if type(featurelist) == str:
        features = featurelist.split(", ")
        featurelist = {}
        for feat in features:
            arg = feat[1:]
            if feat[0] == '+':
                featurelist[arg] = Feature.Plus
            elif feat[0] == '-':
                featurelist[arg] = Feature.Minus
            elif feat[0] == '0':
                featurelist[arg] = Feature.NotSpecified
            elif feat[0] == '?':
                featurelist[arg] = Feature.Needs
            elif feat[0] == 'm':
                featurelist[arg] = Feature.Marked
            elif feat[0] == 'u':
                featurelist[arg] = Feature.Unmarked
            elif feat[0] == '@':
                featurelist[arg] = Feature.Any
            else:
                raise ValueError("No such feature value: " + feat[0]) 
    set = IPA.copy()
    del set['_']
    for key in featurelist.keys():
        for elem in set.keys():
            if set[elem][key] != featurelist[key]:
                del set[elem]
    if toprint:
        return set.keys()
    else:
        return set


if __name__ == "__main__":
    #print subset('+lab, -syll')
    print PhonParse(r'\ae')
    print subset("+high, +round")