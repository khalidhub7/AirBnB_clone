#!/usr/bin/python3
'''
airbnb console
'''
from models.engine.file_storage import FileStorage
from models import storage
import shlex
import cmd
from models.base_model import BaseModel
import sys
import json


class HBNBCommand(cmd.Cmd):
    '''
    define HBNBCommand
    prompt: prompt
    list_classess: all class used names
    '''

    prompt = "(hbnb) "
    list_classess = ["BaseModel", "User", "State", "City", "Amenity\
", "Place", "Review"]

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

    def check_id_exist(self, arg):
        '''
        check if class && id exist
        '''
        myargs = shlex.split(arg)
        if len(myargs) == 0:
            print("** class name missing **")
            return False
        if myargs[0] not in HBNBCommand.list_classess:
            print("** class doesn't exist **")
            return False
        if len(myargs) < 2:
            print("** instance id missing **")
            return False
        if myargs[0]+"."+myargs[1] in storage.all():
            return True
        print("** no instance found **")

    def check_attr_exist(self, arg):
        '''
        check if attribute exist
        '''
        myargs = shlex.split(arg)
        if len(myargs) < 3:
            print("** attribute name missing **")
            return False
        if len(myargs) < 4:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        '''show command to prints object representation'''
        myargs = shlex.split(arg)
        if self.check_id_exist(arg):
            print(storage.all()["{}.{}\
".format(myargs[0], myargs[1])])

    def do_destroy(self, arg):
        '''destroy command that destroy object'''
        myargs = shlex.split(arg)
        if self.check_id_exist(arg):
            del storage.all()["{}.{}\
".format(myargs[0], myargs[1])]
            storage.save()

    def do_all(self, arg):
        '''print all objects representation'''
        if arg == "":
            list_string = []
            for key in storage.all():
                list_string.append(str(storage.all()[key]))
            print(list_string)
        else:
            if arg.split()[0] in HBNBCommand.list_classess:
                list_string = []
                for key in storage.all():
                    if arg.split()[0] in key:
                        list_string.append(str(storage.all()[key]))
                print(list_string)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        '''update command that update an object'''
        if self.check_id_exist(arg):
            if self.check_attr_exist(arg):
                args_list = shlex.split(arg)
                obj = storage.all()[f"{args_list[0]}.{args_list[1]}"]
                if hasattr(obj, args_list[2]):
                    try:
                        value = type(getattr(obj, args_list[2]))(args_list[3])
                        setattr(obj, args_list[2], value)
                    except ValueError:
                        pass
                else:
                    value = args_list[3]
                    try:
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                    except ValueError:
                        value = args_list[3]
                    setattr(obj, args_list[2], value)
                obj.save()

    def do_quit(self, line):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''C-d command to exit the program'''
        return True

    def emptyline(self):
        '''an empty line handling'''
        pass

    def default(self, line):
        '''
        default commands
        '''
        if line.endswith(".all()"):
            '''
            Check if command matches <class_name>.all()
            '''
            if line[:-6] != "":
                self.do_all(line[:-6])
        elif line.endswith(".count()"):
            '''
            Check if command matches <class_name>.count()
            '''
            if line[:-8] != "":
                if line[:-8] in HBNBCommand.list_classess:
                    num_obj = 0
                    for key in storage.all():
                        if line[:-8] in key:
                            num_obj += 1
                    print(num_obj)
                else:
                    print("** class doesn't exist **")

        elif ".show(" in line and line.endswith(")"):
            '''
            Check if command matches <class_name>.show(<id>)
            '''
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_show(className+" "+id)

        elif ".destroy(" in line and line.endswith(")"):
            '''
            Check if command matches <class_name>.destroy(<id>)
            '''
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_destroy(className+" "+id)

        elif ".update(" in line and line.endswith(")"):
            className = line.split(".")[0]
            args = line.split("(")[1][:-1]
            if "{" in args and args.endswith("}"):
                id = args.split(", ")[0]
                str_dict = "{"+args.split("{")[1]
                dictionary = dict(eval(str_dict))
                string = className+" "+id
                for attr in dictionary:
                    self.do_update(string+" \
"+attr+" "+"\""+str(dictionary[attr])+"\"")
            else:
                string = className
                for elem in args.split(", "):
                    string += " "+elem
                self.do_update(string)
        else:
            print("*** Unknown syntax: "+line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
