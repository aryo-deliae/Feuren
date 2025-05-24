import discord
import os
from dotenv import load_dotenv
import json
from discord.ext import commands
from discord import Intents, app_commands
from keep_alive import keep_alive

load_dotenv()
key_bot = os.getenv('DISCORDQUOIQUARBITRE_KEY')

intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)



racine = (os.getcwd())
chemin = os.path.join(racine, "score.json")

@bot.event
async def on_ready():
    print(f'Je me suis bien connecté en tant que {bot.user}')


@bot.event
async def on_message(message):

    if str(message.author.name) == "Coiffeur":
        oh = message.mentions

        with open(chemin, 'r', encoding='utf-8') as f:
            dota = json.load(f)

        for i in oh:
            for j in dota:

                if str(i) == j["id"]:
                    up = int(j["score"])
                    up += 1
                    j["score"] = up

        with open( chemin, 'w', encoding='utf-8') as f:
                        json.dump(dota, f, ensure_ascii=False, indent=2)

    if message.content == "!score":
        with open(chemin, 'r', encoding='utf-8') as f:
            dota = json.load(f)

        ordo = 0
        ordre = []
        nom_ordonné = []
        dict_ordonné = {}

        for i in dota:
            ordre.append(i["score"])
            ordre.sort(reverse = True)


        def anti_doublon(dicto, liste):
            resultat = False
            for i in liste :
                if i == dicto :
                    resultat = True 
            return resultat 

        for j in ordre :
            for i in dota : 
                if i["score"] == j and anti_doublon(i["nom"], nom_ordonné) is False :
                    nom_ordonné.append(i["nom"])

        for i in nom_ordonné :
            dict_ordonné.update({f"{i}" : ordre[ordo]})
            ordo += 1


        joi = ""

        for i in dict_ordonné :
            count = 0
            for lettre in i : 
                count += 1

            espace = 12
            aspace = espace - count
            ospace = " "*aspace

            joi += f"{i}{ospace}: {dict_ordonné[i]}\n"

        joi = f"```\n{joi}```"
        await message.channel.send(joi)

keep_alive()
bot.run(key_bot)