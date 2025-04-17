import discord
from discord.ext import commands, tasks
import random
import os
from dotenv import load_dotenv
import asyncio
from flask import Flask
from threading import Thread

# Load .env variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Replace with the actual channel ID where you want the daily facts sent
DAILY_FACT_CHANNEL_ID = 1362548069626941661

music_facts = [
    "Did you know? The world's longest song is 'The Rise and Fall of Bossanova' by PC III, lasting 13 hours!",
    "The Beatles hold the record for the most No. 1 hits on the Billboard Hot 100 chart.",
    "Music can help reduce stress by lowering cortisol levels, according to research.",
    "Beethoven continued composing music even after he went completely deaf.",
    "Did you know? The shortest song in the world is ‘You Suffer’ by Napalm Death, at just 1.316 seconds long!",
    "Mozart wrote more than 600 pieces of music in his lifetime, including symphonies, operas, and chamber music.",
    "In the 1970s, the first synthesizers were invented, revolutionizing the music industry.",
    "Music can boost your mood, reduce anxiety, and even improve cognitive performance.",
    "The first recorded instance of music being played on a piano was in 1700.",
    "Did you know? The iconic sound of the T-Rex roar in Jurassic Park was created using the sound of a guitar string being struck!",
    "J.S. Bach wrote some of his most famous compositions while in prison.",
    "The first music video played on MTV was 'Video Killed the Radio Star' by The Buggles.",
    "In 1984, Michael Jackson’s ‘Thriller’ became the first album to be certified for over 30 million copies sold.",
    "One of the most expensive records ever made was ‘Smiley Smile’ by The Beach Boys, which cost over $1 million.",
    "The first known use of musical notation dates back to 2000 BC in ancient Mesopotamia.",
    "Elvis Presley’s first recording was a song he made at Sun Studios for his mother’s birthday.",
    "The longest concert ever performed lasted 18 hours and 40 minutes, featuring multiple artists from all over the world.",
    "Did you know? Beethoven’s Symphony No. 9 was the first symphony to include voices.",
    "The world’s largest choir performed in the Philippines with over 8,000 members singing together.",
    "Before the electric guitar, musicians used acoustic guitars or even instruments like the lute for rock music.",
    "In 1990, the first-ever music download took place via the internet, with the song 'The Very First Time' being the test case.",
    "Did you know? Lady Gaga's stage name was inspired by Queen's hit song 'Radio Ga Ga.'",
    "The first Grammy Awards were held in 1959, and they’ve become one of the most prestigious honors in the music industry.",
    "The song 'Bohemian Rhapsody' by Queen had no verses and was a blend of opera, rock, and ballad.",
    "The longest recorded song title is 85 words long, and it is by a band called ‘The 100th Window.’",
    "Did you know? John Lennon’s middle name was Winston, named after Winston Churchill!",
    "The fastest recorded drum beat ever played reached 2,403 beats per minute, set by a German drummer named 'Hellhammer.'",
    "The first music store opened in 1824 in London and was known as the 'Pianoforte Warehouse.'",
    "Did you know? The first electronic music ever created was in the early 20th century by a Russian composer named Alexander Scriabin.",
    "The 'I Vow to Thee, My Country' is a popular piece of patriotic music that was written by Gustav Holst in 1918.",
    "One of the world’s largest organs is housed in the Boardwalk Hall in Atlantic City, USA, and it has 33,000 pipes!",
    "The ‘Air Guitar’ Championship is a real competition that began in Finland in 1996.",
    "Rock music came into being in the 1950s, but its roots trace back to the blues, jazz, and swing music of earlier decades.",
    "Did you know? The famous song 'Yesterday' by The Beatles was composed by Paul McCartney in a dream.",
    "There are over 1,000 different styles of dance, most of which were inspired by various music genres.",
    "Did you know? The longest-lasting music note ever played lasted for 35 minutes, set on a specially designed instrument.",
    "The 'Moonlight Sonata' by Beethoven was originally titled 'Sonata quasi una fantasia' (Sonata in the form of a fantasy).",
    "In the early 1900s, jazz was considered 'rebellious' and often banned from radio stations.",
    "A violin can have over 70 individual parts, and the wood is essential to creating its unique sound.",
    "In 2017, Spotify hit a new record of 50 million songs uploaded to its platform!",
    "Did you know? The world’s largest grand piano was built by a 15-year-old in New Zealand in 2009!",
    "Before it was called 'hip hop,' this genre was originally referred to as 'rap music.'",
    "There’s a music genre called 'Pirate Metal' that blends heavy metal with pirate themes and lore!",
    "Beyoncé has won the most Grammy Awards by a female artist, with 28 total wins.",
    "Jimi Hendrix was known for playing his guitar upside down because he was a left-handed player!",
    "Did you know? The loudest concert ever recorded took place in 1972 by The Who, reaching 126 decibels!",
]

song_recommendations = [
    "Blinding Lights - The Weeknd",
    "Heat Waves - Glass Animals",
    "Peaches - Justin Bieber",
    "Bad Habit - Steve Lacy",
    "Watermelon Sugar - Harry Styles",
    "Save Your Tears - The Weeknd",
    "Stay - The Kid LAROI & Justin Bieber",
    "Sunflower - Post Malone & Swae Lee",
    "Levitating - Dua Lipa",
    "Shivers - Ed Sheeran",
    "As It Was - Harry Styles",
    "Die For You - The Weeknd & Ariana Grande",
    "good 4 u - Olivia Rodrigo",
    "Late Night Talking - Harry Styles",
    "Unholy - Sam Smith & Kim Petras",
]

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')
    if not send_music_fact.is_running():
        send_music_fact.start()

@bot.command()
async def hello(ctx):
    await ctx.send("Yo, it's your boy Ryan! 🎤")

@bot.command()
async def recommend(ctx):
    song = random.choice(song_recommendations)
    await ctx.send(f"🎧 You might like: **{song}**")

@bot.command()
async def fact(ctx):
    fact = random.choice(music_facts)
    await ctx.send(f"🎶 Did you know? {fact}")

@tasks.loop(hours=24)
async def send_music_fact():
    await bot.wait_until_ready()
    channel = bot.get_channel(DAILY_FACT_CHANNEL_ID)
    if channel:
        fact = random.choice(music_facts)
        await channel.send(f"🎵 Daily Music Fact: {fact}")

# Optional keep_alive webserver (useful for Replit or Render.com)
app = Flask('')

@app.route('/')
def home():
    return "I'm alive, Ryan!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

keep_alive()

# Start bot
bot.run(os.getenv("TOKEN"))
