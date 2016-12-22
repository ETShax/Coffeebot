# -*- coding: UTF-8 -*-

"""
muutama esimerkki komennoista
"""

import random, time, os
from subprocess import call

# tÃ¤hÃ¤n sanastoon lisÃ¤tÃ¤Ã¤n komennot ja niitÃ¤ vastaavat oliot

command_dict = {}


class Test:
    def main(self, irc, line):
        irc.send('PRIVMSG %s :Hell World!' % line[2])


command_dict[':!test'] = Test()


class Join:
    def main(self, irc, line):
        if line[0] in irc.users:
            irc.send('JOIN %s' % (line[4]))


command_dict[':!join'] = Join()


class Quit:
    def main(self, irc, line):
        # mÃ¤Ã¤ritellÃ¤Ã¤n komento vain pÃ¤Ã¤kÃ¤yttÃ¤jille

        if line[0] in irc.users:
            irc.send('QUIT')
            irc.socket.close()
            irc.done = 1


command_dict[':!quit'] = Quit()


class Kahvia:
    # tarttee olla yhteys karahkaan
    def main(self, irc, line):
                os.system('ssh user@raspi "python ~/raspit/harkka/kahvitulos.py "' )
                os.system('scp user@raspi:~/raspit/harkka/kahvitulos.txt .')
        	tulos = open('kahvitulos.txt', 'r')
        	for laini in tulos:
            		irc.send('PRIVMSG %s :%s' % (line[2], laini))



command_dict[':!kahvi'] = Kahvia()


