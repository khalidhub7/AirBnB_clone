#!/usr/bin/python3
'''AIRBNB console'''

import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    list_classess = ["BaseModel", "User", "State", "City\
", "Amenity", "Place", "Review"]
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
        if self.check_id_exist(arg):
            del models.storage.all()["{}.{}\
".format(my_args[0], my_args[1])]
            models.storage.save()
    
    def do_all(self, arg):
        '''command prints all objs representation'''
        if arg == "":
            list = []
            for i in models.file_storage.FileStorage.all():
                list.append(str(models.storage.all()[i]))
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
    
    def do_update(self, arg):
        '''command that update obj'''
        if self.check_id_exist(arg):
            if self.check_attr_ifexist(arg):
                myargs = arg.split()
                obj = models.storage.all()[f"{myargs[0]}.{myargs[1]}"]
                if hasattr(obj, myargs[2]):
                    try:
                        value = type(getattr(obj, myargs[2]))(myargs[3])
                        setattr(obj, myargs[2], value)
                    except ValueError:
                        pass
                else:
                    value = myargs[3]
                    try:
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                    except ValueError:
                        value = myargs[3]
                    setattr(obj, myargs[2], value)
                obj.save()
        
    def check_attr_ifexist(self, arg):
        '''
        check attribute if exist
        '''
        myargs = arg.split()
        if len(myargs) < 3:
            print("** attribute name missing **")
            return False
        if len(myargs) < 4:
            print("** value missing **")
            return False
        return True
    
    def default(self, line):
        '''
        default coooooommands
        '''
        if line.endswith(".all()"):
            '''
            Check if the command matches
            <class_name>.all()
            '''
            if line[:-6] != "":
                self.do_all(line[:-6])
        elif line.endswith(".count()"):
            '''
            Check if the command matches
            <class_name>.count()
            '''
            if line[:-8] != "":
                if line[:-8] in HBNBCommand.list_classess:
                    num_obj = 0
                    for key in models.storage.all():
                        if line[:-8] in key:
                            num_obj += 1
                    print(num_obj)
                else:
                    print("** class doesn't exist **")

        elif ".show(" in line and line.endswith(")"):
            '''
            Check if the command matches
            <class_name>.show(<id>)
            '''
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_show(className+" "+id)

        elif ".destroy(" in line and line.endswith(")"):
            '''
            Check if the command matches
            <class_name>.destroy(<id>)
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
                for elm in args.split(", "):
                    string += " "+elm
                self.do_update(string)
        else:
            print("*** Unknown syntax: "+line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
