#!/usr/bin/python3
'''
AirBnB_ console'''
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    define HBNBCommand class'''

    classes_defined = {'BaseModel', 'User', 'State',\
'City', 'Place', 'Amenity', 'Review'}

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
        spliter = arg.split()
        if len(spliter) == 0:
            print('** class name missing **')
            return
        elif spliter[0] not in HBNBCommand.classes_defined:
            print('** class doesn\'t exist **')
            return
        else:
            new__instance = globals()[spliter[0]]()
            return new__instance

    def do_show(self, arg):
        """show command to prints object representation"""
        args_list = shlex.split(arg)
        if self.check_id(arg):
            print(storage.all()["{}.{}\
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
