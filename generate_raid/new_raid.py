import os, ConfigParser
from datetime import date
import common
from common import *

class NewRaid(object):

    def __init__(self, sections, ticket_number, raid_config_path='~/.raidconfig'):
        self.user = utilities.get_user()
        self.sections = sections
        self.ticket_number = ticket_number
        self.__set_date()
        self.__set_raid_path(raid_config_path)

    def __set_date(self):
        today = date.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day

    def __set_path(self, raid_config_path):
        raid_config = ConfigParser.ConfigParser()
        raid_config.readfp(open(os.path.expanduser(raid_config_path)))
        self.path = raid_config.get('location', 'path')

    def __set_raid_path(self, raid_config_path):
        self.__set_path(raid_config_path)
        self.raid = os.path.join(self.path, "raid{ticket_number}.txt".format(ticket_number=self.ticket_number))

    def save(self):
        with open(self.raid, 'w') as raid:
            raid.writelines(['hi\n', 'there\n'])
            raid.close()

def NewRaidMain():
    print 'yup'
