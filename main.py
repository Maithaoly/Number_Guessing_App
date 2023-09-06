import myFunction
import os


def main():
    while (True):
        
        print('-'*85)
        print('\t\t\t\tNumber Guessing App')
        print('-'*85)
        print('\t\t\t\t1. Rules Of Game')
        print('\t\t\t\t2. Start Game')
        print('\t\t\t\t3. Exit')
        res = int(input('\nInput you choice...'))
        flag = 0
        
        match res:
            case 1:
                os.system('cls')
                f = open("rule.txt", "r")
                print(f.read())
                
            case 2:
                os.system('cls')
                myFunction.PlayGame()

            case 3:
                os.system('cls')
                flag = 1
                
        if flag == 1:
                print('EXIT GAME !!!')
                return 1
        
if __name__ == '__main__':
    main()