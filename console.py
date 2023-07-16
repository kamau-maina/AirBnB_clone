#!/usr/bin/python3
""" entry point to the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb)"

    def do_exit(self, arg):
        """The exit command"""
        return True

    def do_EOF(self, line):
        """End of file commaond
        return True"""
        return True

    def emptyline(self):
        """pass when an empty line has been entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
