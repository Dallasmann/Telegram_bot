import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import openai

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
telegram_token = os.getenv("TELEGRAM_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI API
openai.api_key = openai_key

# Define a function to respond to messages
def respond(update, context):
    # Get the user's message
    message = update.message.text
    
    # Generate a response using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"answer in a funny way to the following: {message}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    ).choices[0].text.strip()

     # Create an InlineKeyboardButton
    button = InlineKeyboardButton("Click me!", callback_data="button_clicked")

    # Create an InlineKeyboardMarkup with the button
    reply_markup = InlineKeyboardMarkup([[button]])
    
    # Send the response back to the user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response
    )

# Set up the main function to run the bot
def main():
    updater = Updater(telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, respond))
    updater.start_polling()
    updater.idle()

# Call the main function to run the bot
if __name__ == '__main__':
    main()


    # Append the AI's reply to the conversation
    conversation += f"AI: {reply}\n"

    # Store the updated conversation state
    conversation_state[chat_id] = conversation

    # Send the response back to the user
    context.bot.send_message(chat_id=chat_id, text=reply)

def main():
    # Create an instance of the Updater class
    updater = Updater(token=telegram_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a handler to handle incoming messages
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
