#import module dasar
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from pprint import pprint

#import library untuk konfigurasi
from dotenv import dotenv_values

env = dotenv_values(".env")
bot_token = env['BOT_TOKEN']

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"terdapat pesan yang masuk ke handler start.\nIsinya adalah :\n{update.message.text}")
    print("_"*40)
    await context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text="Halo, selamat datang di bot saya :)"
    )

async def hitung(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"terdapat pesan yang masuk ke handler hitung.\nIsinya adalah :\n{update.message.text}")
    print("_"*40)

    pprint(update.to_dict())

    list_angka = update.message.text.split()[1]
    list_angka = eval(list_angka)
    result = sum(list_angka)

    await context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Hasil dari penjumlah pada list {list_angka} adalah {result}"
    )

if __name__ == "__main__":
    #membuat objek aplikasi
    application = Application.builder().token(bot_token).build()

    #membuat objek start handler
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #membuat objek hitung handler
    hitung_handler = CommandHandler('hitung', hitung)
    application.add_handler(hitung_handler)

    print("aplikasi berjalan")

    #menjalankan aplikasi secara streaming
    application.run_polling()


