## NOTE TO SELF ADD HOMELESS FIGHTING SIMULATOR, MAKE +hp's AND +attk's PER WEAPON








##hi uh me upload git hub "huyjhggfgf" is git hub username thank bye
## LETS GO GAMBLING!!!
import time
import random
##InitialValues
difficulty = 1
machine1 = 5
machine2 = 0
machine3 = 0
machine4 = 0
machine5 = 0
##buying stuff
pointcost = 100
shopc = 0
addattrib = 0
##money
defmoney = 50
askmult = 1
attributepoints = 0
basemm = 100000
maxmoney = 100000
maxm = 1
totalaps = 0
moneymult = 1
moneymultinv = 1
##angel
angmult = 0
angmet = False
soul = 1
angcoins = 0
artifmulti = 1
ammax = 0
ammin = 0
##cheat
confirmedsafeguard = 0
cheatmoney = 1
thisstat = 0
cm = 0
## end
## Artifact list
addid = 0
## t1's
onoff = 0
tleafedclover = 0
fleafedclover = 0
## t2's
t2act = False
SturdyPiggyBank = 0
colladmpass = 0
##ANGEL
cross = 0
holyhand = 0
ContinuityErrors = 0
##RngA
t1artifacts = [1, 2, 3]
t2artifacts = [1]
## HERE ARE YOUR INITIAL CONTROLS!!!!

settings = int(input("Would you like to change some default stats? If you would like to change them, enter 1, if not enter 0. Enter: "))
if settings == 1:
    risk = int(input("Risk. Set to 1 if you want the default risk. Setting risk to higher than 1, or reaching it through other means disables safeguard. Enter: "))
    cooldown = int(input("What do you want time inbetween rolls to be? 1 = 1 second Enter: "))
    askevery = int(input("How often do you want to change the machines and amount you roll? 10 is reccommended. Enter: "))
    money = 50
else:
    if settings == 2:
        print("oh hey hackerman, the fog is coming the fog is coming the fog is coming the fog is coming")
        risk = int(input("risk"))
        cooldown = int(input("cooldown"))
        askevery = int(input("interval"))
        money = int(input("money"))
        defmoney = int(input("defaultmoney"))
        cheatmoney = int(input("moneymult"))
        confirmedsafeguard = int(input("safeguard (1=y 2=n)"))
        difficulty = 0
    elif settings == 3:
        print("preset1")
        risk = 1
        cooldown = 1
        askevery = 10
        money = 10000
        defmoney = money
        cheatmoney = 1
        confirmedsafeguard = 2
        difficulty = 0
    elif settings == 4:
        print("preset2")
        risk = 1
        cooldown = 1
        askevery = 10
        money = 10000000
        defmoney = 50
        cheatmoney = 1
        confirmedsafeguard = 2
        difficulty = 0
    else:
        money = 50
    risk = 1 ## risk 1 is the default, and the rnjesus cannot go lower. increases both sides of rnjesus. id recommend 1.5 at most.
    cooldown = 2
    askevery = 10
pcnt = int(input("wanna see the updates? 1=Y Enter: "))
if pcnt == 1:
    print("-------------------UPDATE-------------------")
    print("Angel Coins are spent to give an extra life if you have one left.")
    print("MAJOR REBALANCES!!!!")
    print("MAJOR BUG FIXES!!!!!!!")
    print("AAAAAANNNNDDDDD")
    print("AAADAEEEED THE COOOLLOOOOOO SEEEEE UUUUUUUUMMMM!M!MMHDHASGDHGWAYTDHABGuQWERTYUIOPASDFGHJKLZXCVBNM") 
    print("adn war")
##postsetup stats
asking = askevery

## USE F6 TO PAUUUSEEE!!!!! RAAAHHHH
##InfoStats
moneydiff = money
currentmoney = money
highscore = money*5
while True:
    if True:
        if asking >= askevery:
            if money >= highscore:
                print("You reached new heights in money, your previous highscore was", highscore, "now your highscore is", money)
                highscore = money
            else:
                print("No new heights obtained. Your", highscore-money, "away from your highscore of", highscore)
            while cm == 0:
                print("------------------MENU!!------------------")
                print("1 = Continue 2 = Change slots, 3 = Upgrades menu, 4 = Artifact inventory, 5 = Artifact info.", end=" ")
                if money >= 10000000 or angmet == True:
                    print("999 = Tribute", end=" ")
                menu = int(input("Enter: "))
                if menu == 1:
                    cm = 1
                    asking = 1
                elif menu == 2:
                    print("-----------SLOTS!!!-----------")
                    print("You have", money, "dollars!")
                    machine1 = int(input("How many of Money Machines do you want? Each costs 1$ Enter: "))
                    if machine1 < 0:
                        machine1 = 0
                        print("Cannot be below zero, Set to 0.")
                    machine1 = machine1
                    machine2 = int(input("How many of Artifact Machines do you want? Each costs 1000$ Enter: "))
                    if machine2 < 0:
                        machine2 = 0
                        print("Cannot be below zero, Set to 0.")
                    machine2 = machine2
                    machine3 = int(input("How many of Relic Machines do you want? Do be warned, the minimum rng is 4000. You may want to obtain more rng increasing artifacts before attempting. Each costs 50000$ Enter: "))
                    if machine3 < 0:
                        machine3 = 0
                        print("Cannot be below zero, Set to 0.")
                    machine3 = machine3
                    menu = 0
                elif menu == 3:
                    print("-----------UPGRADE!!!-----------")
                    print("You have", attributepoints, "Attribute points. Enter 1 to buy more. Currently costs", pointcost)
                    print("You have", moneymultinv, "multiplier, and", moneymult, "total multiplier. Enter 2 to change.")
                    print("You have", basemm, "base maximum money, and", maxm, "max money multiplier, totaling to", maxmoney, "Enter 3 to change.")
                    print("Enter 0 to go back.")
                    choice = int(input("Enter: "))
                    if choice == 0:
                        menu = 0
                    elif choice == 1:
                        print("-----------BUYING POINTS!-----------")
                        print("Buying", ContinuityErrors+1, "point(s)!")
                        addattrib = 1
                        if money >= pointcost*addattrib:
                            attributepoints = attributepoints + 1 + ContinuityErrors
                            
                            totalaps = totalaps + addattrib
                            money -= addattrib*pointcost
                            print("------------SUCCESS------------")
                            print("Bought", addattrib, "you now have", attributepoints, "attribute points and", money, "money.")
                            pointcost = (500*(totalaps**2))+500
                            print("Now costs", pointcost)
                        else:
                            print("-------------Error-------------")
                            print("NOT ENOUGH MONEY")
                        addattrib = 0
                    elif choice == 2:
                        print("----------UPGRADING..----------")
                        print("Upgrading Multiplier....")
                        print(attributepoints, "points to invest.")
                        addattrib = int(input("How many points would you like to invest? Enter: "))
                        if moneymultinv+addattrib > 1:
                            if addattrib <= attributepoints:
                                moneymultinv += addattrib
                                attributepoints -= addattrib
                                print("------------SUCCESS------------")
                                moneymult = (1*cheatmoney*moneymultinv*artifmulti*angmult)
                                print("Bought", addattrib, "multiplier, you now have", moneymultinv, "investment point multiplier, and", moneymult, "total multiplier")
                            else:
                                print("-------------Error-------------")
                                print("NOT ENOUGH POINTS")
                        else:
                            print("CANT GO NEGATIVE")
                    elif choice == 3:
                        print("----------UPGRADING..----------")
                        print("Upgrading Max Money....")
                        print(attributepoints, "points to invest.")
                        addattrib = int(input("How many points would you like to invest? Enter: "))
                        if maxm+addattrib > 1:
                            if addattrib <= attributepoints:
                                maxm += addattrib
                                attributepoints -= addattrib
                                print("------------SUCCESS------------")
                                maxmoney = basemm*maxm + 10000*SturdyPiggyBank
                                print("Bought", addattrib, "Max Money Mult, you now have", maxm, "max money multiplier, and", maxmoney, "total max")
                            else:
                                print("-------------Error-------------")
                                print("NOT ENOUGH POINTS")
                        else:
                            print("CANT GO NEGATIVE")
                elif menu == 4:
                    print("--------Inventory--------")
                    print(onoff, "On Off Switches", tleafedclover, "Three Leafed Clovers", fleafedclover, "Four Leafed Clovers",  end=' ')
                    if t2act == True:
                        print(SturdyPiggyBank, "Sturdy Piggy Banks", end=' ')
                    if angmet == True:
                        print(cross, "Crosses", holyhand, "Holy Hand Grenades")
                    else:
                        print(" ")
                    menu == int(input("Enter 5 check info or enter 1 to go back. Enter: "))
                elif menu == 5:
                    print("OnOff = 1, TLeafedClover = 2, FLeafedClover = 3", end=',')
                    if angmet == True:
                        print("Cross = 7771, Holy Hand Grenade = 7772")
                    print("Enter the id number of the item you wish to know more about, or enter 0 to go back.")
                    info = int(input("Enter: "))
                    if info == 0:
                        menu = 0
                    elif info == 1:
                        menu = 5
                        print("When the roll your on is odd, you gain 0.4 times money per, else you get 80 more min/max rng per.")
                    elif info == 2:
                        menu = 5
                        print("Gain 0.1 times money per clover.")
                    elif info == 3:
                        menu = 5
                        print("Gain 25 minimum and maximum rng per clover")
                    elif info == 4:
                        menu = 5
                        print("Gives you 10,000 max money")
                    elif info == 7771:
                        print("Gives 0.2 angel multiplier per cross")
                    elif info == 7772:
                        print("Gives 0.4 angel multiplier per grenade, but also has a 2 percent chance to divide your money by 1 + Holy Hand Grenades per grenade")
                    elif info == 7773:
                        print("Every time you purchase an upgrade point, you gain another one for free that doesnt increase price or cost anything")
                elif menu == 999:
                    if money >= 10000000:
                        print("Hello. You have reached a total of 10 Million dollars. This is a great amount, and the gods congratulate you.")
                        time.sleep(4)
                        print("Edgy message, sell physical body transfer to new one for reward. Currently no reward for growing past 10m.")
                        angmet = True
                        time.sleep(4)
                        print("Would you like to take this offer?")
                        time.sleep(1)
                        angelchoice = int(input("1=y 2=n. ENTER: "))
                        if angelchoice == 1:
                            print("Great, Please hold on as we extract your soul.")
                            ##artifs
                            onoff = 0
                            tleafedclover = 0
                            fleafedclover = 0
                            SturdyPiggyBank = 0
                            ##points
                            attributepoints = 0
                            moneymultinv = 0
                            totalaps = 0
                            money = defmoney
                            angcoins += 1
                            print("Simply enter in the number once again to spend your token")
                    elif angmet == True:
                        print("---------------AngelShop----------------")
                        print("You have", angcoins, "Angel Coins.")
                        print("The angel mult formula is 7**angelmult or 7 to the power of angelmult rounded to the hundredths")
                        print("You have", cross, "Cross. Option = 1, You gain 0.2 Angel Multiplier")
                        print("You have", holyhand, "Holy Hand Grenades. Option = 2, You gain 0.4 Angel Multiplier, but every round you have a 2 percent chance to divide your money by 1 + the amount of hand grenades you have.")
                        print("You have", ContinuityErrors, "Continuity Errors. Option = 3, Every time you purchase an upgrade point, you gain another one for free that doesnt increase price or cost anything")
                        shopc = int(input("0 to go back. Enter: "))
                        if shopc == 0:
                            menu = 0
                        elif shopc == 1:
                            if angcoins >= 1:
                                angcoins -= 1
                                cross += 1
                                print("Bought An Cross")
                        elif shopc == 2:
                            if angcoins >= 1:
                                angcoins -= 1
                                cross += 1
                                print("Bought A Holy Hand Grenade")
                        elif shopc == 3:
                            if angcoins >= 1:
                                angcoins -= 1
                                ContinuityErrors += 1
                                print("Bought An Continuity Error")
                    else:
                        print("Not for you, Uninteresting mortal.")
                elif menu == 666:
                    print("Sold your soul for 20 bucks. Enjoy your terrible luck.")
                    soul -= 1
                    money += 20
                    difficulty += 1
                elif menu == 777:
                    print("Easy mode enabled.                                                                                                                               wimp.")
                    angmult += 1
                    difficulty -= 2
                elif menu == 1234:
                    print("cheaterstats")
                    print(difficulty, "diff")
                    print(totalaps, "atps")
                    print(confirmedsafeguard, "sg")
                    print(defmoney, "defmoney")
                    print(cheatmoney, "cm")
                    print(soul, "sou")
                    print(angmult, "angel mult")
                    print(angmulti, "angel multi")
                    print(moneymult, "total mult")
                    print(settings, "set")
            ## END OF MENUS

            #MARK
            askmult = 1
        else:
            asking = asking + 1
            askmult += 1
        choice = 0
        cm = 0
        if confirmedsafeguard == 0:
            if risk > 1:
                safeguard = 0
            else:
                safeguard = 1
        else:
            safeguard = 1
        ##THIS IS THE GAMBLING!! Dont rig it or you die

        #MARK
        RNJESUS = random.randrange(10000-10000*soul + ammin + 900-900*risk + int(ammin*(risk-1)), 1000 -850+850*risk + ammax)
        natrng = random.randrange(0, 100)
        if machine1 >= 1:
            on1 = 1
        else:
            on1 = 0
        if machine2 >= 1:
            on2 = 1
        else:
            on2 = 0

        #SLOT1

        if machine1 >= 1 and money >= 1*machine1:
            money = money - 1*machine1
            print("-------------MoneyMachine-------------")
            print("Spent 1 dollar", machine1, "times")
            if RNJESUS >= 200 or safeguard == 0:
                if RNJESUS >= 2000:
                    money = money + machine1*moneymult + 0.0003*(RNJESUS*(machine1*moneymult))
                else:
                    money = money + machine1*moneymult + 0.0002*(RNJESUS*(machine1*moneymult))
        else:
            if on1 >= 1:
                print("You couldnt afford all of the Money Machines's so nothing happened.")
                asking = asking + 1

        ##SLOT2

        if machine2 >= 1 and money >= 1000*machine2:
            obtained = "Nothing rn"
            print("-------------ArtifactMachine-------------")
            print("Spent 1000 dollar", machine2, "times")
            money = money - 1000*machine2
            if RNJESUS >= 500 or safeguard == 0:
                cart = int(random.choice(t1artifacts))
                if cart == 1:
                    onoff += machine2
                    obtained = "On Off Switches"
                elif cart == 2:
                    tleafedclover += machine2
                    obtained = "Three Leafed Clovers"
                elif cart == 3:
                    fleafedclover += machine2
                    obtained = "Four Leafed Clovers"
                print("Got", machine2, "of", obtained)
        elif on2 >= 1:
            print("You couldnt afford all of the Artifact Machines's so nothing happened.")
            asking = asking + 1

        ##SLOT2

        if machine3 >= 1 and money >= 50000*machine3:
            obtained = "Nothing rn"
            print("-------------ArtifactMachine-------------")
            print("Spent 50000 dollar", machine3, "times")
            money = money - 50000*machine3
            if RNJESUS >= 4000 or safeguard == 0:
                t2act = True
                cart = int(random.choice(t2artifacts))
                if cart == 1:
                    SturdyPiggyBank += machine3
                    obtained = "Sturdy Piggy banks"
                elif cart == 2:
                    tleafedclover += machine2
                    obtained = "Three Leafed Clovers"
                elif cart == 3:
                    fleafedclover += machine2
                    obtained = "Four Leafed Clovers"
                print("Got", machine3, "of", obtained)
        elif on2 >= 1:
            print("You couldnt afford all of the Relic Machines's so nothing happened.")
            asking = asking + 1
        ##THIS IS THE STATS AFTER EVERYTHING

        #MARK
        basemm = 100000 
        maxmoney = basemm*maxm + 10000*SturdyPiggyBank
        if money > maxmoney:
            money = maxmoney

        pointcost = (500*(totalaps**2))+500
        if RNJESUS == 777:
            thisstat += 1
            print("You rolled high")
            if thisstat >= 10:
                print("Suddenly you obtained alot of clovers.")
                tleafedclover += 777
                fleafedclover += 777
        onoffc = asking % 2
        if onoffc == 1:
            onoffb = 1
        else:
            onoffb = 0
        ammax = (1-onoffb)*onoff*80 + 25*fleafedclover
        ammin = (1-onoffb)*onoff*80 + 25*fleafedclover
        artifmulti = 1 + 0.1*tleafedclover + 0.4*onoffb*onoff
        if money >= 100:
            money = int(money)
        else:
            money = round(money, 2)
        moneydiff = money-currentmoney
        if moneydiff >= 100:
            moneydiff = int(moneydiff)
        else:
            moneydiff = round(moneydiff, 2)
        if natrng == 66:
            print("Souls4Cash just enter in 666 in the menu!!!")
        if natrng == 77:
            print("Is this game too difficult for thyne? Commit to paradise by entering 777 in thyne menu!!")
        print("------------Total------------")
        print("Your RNG was", RNJESUS)
        print("Ran", asking, "times")
        if moneydiff >= 0:
            print("You gained", moneydiff, "dollars.")
        else:
            print("You lost", 0-moneydiff, "dollars.")
        print("You have", money)
        currentmoney = money
        if holyhand >= 1 and natrng <= 2:
            money = money/(holyhand+1)
            difficulty += holyhand/1000
            print("The Holy hand Grenade went off and took", )
        angmult = 0.2*cross + 0.4*holyhand
        angmulti = 1+7**angmult
        moneymult = 1*cheatmoney*moneymultinv*artifmulti*angmulti
        moneymult = int(round(moneymult, 2))
        time.sleep(cooldown)
        if money < 1:
            print("YOU LOSE!!! TIME TO SELF DESTRUCT!!! IN 5!")
            time.sleep(2)
            print("4!!")
            time.sleep(2.2)
            print("3!!!")
            time.sleep(2.4)
            print("2!!!!")
            time.sleep(2.6)
            print("1!!!!!!!!!")
            time.sleep(1)
            if angcoins >= 1:
                print("ERROR")
                time.sleep(1)
                print("ERROR")
                time.sleep(1)
                print("ANGEL COIN DETECTED, EXTRACTING...")
                time.sleep(3)
                print("RUN AWAY!!!! HAHAHAHAHAHA!!!! NO ANGEL COIN FOR YOU!!!")
                money = defmoney
                angcoins -= 1
            else:
                while True:
                    print("honk")
                    print("shuu")