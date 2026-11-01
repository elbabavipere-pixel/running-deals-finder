python

import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

WELCOME = """
🏃 RUNNING DEALS FINDER

Bienvenue !

Je suis ton assistant de chasse aux bonnes affaires.

🔎 Marques surveillées :
• Nike
• Under Armour

👕 Catégories :
• Vestes et coupe-vent
• Leggings et pantalons
• Shorts de running

📏 Toutes les tailles
💰 Aucun budget maximum

Commandes disponibles :
/start - Accueil
/help - Aide
/status - État du bot
/criteres - Voir tes critères

La recherche automatique sera activée
lorsque la source d'annonces autorisée
sera configurée.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Utilise /start pour afficher le menu."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 Bot Telegram opérationnel.\n"
        "Recherche d'annonces : en attente de configuration."
    )

async def criteres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏷 Marques : Nike et Under Armour\n"
        "👕 Articles : vestes et bas de running\n"
        "📏 Tailles : toutes\n"
        "💰 Budget : illimité"
    )

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN manquant")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("criteres", criteres))

    print("Running Deals Finder démarre...")
    app.run_polling()

if __name__ == "__main__":
    main()
