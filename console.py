#!/usr/bin/python3
"""Module: console.py"""
import cmd
import models
import re
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program\n """
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program\n """
        print()
        return True

    def emptyline(self):
        """ Handle empty lines"""
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
