#!/usr/bin/python3
'''
AirBnB_ console'''
import cmd
from models import storage


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

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
