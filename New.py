

current_number = 1
while current_number <= 5:
    print (current_number)
    current_number +=1



name = input ("Hallo, wie heisst Du?: ")
print ("\nHallo " + name + " Schoen, dass Du da bist!")
Alter = input ("\nund wie alt bist Du?: ")
Alter = int(Alter)
if Alter>=18:
    print ("\nGratuliere! Du darfst Dir diesen gruseligen Horrorfilm anschauen")
else:
    print ("\nLeider bist Du noch nicht alt genug fuer diesen Gruselfilm!")
