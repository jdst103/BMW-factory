from factory_functions import *
import time
if __name__ == '__main__':
    while True:
        client_input = input('\nWelcome to the BMW Factory in China!! what would you like to do? '
                             '\nEnter "1" to run tests on our factory or "2" to create your own personal '
                             'Ultimate Driving Experience..!\n:')
        if client_input == '1':
            print('lets run some successful tests!')
            time.sleep(0.8)
            print('hopefully...')
            time.sleep(1)
            from factory_test import *

        elif client_input == '2':
            print('lets make your your personal own'
                             'Ultimate Driving Experience..!')
            arg1 = input('what material do you want!')
            arg2 = input('Do you want handmade experience to tailor to your needs? - TYPE "labour"?\n..OR our state of the art... '
                         'sewing machine!. - ENTER "sewing machine"')
            result = run_factory(arg1, arg2)
            print(result)
        elif client_input == 'stop':
                break
        else:
            print('sorry that"s not a valid option! Please try again')
