#!/usr/bin/python3
'''AIRBNB console'''

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_EOF(self, line):
        '''Quit command to exit the program'''
        return True
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True
    def emptyline(self):
        pass

    def do_create(self, arg):
        """command that create new instance"""
        name_of_class = arg.split()
        if len(name_of_class[0]) == 0:
            print("** class name missing **")
        elif name_of_class[0] not in HBNBCommand.list_classess:
            print("** class doesn't exist **")
        else:
            new = eval(name_of_class[0])()
            models.storage.save()
            print(new.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
