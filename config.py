import re
import socket
from replies import reply, find_in_Replies
from Queue import Queue
import urllib2
from bs4 import BeautifulSoup

user_queue = Queue()
# For sending messages to a specified channel
def sendmsg(chan, msg):
    global irc
    irc.send("PRIVMSG "+ chan +" :"+ msg + "\n")

# This is a subroutine which help to join a specified channel
def JoinChan(chan):
    global irc
    irc.send("JOIN "+ chan +"\n")


# This is a subroutine which responds to server pings
def ping():
    global irc
    irc.send ("PONG :pingis\n")


def tweet(chan):
    theurl = "https://twitter.com/pyconpune"
    thepage = urllib2.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    sendmsg(chan, soup.title.text)
    tweets = soup.findAll('div', {"class": "content"})[0]
    status = tweets.find('p', {'class': 'TweetTextSize TweetTextSize--16px js-tweet-text tweet-text'}).text
    # date = tweets.find('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'}).text
    # last_tweet = status + " " + date
    print status
    sendmsg(chan, status.encode('ascii', 'ignore'))



# This is a main routine
def main():
    global irc, user_queue
    botnick = "pikachu"
    bufsize = 2048
    admin = ["rahuldecoded"]
    channel = "#uit-foss"
    port = 6667
    server = "irc.freenode.net"
    master = "rahuldecoded"
    uname = "ircusername"
    realname = "realname"
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    irc.send("USER " + botnick + " " + botnick + " " + botnick + " :Hello! I am a test bot!\r\n")
    irc.send("NICK " + botnick + "\n")
    JoinChan(channel)

    pattern1 = '.*:(\w+)\W*%s\W*$' % botnick
    pattern2 = '.*:%s\W*(\w+)\W*$' % botnick

    while 1:
        try:
            ircmsg = irc.recv(bufsize)
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)
            m1 = re.match(pattern1, ircmsg, re.I)
            m2 = re.match(pattern2, ircmsg, re.I)
            if (m1 == None) and (m2 != None):
                m1 = m2

            if (m1 != None):  # Yes
                word = m1.group(1)  # Word found
                word = word.lower()  # Make word lower case
                # Print a reply
                if find_in_Replies(word):
                    sendmsg(channel, reply(word))

        except Exception:
            pass

    # Admin Commands

        # For showing the length of the queue.
        if ircmsg.split(" ")[-1] == "::show":
            if ircmsg.strip(":").split("!")[0] in admin:
                sendmsg(channel, str(user_queue.in_queue()) + " \n")

        # For getting to the next user in the queue.
        if ircmsg.split(" ")[-1] == "::next":
            if ircmsg.strip(":").split("!")[0] in admin:
                sendmsg(channel, str(user_queue.next_nick()) + " \n")
                user_queue.pop_next()

        # For clearing the queue.
        if ircmsg.split(" ")[-1] == "::clearqueue":
            if ircmsg.strip(":").split("!")[0] in admin:
                user_queue.clear()
                sendmsg(channel, "Queue cleared")

        # For adding someone as a admin
        if ircmsg.split(" ")[-2] == "::add":
            if ircmsg.strip(":").split("!")[0] in admin:
                admin.append(ircmsg.split(" ")[-1])

        # For removing someone from admin privilege.
        if ircmsg.split(" ")[-2] == "::remove":
            if ircmsg.strip(":").split("!")[0] in admin:
                try:
                    admin.remove(ircmsg.split(" ")[-1])
                except ValueError:
                    return ircmsg.split(" ")[-1] + "is not in admin list."




        # User Commands
        if ircmsg.find("PING :") != -1:
            ping()
        if ircmsg.split(" ")[-1] == ":!":
            user_name = ircmsg.strip(":").split("!")
            sendmsg(channel, str(user_name[0]) + " , you have added in queue. Wait for your turn.\n")
            user_queue.enqueue(user_name[0])
        if ircmsg.split(" ")[-1] == "::tweet":
            tweet(channel)


main()
exit(0)
