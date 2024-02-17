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
        '''
        create command to creates a new instance
        '''
        nameof_class = arg.split()
        if len(nameof_class) == 0:
            print("** class name missing **")
        elif nameof_class[0] not in HBNBCommand.list_classess:
            print("** class doesn't exist **")
        else:
            new = eval(nameof_class[0])()
            storage.save()
            print(new.id)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
