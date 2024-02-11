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
        '''show obj representation'''
        my_args = arg.split()
        if self.check_id_exist(arg):
            print(models.storage.all()["{}.{}\
".format(my_args[0], my_args[1])])
    
    def check_id_exist(self, arg):
        """
        check if class && id exist
        """
        my_args = arg.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return False
        if my_args[0] not in HBNBCommand.list_classess:
            print("** class doesn't exist **")
            return False
        if len(my_args) < 2:
            print("** instance id missing **")
            return False
        if my_args[0] + "." + my_args[1] in models.storage.all():
            return True
        print("** no instance found **")

    def do_destroy(self, arg):
        '''command that destroy obj'''
        my_args = arg.split()
        if self.check_id(arg):
            del models.storage.all()["{}.{}\
".format(my_args[0], my_args[1])]
            models.storage.save()

    def do_all(self, arg):
        '''command prints all objs representation'''
        if arg == "":
            list = []
            for key in models.storage.all():
                list.append(str(models.storage.all()[key]))
            print(list)
        else:
            if arg.split()[0] in HBNBCommand.list_classess:
                list = []
                for key in models.storage.all():
                    if arg.split()[0] in key:
                        list.append(str(models.storage.all()[key]))
                print(list)
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
