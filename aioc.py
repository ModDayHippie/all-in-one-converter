import time
print('this project is a WIP')

print('this is a conversion program made by MDH')

ammount = input('what is the ammount to be converted:')
type = input('what type of unit is it? kg, lbs,grams,oz,feet,meters,farenhite,celcius')

if type == 'kg':
    kgtype = input('what would you like to convert to, lbs, grams or oz')
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

if type == 'lbs':
    ltype = input('what would you like to convert to, kgs, grams or oz')
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
if type == 'grams':
    gtype = input('what would you like to conver to lbs, kg, or oz')
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
if type == 'oz':
    oztype = input('what would you like to convert to? grams, kg, lbs')
    if oztype == 'grams':
        print('oi')

time.sleep(2)
input('press Enter to exit')