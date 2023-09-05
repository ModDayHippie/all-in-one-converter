#this is a test line
import time
print('''░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌ Doge is watching
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█''')

print('this project is a WIP that showcases math,loops,input and other basic functions of python')

print('this is a conversion program made by MDH')
print('v1.1')
print('------------------------------------------------------------------------------------------')

ammount = input('what is the ammount to be converted:')
type = input('what type of unit is it? kg, lbs,grams,oz,feet,meters,farenhite,celcius,tip,centimeteres:')


#these lines are to convert kg
if type == 'kg':
    kgtype = input('what would you like to convert to, lbs, grams or oz:')
    if kgtype == 'lbs':
        kglbstype = int(ammount) * 2.204
        print('the weight in lbs is')
        print(kglbstype)
    if kgtype == 'grams':
        kggtype = int(ammount) * 1000
        print('the weight in grams is')
        print(kggtype)
    if kgtype == 'oz':
        kgoztype = int(ammount) * 35.174
        print('the wight in ounces is')
        print(kgoztype)


#these lines are for converting lbs
if type == 'lbs':
    ltype = input('what would you like to convert to, kgs, grams or oz:')
    if ltype == 'kgs':
        lbskgtype = int(ammount) / 2.205
        print('the weight in kg is')
        print(lbskgtype)
    if ltype == 'grams':
        lbsgtype = int(ammount) * 453.592
        print('the wight in grams is')
        print(lbsgtype)
    if ltype == 'oz':
        lbsoztype = int(ammount) * 16
        print('the weight in oz is')
        print(lbsoztype)


#these lines convert grams
if type == 'grams':
    gtype = input('what would you like to conver to lbs, kg, or oz:')
    if gtype == 'lbs':
        glbstype = int(ammount) / 454
        print('so the weight in lbs is')
        print(glbstype)
    if gtype == 'kg':
        gkgtype = int(ammount) / 1000
        print('so the weight in kg is')
        print(gkgtype)
    if gtype == 'oz':
        ozkgtype = int(ammount) / 28.35
        print('so the weight in oz is')
        print(ozkgtype)


#these lines convert oz
if type == 'oz':
    oztype = input('what would you like to convert to? grams, kg, lbs:')
    if oztype == 'grams':
        oztograms = int(ammount) * 28.3
        print('so the wight in grams is')
        print(oztograms)
    if oztype == 'kg':
        oztokg = int(ammount) / 35.274
        print('so the weight in kg is')
        print(oztokg)
    if oztype == 'lbs':
        oztolbs = int(ammount) / 16
        print('so the weight in lbs is')
        print(oztolbs)


#these lines convert feet
if type == 'feet':
    feettype = input('what would you like to convert to, km, miles, or meters, inches:')
    if feettype == 'km':
        feettokm = int(ammount) / 3281
        print('so the length in km is')
        print(feettokm)
    if feettype == 'miles':
        feettomiles = int(ammount) / 5280
        print('so the length in miles is')
        print(feettomiles)
    if feettype == 'meters':
        feettometers = int(ammount) / 3.281
        print('so the length in meters is')
        print(feettometers)
    if feettype =='inches':
        feettoinch = int(ammount) * 12
        print('so the length in inches is')
        print(feettoinch)


#these lines convert meters
if type == 'meters':
    metertype = input('what would you like to convert to, feet, inches, km, miles:')
    if metertype == 'feet':
        metertofeet = int(ammount) * 3.281
        print('so the lenght in feet is')
        print(metertofeet)
    if metertype == 'inches':
        metertoinch = int(ammount) * 39.3701
        print('so the length in inches is')
        print(metertoinch)
    if metertype == 'km':
        metertokm = int(ammount) / 1000
        print('the length in km is')
        print(metertokm)
    if metertype == 'miles':
        metertomile = int(ammount) / 1609
        print('so the length in miles is')
        print(metertomile)

#these lines are for a tip calc
if type == 'tip':
      tipammount = input('What % would you like to tip?5,10,15 or 20:')
      if tipammount == '5': 
          fivetip = int(ammount)  * 1.05 - int(ammount)
          print('so the ammount to tip would be')
          print(fivetip)
      if tipammount == '10':
          tentip = int(ammount)  * 1.10 - int(ammount)
          print('so the ammount to tip would be')
          print(tentip)
      if tipammount == '15':
          fivtip = int(ammount)  * 1.15 - int(ammount)
          print('so the ammount to tip would be')
          print(fivtip)
#these lines convert centimeters
if type == 'centimeters':
     centitype = input('what would you like to convert to:')
     if centitype == 'inches':
         centitoinches = int(ammount)  / 2.54
         print('so the length in inches is:')
         print(centitoinches)
     if centitype == 'feet':
         centitofeet = int(ammount) / 30.48
         print('so the lenght in  feet is')
         print(centitofeet)
     if centitype == 'meters':
        centitometers = int(ammount) / 100
        print('so the length in meteres is:')
        print(centitometers)
    # if centitype == '

input('press ENTER to quit')
