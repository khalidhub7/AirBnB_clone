#!/usr/bin/python3
'''AIRBNB console'''

import cmd
import models
import shlex


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
        '''command that create new instance'''
        name_of_class =""
        for i in arg:
            name_of_class += i
            if i == ' ':
                break
        if len(name_of_class) == 0:
            print("** class name missing **")
        elif name_of_class not in HBNBCommand.list_classess:
            print("** class doesn't exist **")
        else:
            models.storage.save()
            print(name_of_class.id)

    def do_show(self, arg):
        """show command to prints object representation"""
        args_list = shlex.split(arg)
        if self.check_id(arg):
            print(models.storage.all()["{}.{}\
".format(args_list[0], args_list[1])])

    def check_id(self, arg):
        """
        check if class name and id exist
        """
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return False
        if args_list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False
        if len(args_list) < 2:
            print("** instance id missing **")
            return False
        if args_list[0]+"."+args_list[1] in storage.all():
            return True
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
