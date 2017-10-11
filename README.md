# pikachu

[![Join the chat at https://gitter.im/pikachu_/Lobby](https://badges.gitter.im/pikachu_/Lobby.svg)](https://gitter.im/pikachu_/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
IRC BOT - using python3
This bot is very useful for organizing the Online Sessions over IRC in a great way.

### Features
1. Maintaing a proper queue of doubts during session.
2. Fetch recent tweets from the given twitter handel.

You can send the following commands to the bot in a PM:

|Command|Description|Channel|Who|
|---|---|---|---|
|`!`|Queue yourself to ask a question during a session|Channel|Any user|
|`:clearqueue`|Clear the question queue|Channel|Admin|
|`:show`|Show the status of the question queue|PM/Channel|Admin|
|`:next`|Ping the next person in the queue to ask their question|Channel|Admin|
|`:add [nick]`|Add `nick` to masters list|PM/Channel|Admin|
|`:remove [nick]`|Remove `nick` from masters list|PM/Channel|Admin|
|`:tweet`|Show the recent tweet in the twitter handle|Channel|Any user|

### Commands for pikachu:

pikachu: yourmessage
  * yourmessage can be
    1. hi/hey/hello
    2. time 
    3. date
    4. goodbye
    5. master


### Install dependencies with:
`$ pip install -r requirements.txt`

### Now run the bot with:
`$ python config.py`
