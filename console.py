#!/usr/bin/python3
'''AIRBNB console'''

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_EOF(self, line):
        """end"""
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
