import unittest
from generate_raid import new_raid
from nose.tools import istest
import os, re, ConfigParser, pytest

#@pytest.fixture()
#def testconfig():
#    newpath = tempfile.mkdtemp()
#    os.chdir(newpath)
#    config_txt = '''
#[location]
#path={working_directory}
#'''.format(working_directory=os.getcwd())
#    with open("config", 'w') as c:
#        c.write(config_txt)
#        c.close()
#    if not os.path.isfile(os.path.join(os.getcwd(), "config")):
#        raise ValueError('nope')
#
#@pytest.fixture()
#def cleanup():
#    delete_file = os.path.join('/tmp', 'raid1234.txt')
#    os.remove(delete_file)
#
#
#@pytest.fixture()
#def add_file():
#    with open('/tmp/die_please', 'w') as f:
#        f.write('die\nplease')
#        f.close()

@pytest.mark.usefixtures("cleandir")
class GenerateRaidTest(unittest.TestCase):

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

#    header_template = '''#****************************************************************************
##Copyright (C) {year} Expedia, Inc. All rights reserved.
##
##Description:
##Jira {ticket_number}: {description}
##
##Change History:
##  Date        Author         Description
##  ----------  -------------- ------------------------------------
##  {today}  {author}       {change_description}
##****************************************************************************
#'''
#    @classmethod
#    def setUpClass(self):
#        pass
#
#    @istest
#    def simple_raid(self):
#        '''Simple raid file.'''
#        sections = ['db2', 'informatica', 'sqlserver']
#        raid = GenerateRaid(sections, ticket_number = 1234)
#        assert type(raid.ticket_number) is int
#        assert type(raid.sections) is list
#        assert type(raid.user) is str
#
#        assert len(str(raid.year)) == 4
#        assert type(raid.year) is int
#
#        assert len(str(raid.month)) <= 2
#        assert type(raid.month) is int
#
#        assert len(str(raid.day)) <= 2
#        assert type(raid.day) is int
#
#
#    @istest
#    def raid_config(self):
#        '''Gets path from raid config.'''
#        raid_config = ConfigParser.ConfigParser()
#        raid_config.readfp(open(os.path.expanduser('~/.raidconfig_for_test')))
#        path = raid_config.get('location', 'path')
#        assert os.path.exists(path)
#
#    @istest
#    def create_raid(self):
#        '''Creates a raid file.'''
#        sections = ['db2']
#        raid = GenerateRaid(sections, ticket_number=1234, raid_config_path='~/.raidconfig_for_test')
#        raid.write_raid()
#        assert os.path.isfile(os.path.join(raid.path, "raid{ticket_number}.txt".format(ticket_number=raid.ticket_number)))
#
#    @istest
#    def header(self):
#        '''Lame header test in generate_raid.'''
#        header = self.header_template.format(year=2014, ticket_number=94753, description="Example jira desc.", today="2014-01-06", author="mschober", change_description="example change desc")
#        self.assertEquals(header, '''#****************************************************************************
##Copyright (C) 2014 Expedia, Inc. All rights reserved.
##
##Description:
##Jira 94753: Example jira desc.
##
##Change History:
##  Date        Author         Description
##  ----------  -------------- ------------------------------------
##  2014-01-06  mschober       example change desc
##****************************************************************************
#''')
#
