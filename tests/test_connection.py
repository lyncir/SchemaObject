#!/usr/bin/python

"""
Tests for the Database Connection URL (RFC 1738)
http://www.ietf.org/rfc/rfc1738.txt
"""

import unittest
from schemaobject.connection import REGEX_RFC1738
from schemaobject.connection import build_database_url


class TestDatabaseURL(unittest.TestCase):

    def test_user_pw_host_port_db(self):
        test = "mysql://user:password@localhost:3306/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), 'password')
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), 'database')

    def test_user_pw_host_db(self):
        test = "mysql://user:password@localhost/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), 'password')
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')


    def test_user_pw_db(self):
        test = "mysql://user:password@/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), 'password')
        self.assertEqual(matches.group('host'), '')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')

    def test_host_port_db(self):
        test = "mysql://localhost:3306/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), None)
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), 'database')

    def test_host_db(self):
        test = "mysql://localhost/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), None)
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')


    def test_host(self):
        test = "mysql://localhost"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), None)
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), None)

    def test_host_port(self):
        test = "mysql://localhost:3306"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), None)
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), None)

    def test_db(self):
        test = "mysql:///database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), None)
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), '')
        self.assertEqual(matches.group('port'), None)


    def test_empty_user_host_port_db(self):
        test = "mysql://@localhost:3306/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), '')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), 'database')

    def test_empty_user_host_port(self):
        test = "mysql://@localhost:3306"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), '')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), None)

    def test_empty_user_host_db(self):
        test = "mysql://@localhost/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), '')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')

    def test_empty_user_db(self):
        test = "mysql://@/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), '')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), '')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')

    def test_user_host_port_db(self):
        test = "mysql://user@localhost:3306/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), 'database')

    def test_user_host_db(self):
        test = "mysql://user@localhost/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), None)
        self.assertEqual(matches.group('database'), 'database')

    def test_user_host_port(self):
        test = "mysql://user@localhost:3306"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), 'localhost')
        self.assertEqual(matches.group('port'), '3306')
        self.assertEqual(matches.group('database'), None)

    def test_user_db(self):
        test = "mysql://user@/database"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), None)
        self.assertEqual(matches.group('host'), '')
        self.assertEqual(matches.group('port'), None)

    def test_user_pw(self):
        test = "mysql://user:password@"
        matches = REGEX_RFC1738.match(test)

        self.assertTrue(matches)
        self.assertEqual(matches.group('protocol'), 'mysql')
        self.assertEqual(matches.group('username'), 'user')
        self.assertEqual(matches.group('password'), 'password')
        self.assertEqual(matches.group('host'), '')
        self.assertEqual(matches.group('port'), None)

    def test_build_url_host(self):
        url = build_database_url('host')
        self.assertEqual(url, 'mysql://root@host:3306/')

    def test_build_url_database(self):
        url = build_database_url(host='host', password='pwd', database='test')
        self.assertEqual(url, 'mysql://root:pwd@host:3306/test')

    def test_build_url_missed_host(self):
        self.assertRaises(TypeError, build_database_url)