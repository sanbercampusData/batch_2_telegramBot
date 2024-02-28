from telethon import TelegramClient, events

#import library untuk konfigurasi
from dotenv import dotenv_values

from src import process

env = dotenv_values(".env")
bot = TelegramClient("test", env['API_ID'], env['API_HASH']).start(bot_token=env['BOT_TOKEN'])

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    '''send message when the command /start is issued.'''
    await event.reply('Halo, selamat datang di bot saya, versi telethon')

@bot.on(events.NewMessage(pattern='/echo'))
async def echo(event):
    '''send message when the command /echo is issued.'''
    print(event.date, event.peer_id)
    await event.respond(event.text)

@bot.on(events.NewMessage(pattern='/hitung'))
async def hitung(event):
    '''send message when the command /hitung is issued.'''

    list_angka = event.text.split()[1]
    list_angka = eval(list_angka)
    result = sum(list_angka)
    
    await event.respond(f"Hasil dari penjumlah pada list {list_angka} adalah {result}")

@bot.on(events.NewMessage(pattern='#sanbercampusBertanya'))
async def sambercampus_bertanya(event):
    '''answering the question from dataset.'''

    data = event.text.split()
    data.pop(0)
    data = ' '.join(data)
    result = process.search_services(data, env)

    await event.respond(f"{result}")

#endppoint yang digunakan untuk meminta pada program untuk melakukan pelatihan model machine learning
@bot.on(events.NewMessage(pattern='#latih_model'))
async def latih_model(event):
    '''training NLP Sentiment model'''

    data = event.text.split()
    data.pop(0)
    data = ' '.join(data)
    result = process.train_model(env)

    await event.respond(f"{result}")

@bot.on(events.NewMessage(pattern='#prediksi_sentiment'))
async def prediksi(event):
    '''training NLP Sentiment model'''

    data = event.text.split()
    data.pop(0)
    data = ' '.join(data)
    result = process.prediksi_sentiment(env, data)

    await event.respond(f"{result}")



def run():
    '''start the bot'''
    print("aplikasi telethon berjalan")
    bot.run_until_disconnected()
