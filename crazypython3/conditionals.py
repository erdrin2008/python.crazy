#kushtet dhe kontriolla e flow=it te programit
# == nese jane te barabarta dy variable
# != nese nuk jane te barabarta
# < me e vogel se
# > me a madhe se
# <= dhe >=
# operatoret logjike
#and or not
from crazypython1.main import temperatura

#shembulli 1:
age=int(input("your age?"))
if age>=15:
      print("you have gotten accepted in our school in the most advanced levels")
else:
      print("man you so young go enjoy life XD")

temperatura=28
if temperatura>30:
      print("it would be advised to stay at home it really hot outside so go out in your own risk")
elif 20<=temperatura<=30:
      print("the weather is so good why dont u go out for some fresh air")
else:
      print("it would be advised to stay at home because outside it super cold so why dont stay at home in your cozy bed")