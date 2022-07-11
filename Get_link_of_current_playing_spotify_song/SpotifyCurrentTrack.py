import requests
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler

ENDPOINT_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
KEY = "HIDDEN " #key and toekn hidden for obvious reasons
Token = "HIDDEN"
updater = Updater("Token", use_context=True)

def playing(update: Update, context: CallbackContext):
    linkup = main()

    update.message.reply_text(
        f"{linkup}"
        )
    update.message.reply_text(
        f"This is your current playing track^^^^"
    )

updater.dispatcher.add_handler(CommandHandler('playing', playing))

updater.start_polling()


def get_currently_playing(access_tok):
    response = requests.get(
        ENDPOINT_URL,
        headers={
            "Authorization": f"Bearer {access_tok}"
        }
    )
    json_resp = response.json()
    link = json_resp['item']['external_urls']['spotify']
    track_link = {
        "link": link
    }
    return track_link

def main():
    playing_track_link = get_currently_playing(KEY)
    return playing_track_link.get("link")


