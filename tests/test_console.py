#!/usr/bin/python3
"""
This module is for unit testing of the console.py file
at the base of the directories
"""
import sys
from io import StringIO
from unittest.mock import patch, Mock
from unittest import TestCase, skip
from console import HBNBCommand


class TestConsole(TestCase):
    """This class is for testing the console interpreter
    command, handling errors, output format.
    """

    def setUp(self):
        self.cmd_line = HBNBCommand()

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("quit")
            out = f.getvalue().strip()
            self.assertEqual(out, "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("EOF")
            out = f.getvalue().strip()
            self.assertEqual(out, "")

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("help count")
            out = f.getvalue().strip()
            expected = "\n\tRetrieve the number of instances of a class \
                    \n\tFormat: count <class name>, <class name>.count()"
            self.assertEqual(out, expected)

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("")
            out = f.getvalue().strip()
            self.assertEqual(out, "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("show")
            out = f.getvalue().strip()
            self.assertEqual(out, "** class name missing **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("show BaseModel")
            self.cmd_line.onecmd("show User")
            self.cmd_line.onecmd("show Place")
            self.cmd_line.onecmd("show State")
            self.cmd_line.onecmd("show City")
            self.cmd_line.onecmd("show Amenity")
            self.cmd_line.onecmd("show Review")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0], "** instance id missing **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("show BaseModel 122222211")
            self.cmd_line.onecmd("show City '1234344'")
            self.cmd_line.onecmd("show Place all")
            self.cmd_line.onecmd("show State chicago")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0], "** no instance found **")

    @skip("")
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd('create')
            out = f.getvalue().strip()
            self.assertEqual(out, "** class name missing **")
            f.truncate(0)
            f.seek(0)
            # self.cmd_line.onecmd("create BaseModel")
            self.cmd_line.onecmd("create User")
            self.cmd_line.onecmd("create Place")
            # self.cmd_line.onecmd("create State")
            # self.cmd_line.onecmd("create City")
            # self.cmd_line.onecmd("Create Review")
            # self.cmd_line.onecmd("create Amenity")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 2)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("update")
            out = f.getvalue().strip()
            self.assertEqual(out, "** class name missing **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("update BaseModel")
            self.cmd_line.onecmd("update User")
            self.cmd_line.onecmd("update Place")
            self.cmd_line.onecmd("update State")
            self.cmd_line.onecmd("update City")
            self.cmd_line.onecmd("update Review")
            self.cmd_line.onecmd("update Amenity")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0], "** instance id missing **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd_line.onecmd("destroy")
            out = f.getvalue().strip()
            self.assertEqual(out, "** class name missing **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("destroy Base")
            out = f.getvalue().strip()
            self.assertEqual(out, "** class doesn't exist **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("destroy BaseModel")
            self.cmd_line.onecmd("destroy User")
            self.cmd_line.onecmd("destroy Place")
            self.cmd_line.onecmd("destroy State")
            self.cmd_line.onecmd("destroy City")
            self.cmd_line.onecmd("destroy Amenity")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0], "** instance id missing **")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("destroy BaseModel 122222211")
            self.cmd_line.onecmd("destroy City 1234344 is my id")
            self.cmd_line.onecmd("destroy Place fake palace built")
            self.cmd_line.onecmd("destroy State imagineState")
            out_list = f.getvalue().strip().split('\n')
            out = list(set(out_list))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0], "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand.get_data = Mock()
            HBNBCommand.get_data.return_value = {}
            self.cmd_line.onecmd("all User")
            out = f.getvalue().strip()
            self.assertEqual(out, "[]")
            f.truncate(0)
            f.seek(0)
            self.cmd_line.onecmd("all")
            out = f.getvalue().strip()
            self.assertEqual(out, "[]")
