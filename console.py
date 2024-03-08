#!/usr/bin/python3
# Importing necessary modules
from models.engine.file_storage import FileStorage
from models import storage
import shlex
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    # Setting up command prompt and class list
    prompt = "(hbnb) "
    list_classes = ["BaseModel"]

    # Creating new instance
    def do_create(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.list_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            storage.save()
            print(new_instance.id)

    # Checking if ID exists
    def check_id_exist(self, arg):
        myargs = shlex.split(arg)
        if len(myargs) < 2:
            print("** class name missing **")
            return False
        if myargs[0] not in self.list_classes:
            print("** class doesn't exist **")
            return False
        if myargs[0] + "." + myargs[1] in storage.all():
            return True
        print("** no instance found **")

    # Showing object representation
    def do_show(self, arg):
        myargs = shlex.split(arg)
        if self.check_id_exist(arg):
            print(storage.all()["{}.{}".format(myargs[0], myargs[1])])

    # Destroying object
    def do_destroy(self, arg):
        myargs = shlex.split(arg)
        if self.check_id_exist(arg):
            del storage.all()["{}.{}".format(myargs[0], myargs[1])]
            storage.save()

    # Printing all objects representation
    def do_all(self, arg):
        if arg == "":
            print([str(obj) for obj in storage.all().values()])
        else:
            if arg.split()[0] in self.list_classes:
                print([str(obj) for obj in storage.all().values() if arg.split()[0] in obj.__class__.__name__])
            else:
                print("** class doesn't exist **")

    # Updating an object
    def do_update(self, arg):
        if self.check_id_exist(arg):
            args_list = shlex.split(arg)
            obj = storage.all()["{}.{}".format(args_list[0], args_list[1])]
            if hasattr(obj, args_list[2]):
                try:
                    value = type(getattr(obj, args_list[2]))(args_list[3])
                    setattr(obj, args_list[2], value)
                except ValueError:
                    pass
            else:
                value = args_list[3]
                try:
                    value = float(value) if '.' in value else int(value)
                except ValueError:
                    pass
                setattr(obj, args_list[2], value)
            obj.save()

    # Quitting the program
    def do_quit(self, line):
        return True

    # Exiting on end of file
    def do_EOF(self, line):
        return True

    # Handling empty line
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
