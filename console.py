#!/usr/bin/python3
'''
AirBnB_ console'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    define HBNBCommand class'''

    prompt = '(hbnb)  '

    def do_EOF(self, line):
        '''
        EOF command'''
        return True

    def do_quit(self, line):
        '''
        Quit command to exit the program'''
        return True

    def emptyline(self):
        '''
        emptyline haldle'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
