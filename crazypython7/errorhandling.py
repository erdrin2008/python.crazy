#error handling try, expect finally
#try - writing of the needed code
#expect - what happens if an error happens in the try part
#finally - part of code that is always running
from crazypython5.functionexamples import resultati

#this is dedicated for error that programmers do not predict

#first example
#try:
#   print("pjesto me dy numra")
#  nr1=int(input("shkruani nr1:"))
# nr2=int(input("shkruani nr2:"))
#resultati=nr1/nr2
#print("rezulatati:",resultati)
#except ZeroDivisionError:
#      print("ke gabu per shkak qe je duke pjestuar me 0 ")

#second example
fruits={
    "apple":5,
    "banana":6,
    "orange":7
}
try:
    print(fruits["banana"])
except KeyError:
    print("the key does not exist in the dictionary")


text="this is not a number"
#third example
try:
    text_to_int=int(text)
except Exception as e:
    print("an error occurred at while parsing the data:", e)

#forth example
try:
    resultati=10/2
except ZeroDivisionError:
    print("division by error occurred")
else:
    print("division successful, result:",resultati)

#fifth example
try:
    resultati=10/0
except ZeroDivisionError:
    print("division by zero error occurred")
finally:
    print("this part of teh code always runs")


