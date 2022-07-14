#Discord -> LiBeRtY#9024
from time import time
import os
import sys
if os.name =="nt":
    os.system('cls')
else:
    os.system('clear')

import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
header = """
         ,-.-.     ,----.             ,--.-,,-,--,   _,.---._       _,.---._    ,--.-.,-.  
,-..-.-./  \==\ ,-.--` , \   _..---. /==/  /|=|  | ,-.' , -  `.   ,-.' , -  `. /==/- |\  \ 
|, \=/\=|- |==||==|-  _.-` .' .'.-. \|==|_ ||=|, |/==/_,  ,  - \ /==/_,  ,  - \|==|_ `/_ / 
|- |/ |/ , /==/|==|   `.-./==/- '=' /|==| ,|/=| _|==|   .=.     |==|   .=.     |==| ,   /  
 \, ,     _|==/==/_ ,    /|==|-,   ' |==|- `-' _ |==|_ : ;=:  - |==|_ : ;=:  - |==|-  .|   
 | -  -  , |==|==|    .-' |==|  .=. \|==|  _     |==| , '='     |==| , '='     |==| _ , \  
  \  ,  - /==/|==|_  ,`-._/==/- '=' ,|==|   .-. ,\\==\ -    ,_ / \==\ -    ,_ //==/  '\  | 
  |-  /\ /==/ /==/ ,     /==|   -   //==/, //=/  | '.='. -   .'   '.='. -   .' \==\ /\=\.' 
  `--`  `--`  `--`-----```-._`.___,' `--`-' `-`--`   `--`--''       `--`--''    `--`       
  
            { 1 } SPAM MODE             { 2 } NORMAL MODE             { 3 } EXIT
  """
print(header)


    

while True:
    tostart = input('\n@~~|> ')
    if tostart == "1":
        webhook = DiscordWebhook(url=input('url #-@-> '), username=input('username #-@-> '), avatar_url=input("avatar_url (optional) #-@-> "))
        embed = DiscordEmbed(
            title=input("title of embed #-@-> "),
            description=input("description #-@-> "),
            
        )
        timestamp = input('put timestamp (y/n) #-@-> ')
        if timestamp =='y':
            embed.set_timestamp()
            
            nbr = input('amount of messages @~~|> ')
            for i in range(int(nbr)):
                webhook.add_embed(embed)
                response = webhook.execute() 
            
        elif timestamp == 'n':
            nbr = input('amount of messages @~~|> ')
            for i in range(int(nbr)):
                webhook.add_embed(embed)
                response = webhook.execute() 
            
    elif tostart == "2":
        webhook = DiscordWebhook(url=input('url #-@-> '), username=input('username #-@-> '), avatar_url=input("avatar_url (optional) #-@-> "))
        embed = DiscordEmbed(
            title=input("title of embed #-@-> "),
            description=input("description #-@-> "),
            color=input('hexadecimal color #-@-> ')
        )
        timestamp = input('put timestamp (y/n) #-@-> ')
        if timestamp =='y':
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute() 
            
        elif timestamp == 'n':
            webhook.add_embed(embed)
            response = webhook.execute()

    elif tostart == '3':
        sys.exit()
