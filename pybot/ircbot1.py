# -*- coding: cp1252 -*-

"""
yksinkertainen ircbotti

komennot:
    !test
    !join
    !quit
    !anagram
"""

import socket
import botcommands
import time
asd = 0
class Ircbot1:

    def __init__( self ):

        # määritellään botille pääkäyttäjät

        self.users = [ ':ETS!harbinger@paija.us' ]

        # välttämättömiä tietoja

        self.server   = 'irc.portlane.se'
        self.port     = 6667
        self.username = 'orjatar'
        self.realname = 'larvae'
        self.nick     = 'injektio'

        # luodaan socket
	
        self.socket = socket.socket()
	
        # haetaan botille komennot

        self.commands = botcommands.command_dict

        # päälooppia toistettan kunnes done = 1

        self.done     = 0

        # kanava jolle botti halutaan

        self.channel  = '#etstestaa'

    def send( self, string ):

        # tällä lähetetään viestejä

        self.socket.send( string + '\r\n' )

    def connect( self ):

        # yhdistetään serveriin ja läheteään omat tiedot
        self.socket.connect( ( self.server, self.port ) )
        self.send( 'NICK %s' % self.nick )
        self.send( 'USER %s a a :%s' % ( self.username, self.realname ) )

        # liitytään kanavalle

        self.send( 'JOIN %s' % self.channel )

    def check( self, line ):
        global asd
        print line
        line = line.split(' ')

        # vastataan pingiin muuten serveri katkaisee yhteyden

        if line[0] == 'PING':

             self.send( 'PONG '+line[1] )
        if line.__contains__("221"):
             self.send('JOIN %s' % self.channel)
        if line.__contains__("!reload"):
            reload(botcommands)
        try:

            # vastataan komentoihin myös yksityiskeskutelussa

            if line[2][0] != '#':

                line[2] = line[0].split( '!' )[0][1:]

            # suoritetaan komennot jos niitä on tullut
            if (time.time()-asd) >6:

                self.commands[ line[3] ].main( self , line )

                asd = time.time()
        except:

            pass

    def mainloop( self ):


        buffer = ''

        while not self.done:

        # vastaanotetaan dataa

            buffer += self.socket.recv( 4096 )
            buffer = buffer.split( '\r\n' )

            for line in buffer[0:-1]:

                self.check( line )

                if len(buffer)>1:
                    buffer = buffer[-1]

def main():

    irc = Ircbot1()
    irc.connect()
    irc.mainloop()

if __name__ == '__main__': main()
