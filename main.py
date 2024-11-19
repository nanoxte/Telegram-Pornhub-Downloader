# Developer : POuria Hosseini | Telegram id : @isPoori | CHANNEL : @OmgaDeveloper #
import os
import requests
from bs4 import BeautifulSoup
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from threading import Thread
import yt_dlp

TOKEN = 'TOKEN' # Token

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! لینک جستجو یا ویدیو را بفرستید.")

def fetch_pornhub_video_url(search_url):
    try:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')

       
        video_tag = soup.find('a', {'class': 'phimage'})
        video_url = "https://www.pornhub.com" + video_tag['href']
        return video_url
    except Exception as e:
        return None

def download_video(url, chat_id, bot):
    try:
        
        ydl_opts = {
            'outtmpl': './videos/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = ydl.prepare_filename(info_dict)

        
        bot.send_video(chat_id=chat_id, video=open(video_title, 'rb'))
        os.remove(video_title)  # حذف فایل بعد از ارسال
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=f"خطایی رخ داد: {e}")

def handle_message(update: Update, context: CallbackContext):
    url = update.message.text.strip()
    chat_id = update.message.chat_id

    
    if "pornhub.com/video/search" in url:
        update.message.reply_text("در حال جستجو برای ویدیو، لطفاً منتظر بمانید...")
        video_url = fetch_pornhub_video_url(url)
        if video_url:
            url = video_url
        else:
            update.message.reply_text("خطا در یافتن ویدیو.")
            return

    
    update.message.reply_text("ویدیو در حال دانلود است. لطفاً کمی صبر کنید...")
    Thread(target=download_video, args=(url, chat_id, context.bot)).start()

def main():
    
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    
    if not os.path.exists('./videos'):
        os.makedirs('./videos')

    main()