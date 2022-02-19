import ctypes
import sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    ctypes.windll.kernel32.SetConsoleTitleW("Gamble Game")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░█████░░░██░░░██░░░██░░░████░░█░░░███░░")
    print("░░█░░░░░░███░░░██░░███░░░█░░██░█░░░█░░░░")
    print("░██░░░░░░█░█░░░██░░█░█░░░█░░██░█░░░█░░░░")
    print("░█░░███░█░░██░░██░░█░█░░░████░░█░░░███░░")
    print("░█░░░░█░█████░░███░█░█░░██░░█░░█░░░█░░░░")
    print("░██░░██░█░░░██░█░███░██░█░░░█░░█░░░█░░░░")
    print("░░████░██░░░░█░█░░██░░█░█████░░███░███░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░█░░░███░░██░░░░░██░░░░░██░░██████░░")
    print("░░░░█░░░░░░█░░█░██░░░███░░████░░██░░░░░░")
    print("░░░░█░░░░░██░██████░░█░██░█░░█░░░█████░░")
    print("░░░░███████░░█░░░░██░█░░██░░██░░░█░░░░░░")
    print("░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█████░░░")
    print("░░░░░░░░░░░░░░░░Version: 7.0░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░By MerlinMDV░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░PC Edition░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("Welcome to the Gamble Game. TYPE 'exit' TO SAVE AND EXIT. TYPE 'save' TO SAVE GAME. TYPE 'reset' TO RESET ALL PROGRESS. Type 'help' for instructions, type 'changelog' for changelog.")
    EZ = "no"
    bebe = "no"
    megamlz = "no"
    devmode = "no"
    choice = "null"
    rob = "null"
    pay = "null"
    num = "null"
    robby = "null"
    airbreak = "null"
    shopchoice = "null"
    import time
    import random
    import configparser
    White = ""
    exit = "false"
    config = configparser.ConfigParser()
    config.read("GAMBLEDATA.ini")
    strcoins = config.get("GAMBLEDATA", "coins")
    strPEPE = config.get("GAMBLEDATA", "PEPE")
    strgold = config.get("GAMBLEDATA", "gold")
    HAM = config.get("GAMBLEDATA", "HAM")
    air = config.get("GAMBLEDATA", "air")
    gamblehandicap = config.get("GAMBLEDATA", "gamblehandicap")
    gun = config.get("GAMBLEDATA", "gun")
    monopoly = config.get("GAMBLEDATA", "monopoly")
    changelog = config.get("changelog", "text")
    coins = int(strcoins)
    PEPE = int(strPEPE)
    gold = int(strgold)
    def return_all():
      return time
      return sys
      return random
      return configparser
      return ctypes
    while exit != "true":
      print("Gamble, check your inventory, rob, enter the shop, enter the lottery, or work?")
      choice = str(input("(Say inventory, lottery, gamble, rob, shop, or work.) "))
      if choice == "gamble":
        if coins > 200:
          coins -= 1
          print("You were charged 1 coin to gamble, because you are a rich dude and they want your money.")
        if coins > 500:
          coins -= 4
          print("You were also charged 4 more coins to gamble, because you are filthy rich and they want some of that.")
        if gamblehandicap == "yes":
          num = random.randint(1,6)
          if num == 1 or num == 2:
            coins += 5000000
            print("Altering quantum state...")
            time.sleep(2)
            print("Successfully Altered.")
            time.sleep(1)
            print(White+"woah whats happening")
            print("The machine starts smoking and you win the mega jackpot. You gained 5000000 coins.")
          if num == 3 or num == 4 or num == 5:
            coins += 20000000
            print("Altering quantum state...")
            time.sleep(2)
            print("Successfully Altered.")
            time.sleep(1)
            print(White+"wtf")
            print("The machine starts smoking and you win a jackpot that doesn't even seem possible. You gained 20000000 coins.")
          if num == 6:
            coins += 100000000
            print("Altering quantum state...")
            time.sleep(2)
            print("Successfully Altered.")
            time.sleep(1)
            print(White+"...")
            print("The machine explodes. You got 100000000 coins.")
        else:
          num = random.randint(1,11)
          if num == 1 or num == 2 or num == 3 or num == 4:
            coins += 10
            print("winner winner")
            print("You have gained 10 coins!")
          elif num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
            coins -= 9
            print("sucks to suck")
            print("You lost 9 coins")
          elif num == 10:
            print("You suck, gamble.exe stopped working, and you got literally nothing.")
          elif num == 11:
            import random 
            payout = random.randint(1,5)
            if payout == 1 or payout == 3 or payout == 4 or   payout == 5:
              coins += 1
              print("hm")
              print("You got 1 coin. Go figure.")
            elif payout == 2:
              coins += 50
              print("wow such coin")
              print("JACKPOT! HUGE PAYOUT! You got 50 coins, niceee.")
      if choice == "inventory":
        print(" ")
        print("INVENTORY:")
        print(" ")
        print("You have" , coins , "coins.")
        if PEPE > 0:
          print("Your Fake Pepe(s) " + White + "has(ve) ", PEPE ," uses left.")
        if HAM == "yes":
          print("You have the Donkey Kong Hammer Upgarde " + White + "equipped.")
        if air == "yes":
          print("You have the AirPods Pro " + White + "Equipped.")
        if gold > 0:
          print("You're Golden Hammer(s) has(ve) ",gold," uses left.")
      if choice == "work":
        if monopoly == "yes":
          amt = random.randint(10000000,55000000)
          print("Your company has gained ", amt," coins.")
        if gun == "yes":
          togain = (random.randint(1000000,7500000))
          coins += togain
          print("You whip out your assault rifle and hold everyone hostage until they give you money.")
          print("you gained ",togain," coins.")
        else:
          if air == "yes":
            print("+ 5 Coins!" + White)
            import random
            airbreak = random.randint(1,15)
            if airbreak == 1 or airbreak == 2 or airbreak == 3 or airbreak == 4 or airbreak == 5 or airbreak == 6 or airbreak == 7 or airbreak == 8 or airbreak == 9 or airbreak == 10 or airbreak == 11 or airbreak == 12 or airbreak == 13 or airbreak == 15:
              print("You show up to work with your AirPods Pro." + White)
            elif airbreak == 14:
              air = "no"
              print("You try to put on your Airpods, but they fall out of your ear and break.")
          if coins > 200:
            coins -= 1
            print("Your boss knocked off 1 coin from your earnings because you are richer than him.")
          if coins > 500:
            coins -= 4
            print("Your boss also knocked off 4 more coins from your earnings because you are filthy rich and he hates you.")
          import random
          pay = random.randint(1,10)
          if pay == 1 or pay == 2 or pay == 3 or pay == 4:
            coins += 8
            print("lol nice")
            print("You were paid a lucky 8 coins!")
          elif pay == 5 or pay == 6 or pay == 7 or pay == 8 or pay == 9:
            coins += 5
            print("ok")
            print("You earned your ordinary 5 coins.")
          elif pay == 10:
            print("You suck, boss.exe stopped working, and you got literally nothing.")
      if choice == "rob":
        if HAM == "yes":
          coins += 10
          print("+ 10 Coins!" + White)
        gold -= 1
        import random
        rob = random.randint(1,11)
        if rob == 1 or rob == 2 or rob == 3 or rob == 4 or rob == 5 or rob == 6 or rob == 7:
          coins -= 20
          print("lol")
          print("You take out your mini Donkey Kong Hammer and attempt to break the gamble machine open, but the police found you and charged you 20 coins.")
          if gold > 0:
            print("However, your sweet Golden Donkey Kong Hammer managed to purge the machine of 50 Coins before the police found you. Your Golden Hammer(s) has(ve) ", gold, " uses left.")
        elif rob == 8 or rob == 9:
          coins += 25
          print("nice")
          print("You take out your mini Donkey Kong Hammer and crack the gamble machine open. It cracks only a little and you take the 25 coins that spill out. NOW PUT AWAY THAT HAMMER BEFORE THE POLICE SEES YOU!")
          if gold > 0:
            print("Also, your sweet Golden Donkey Kong Hammer managed to purge the machine of 50 Coins extra. Your Golden Hammer(s) has(ve) ", gold, " uses left.")
        elif rob == 10:
          import random
          robby = random.randint(1,5)
          if robby == 1 or robby == 3 or robby == 4 or robby == 5:
            coins -= 5
            print("oof")
            print("You take out your mini Donkey Kong Hammer and attempt to break the gamble machine open, but your regular hammer breaks, forcing you to a buy a new one. You lost 5 coins.")
            if gold > 0:
              print("However, your sweet Golden Donkey Kong Hammer managed to purge the machine of 50 Coins before your old hammer broke. Your Golden Hammer(s) has(ve) ", gold, " uses left.")
          elif robby == 2:
            coins += 300
            print("bruh")
            print("You take out your mini Donkey Kong Hammer and attempt to break the gamble machine open, and it pops open and you take everything! You have gained 300 coins.")
            if gold > 0:
              print("And on top of that your sweet Golden Donkey Kong Hammer managed to purge the machine of 50 Coins extra Coins! Your Golden Hammer(s) has(ve) ", gold, " uses left.")
        elif rob == 11:
          print("you fricking donkey")
          if PEPE > 0:
            PEPE -= 1
            print("You take out your mini Donkey Kong Hammer and attempt to break the gamble machine open, but the police found you! But before you could be eliminated, you showed them your pepe badge and that delayed them enough for you to escape. You got 0 Coins.")
            if gold > 0:
              print("However, your sweet Golden Donkey Kong Hammer managed to purge the machine of 50 Coins during your strategic escape. Your Golden Hammer(s) has(ve) ", gold, " uses left.")
          else:
            print("You take out your mini Donkey Kong Hammer and attempt to break the gamble machine open, but the police found you and eliminated you on the spot.")
            import time
            time.sleep(8)
            exit = "true"
      if choice == "shop":
        print("Welcome to the shop!")
        print(" ")
        print("Your Coins:" , coins , White)
        print("1. Donkey Kong Hammer Upgrade: 50 Coins")
        print(White + "(Procures an extra 10 Coins while stealing! Lasts until you die.)")
        print(" ")
        print("2. Fake Pepe Badge: 500 Coins ")
        print(White + "(Escape elimination by the police. Lasts 3 times.)")
        print(" ")
        print("3. AirPods Pro: 100 Coins ")
        print(White + "(+ 10 Coins when working because at this point your boss just wants to steer clear of you. They can break occasionally, forcing you to buy new ones.)")
        print(" ")
        print("4. Golden Donkey Kong Hammer: 500 Coins" + White)
        print("(+ 50 Coins when stealing. 5 Uses.)")
        print(" ")
        print("5. Frickin' assault rifle: 5000 Coins "+White)
        print("Bring this to work to uh, DRAMATICALLY increase your pay.")
        print(" ")
        print("6. Alter the quantum state: 10000000 Coins ")
        print("?")
        print(" ")
        print("7. Total monopoly: 2000000000 Coins ")
        print("Gain total control over the company you work for.")
        print(" ")
        print("More Coming Soon!")
        print(" ")
        shopchoice = str(input("What would you like to buy? (Type in item #, or say cancel.) "))
        if shopchoice == "1":
          if coins > 49:
            coins -= 50
            print("You bought the Donkey Kong Hammer Upgrade!" + White)
            HAM = "yes"
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "2":
          if coins > 499:
            coins -= 500
            PEPE += 3
            print("You bought the Fake Pepe Coin!" + White)
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "3":
          if coins > 99:
            coins -= 100
            air = "yes"
            print("You bought the AirPods Pro!" + White)
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "4":
          if coins > 499:
            coins -= 500
            gold += 5
            print("You bought the Golden Donkey Kong Hammer!" + White)
            print("")
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "5":
          if coins > 4999:
            coins -= 5000
            gun = "yes"
            print("You bought the Assault Rifle!" + White)
            print("")
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "6":
          if coins > 9999999:
            coins -= 10000000
            gamblehandicap = "yes"
            print("You altered the quantum state!" )
          else:
            print("bruh you don't have enough coins...")
        if shopchoice == "7":
          if coins > 1999999999:
            coins -= 2000000000
            monopoly = "yes"
            gun = "no"
            print("You have gained Total monopoly over your bosses company B)")
      if choice == "lottery":
        print("You currently have",coins ,"Coins.")
        print("")
        print("1. EZ - Loterry Ticket | Coins Won: 250"+White+" | Costs: 50 Coins")
        print("")
        print(White + "2. GoldenBebe - Lottery Ticket | Coins Won: 1000 "+White+"| Costs: 100 Coins"+White)
        print("")
        lottochoice = str(input("What would you like to buy? (Type in item #, or say cancel.) "))
        if lottochoice == "1":
          if coins > 49:
            coins -= 50
            print("You bought the EZ - Loterry Ticket!" + White)
            EZ = "yes"
          else:
            print("bruh you don't have enough coins...")
        if lottochoice == "2":
            if coins > 99:
              coins -= 100
              bebe = "yes"
              print("You bought the GoldenBebe - Loterry Ticket!" + White)
            else:
              print("bruh you don't have enough coins...")
        winlotto = random.randint(1,1000)
        if EZ == "yes":
          EZ = "no"
          if winlotto > 1:
            print("sucks to suck")
            print("You didn't win the EZ Lottery.")
          else:
            coins += 250
            print("winner winner")
            print("You won the EZ Lottery, nice going.")
        if bebe == "yes":
          bebe = "no"
          if winlotto > 1:
            print("sucks to suck")
            print("You didn't win the GoldenBebe Lottery.")
          else:
            coins += 1000
            print("winner winner")
            print("YOU WON THE GOLDENBEBE LOTTERY OH MY GOD")
      if choice == "devmode":
        print("")
        print("")
        cont = str(input("WARNING. ENTERING DEV MODE WILL DELETE ALL PROGRESS FROM GAMBLE GAME AND WILL SHOW HIDDEN VARIALBES THAT MAY AFFECT GAMEPLAY. Continue (y/n)? "))
        print("")
        print("")
        if cont == "y":
          devmode = "yes"
          coins = 10000000000000
          print("DEV MODE ON")
        else:
            if cont == "n":
              print("Aborting...")
            else:
              print("Invalid Syntax, aborting...")
        print("")
        print("")
      if choice == "help":
          print("You can gamble, work, enter the lottery, shop, or rob. If you have less than 10 coins, you die because you will not have enough to buy food and water. You start 100 coins.")
      if choice == "changelog":
          print("")
          print(changelog)
          print("")
      if devmode == "yes":
        print("")
        print("What your command was ",choice)
        print("Rob chance ",rob)
        print("Pay chance: ",pay)
        print("Gamble chance ",num)
        print("Rare rob chance ",robby)
        print("Airpod break chance ", airbreak)
        print("What you chose for shop ",shopchoice)
      if choice == "save":
          print("")
          print("SAVING PROGRESS, DO NOT CLOSE THIS WINDOW.")
          print("...")
          print("")
          val4 = HAM
          val5 = air
          val6 = gamblehandicap
          val7 = gun
          val8 = monopoly
          config.set("GAMBLEDATA", "coins", str(coins))
          config.set("GAMBLEDATA", "PEPE", str(PEPE))
          config.set("GAMBLEDATA", "gold", str(gold))
          config.set("GAMBLEDATA", "HAM", str(val4))
          config.set("GAMBLEDATA", "air", str(val5))
          config.set("GAMBLEDATA", "gamblehandicap", str(val6))
          config.set("GAMBLEDATA", "gun", str(val7))
          config.set("GAMBLEDATA", "monopoly", str(val8))
          config.write(open("GAMBLEDATA.ini", "w"))
          print("")
          time.sleep(1)
          print("Progress saved.")
          print("")
      if choice == "reset":
          print("")
          reset = str(input("WARNING. YOU WILL LOSE ALL DATA. CONTINUE? (y/n) "))
          if reset == "y":
              print("")
              print("ERASING ALL DATA. DO NOT CLOSE THIS WINDOW.")
              print("...")
              print("")
              val4 = HAM
              val5 = air
              val6 = gamblehandicap
              val7 = gun
              val8 = monopoly
              config.set("GAMBLEDATA", "coins", "100")
              config.set("GAMBLEDATA", "PEPE", "0")
              config.set("GAMBLEDATA", "gold", "0")
              config.set("GAMBLEDATA", "HAM", "no")
              config.set("GAMBLEDATA", "air", "no")
              config.set("GAMBLEDATA", "gamblehandicap", "no")
              config.set("GAMBLEDATA", "gun", "no")
              config.set("GAMBLEDATA", "monopoly", "no")
              config.write(open("GAMBLEDATA.ini", "w"))
              print("")
              time.sleep(1)
              print("Data erased. The program will now close.")
              time.sleep(0.5)
              print("")
              time.sleep(1)
              exit = "true"
          else:
            if cont == "n":
              print("Aborting...")
            else:
              print("Invalid Syntax, aborting...")

      if coins < 10:
        exit = "true"
      if choice == "exit":
        val4 = HAM
        val5 = air
        val6 = gamblehandicap
        val7 = gun
        val8 = monopoly
        config.set("GAMBLEDATA", "coins", str(coins))
        config.set("GAMBLEDATA", "PEPE", str(PEPE))
        config.set("GAMBLEDATA", "gold", str(gold))
        config.set("GAMBLEDATA", "HAM", str(val4))
        config.set("GAMBLEDATA", "air", str(val5))
        config.set("GAMBLEDATA", "gamblehandicap", str(val6))
        config.set("GAMBLEDATA", "gun", str(val7))
        config.set("GAMBLEDATA", "monopoly", str(val8))
        config.write(open("GAMBLEDATA.ini", "w"))
        exit = "true"
    if coins < 10:
        print("You died! Either you ran out of coins, or you were eliminated.")
        config.set("GAMBLEDATA", "coins", "100")
        config.set("GAMBLEDATA", "PEPE", "0")
        config.set("GAMBLEDATA", "gold", "0")
        config.set("GAMBLEDATA", "HAM", "no")
        config.set("GAMBLEDATA", "air", "no")
        config.set("GAMBLEDATA", "gamblehandicap", "no")
        config.set("GAMBLEDATA", "gun", "no")
        config.set("GAMBLEDATA", "monopoly", "no")
        config.write(open("GAMBLEDATA.ini", "w"))
    time.sleep(3)
    return_all()
else:
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
