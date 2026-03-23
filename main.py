from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from rag.rag_pipeline import query_rag

# 🔹 Replace with your bot token
BOT_TOKEN = "8646544195:AAFVKiGW9yalZ7QzT4kUdEMN1nV9shzealQ"


# 🔹 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """👋 Hi! I'm your RAG assistant.

You can:
• Ask any question directly (no command needed)
• Example: What is RAG?

Commands:
• /help – Show help anytime
"""
)
#help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🤖 What I can do:

📚 Answer questions from your documents
Example:
• What is RAG?
• Explain machine learning

⚡ How to use:
• Just type your question
• Or: /ask your question

📌 Limitations:
• I only answer from uploaded documents
• If not found → I say "I don't know"

Type your question anytime 👍"""
    )

#ask command
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get query after /ask
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Please provide a query. Example:\n/ask What is RAG?")
        return

    try:
        response = query_rag(query)

        answer = response.get("answer", "")
        source = response.get("source", "")

        reply = f"""

📌 Answer:
{answer}

📄 Source:
{source}

"""
    except Exception as e:
        reply = "Something went wrong. Please try again."

    await update.message.reply_text(reply)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    logger.info(f"User query: {user_query}")

     # 🔹 Handle greetings here ALSO (important)
    if user_query.lower() in ["hi", "hello", "hey"]:
        await update.message.reply_text("Hi! Ask me anything from the documents 😊")
        print("MESSAGE RECEIVED:", update.message.text)
        return
    try:
        response = query_rag(user_query)

        answer = response["answer"]
        source = response["source"] if response["source"] else "No source found"

        reply = f"""
📌 Answer:
{answer}

📄 Source:
{source}
"""

    except Exception as e:
        logger.error(str(e))
        reply = "Something went wrong. Please try again."

    await update.message.reply_text(reply)

# 🔹 Handle user queries
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    logger.info(f"User query: {user_query}")

    try:
        response = query_rag(user_query)

        answer = response["answer"]
        source = response["source"] if response["source"] else "No source found"

        reply = f"""
📌 Answer:
{answer}

📄 Source:
{source}
"""

    except Exception as e:
        logger.error(str(e))
        reply = "Something went wrong. Please try again."

    await update.message.reply_text(reply)

# 🔹 Main app
def main():
    print("FILE STARTED")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ask", ask)) 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()