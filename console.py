#!/usr/bin/python3
"""
Module of AIRBNB console
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import shlex
import sys
import json


class HBNBCommand(cmd.Cmd):
    """
    define HBNBCommand class

    Classe Attributes:
        prompt (str): The prompt.
        classes_list (list): A list of all used class names.
    """

    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City\
", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """create command to creates a new instance\n"""
        className = arg.split()
        if len(className) == 0:
            print("** class name missing **")
        elif className[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        else:
            new_obj = eval(className[0])()
            storage.save()
            print(new_obj.id)

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

    def check_attr(self, arg):
        """
        check if attribute name exist
        """
        args_list = shlex.split(arg)
        if len(args_list) < 3:
            print("** attribute name missing **")
            return False
        if len(args_list) < 4:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        """show command to prints object representation"""
        args_list = shlex.split(arg)
        if self.check_id(arg):
            print(storage.all()["{}.{}\
".format(args_list[0], args_list[1])])

    def do_destroy(self, arg):
        """destroy command that destroy object"""
        args_list = shlex.split(arg)
        if self.check_id(arg):
            del storage.all()["{}.{}\
".format(args_list[0], args_list[1])]
            storage.save()

    def do_all(self, arg):
        """all command thar prints all objects representation"""
        # TODO: all BaseModel dgf
        if arg == "":
            list_str = []
            for key in storage.all():
                list_str.append(str(storage.all()[key]))
            print(list_str)
        else:
            if arg.split()[0] in HBNBCommand.classes_list:
                list_str = []
                for key in storage.all():
                    if arg.split()[0] in key:
                        list_str.append(str(storage.all()[key]))
                print(list_str)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """update command that update an object"""
        if self.check_id(arg):
            if self.check_attr(arg):
                args_list = shlex.split(arg)
                obj = storage.all()[f"{args_list[0]}.{args_list[1]}"]
                if hasattr(obj, args_list[2]):
                    # TODO: handle casting error by using try except
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
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """C-d command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line handling"""
        pass

    def default(self, line):
        """
        default commands
        """
        if line.endswith(".all()"):
            """
            Check if the command matches
            <class_name>.all()
            """
            if line[:-6] != "":
                self.do_all(line[:-6])
        elif line.endswith(".count()"):
            """
            Check if the command matches
            <class_name>.count()
            """
            if line[:-8] != "":
                if line[:-8] in HBNBCommand.classes_list:
                    num_obj = 0
                    for key in storage.all():
                        if line[:-8] in key:
                            num_obj += 1
                    print(num_obj)
                else:
                    print("** class doesn't exist **")

        elif ".show(" in line and line.endswith(")"):
            """
            Check if the command matches
            <class_name>.show(<id>)
            """
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_show(className+" "+id)

        elif ".destroy(" in line and line.endswith(")"):
            """
            Check if the command matches
            <class_name>.destroy(<id>)
            """
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
                for elm in args.split(", "):
                    string += " "+elm
                self.do_update(string)
        else:
            print("*** Unknown syntax: "+line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
