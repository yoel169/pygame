import json

# =========================================== LEVEL PACK SCRIPT TO MAKE LEVELS =====================================
# Follow the prompts to make level packs. If you need help check description.

# validate input but not working
def validate(string):

    ls = ()

    while True:
        try:
            ls = list(map(str, input(string).split()))
        except ValueError:
            print("invalid number of arguments!")
            continue
        else:
            return ls
            break


# validate number of enemies with number of %
def validateRange(string,x):

    ls = []
    while True:
        try:
            ls = list(map(int, input(string).split()))
        except ValueError:
            print("invalid number!")
            continue
        if len(ls) == x:
            return ls
            break
        else:
            print("invalid number of arguments!")


print("Welcome to Yoel's Level maker automator!")
cont = input("Would you like a description of the level pack maker? y/n: ")

# PRINT DESCRIPTION
if cont == 'y':
    print('\n -------------------------------------------------------------------------------------------------------')
    print("First I will ask you how many levels you want in your level pack.")
    print("Then I will ask how many waves for the level. Then the max score for the wave.")
    print("Next, I will ask if you to spawn a single enemy or grouped. If single, the next prompt will be to get: spawn"
          " type, spawn value and enemy type. " )
    print('spawn types: time, score, or random. value for spawn: time is in ms, score, or a random % chance to spawn '
          'every second.')
    print("Last value is the enemy type as int. If grouped, first will ask for spawn type and spawn value.")
    print("After, it will ask for the enemy types, order matters.An additional prompt will be asked for spawn % between"
          " each. It should total to 100 between all of them. ")
    print("It expects the same number of arguments as enemies. Example: types 0 3 2 expects three values at the last "
          "prompt.")
    print("Heres an example for single: single -> time 500 0. That makes a single enemy type 0 to spawn every 500ms.")
    print("Heres an example for grouped: group -> score 25 -> 0 2 -> 50 50. That makes two enemies type 0 and 2, every "
          "25 score theres a 50% chance one of them will spawn. ")
    print("If you don't want to spawn an enemy or don't want more, you can type in cont to continue to buffs, or exit "
          "to exit scripter.")
    print('Next will be buff, same concept as above. Single buff example: single -> random 5 2. Makes a buff'
          ' of type 2 with a 5% chance to spawn every second. ')
    print("After you're done with the wave, it will proceed to the next wave or next level. ")
    print("If all the levels are done it will save it to a json file and prompt you if you want to make another level "
          "pack.")
    print('----------------------------------------------------------------------------------------------------------')

print('\n')

exit = False  # for leaving
script = ['enemy', 'buff']  # for prompting between enemy and buff
levels = ['levels']  # save all the levels
fileCounter = 1  # for saving the packs into diff json files

# LEVEL PACK LOOP
while not exit:

    # get number of levels
    levelC = int(input("How many levels do you want in your level pack: "))

    # LEVEL LOOP
    for y in range(1, levelC + 1):

        print('\n')
        level = {'waves': []}  # level to hold all the waves

        # get number of waves
        print('-------- Level ' + str(y) + ' -------')
        waves = int(input("How many waves do you want in your level: "))

        # WAVES LOOP
        for x in range(1, waves + 1):

            print('------- Wave ' + str(x)+ ' --------')

            # get max score for wave and init enemy and buff lists to be added
            maxScore = int(input("Max score for wave: "))
            enemies = []
            buffs = []
            appender = [enemies, buffs]  # switch between lists

            # SETTING ENEMIES AND BUFFS LOOP
            for x in range(0,2):

                # GET X AMOUNT ENEMY/BUFF
                while True:

                    # USER VALIDATE
                    while True:
                        checker = input("* New " + script[x] + ": single or group (cont or exit): ")

                        if checker == 'exit' or checker == 'single' or checker == 'group' or checker == 'cont':
                            break
                        else:
                            print("wrong input")

                    if checker == 'exit':
                        exit = True
                        break
                    elif checker == 'cont':
                        break
                    elif checker == 'group':

                        spawnT, spawnV = input("Enter spawn type and value: ").split()
                        type_ = list(map(int, input("Enter " + script[x] + " types: ").split()))
                        optional = validateRange("Enter % between enemy spawns: ", len(type_))

                        appender[x].append(['group', spawnT, spawnV, type_, optional])

                    elif checker == 'single':

                        spawnT, spawnV, type_ = input("Enter spawn type, spawn value and " + script[x]+ " type: ").split()
                        appender[x].append(['single', spawnT, int(spawnV), int(type_)])
            if exit:
                break
            else:
                wave = {'maxScore': maxScore, 'enemies': enemies, 'buffs':  buffs}
                level['waves'].append(wave)

        if exit:
            break
        else:
            print('\n')
            levels.append(level)

    if exit:

        print("You exited, nothing was saved. ")

    else:

        string = 'levelpack' + str(fileCounter) + '.json'

        with open(string, 'w') as f:
            json.dump(levels, f, indent=3)

        print("level pack saved to", string)

        anotherOne = input("Make another level pack? y/n")

        if anotherOne == 'n':
            exit = True
        else:
            fileCounter += 1
            print('\n')