import os
import telebot
from telebot import types
import pandas as pd
import natsort
from TOKEN import TOKEN

TOKEN = TOKEN

IMAGE_FOLDER = 'test_images'
bot = telebot.TeleBot(TOKEN)
image_files = []
current_image_index = 0

df = pd.DataFrame(columns=['Filename', 'Result'])



def send_current_image(chat_id):
    if current_image_index < len(image_files):
        image_path = os.path.join(IMAGE_FOLDER, image_files[current_image_index])
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, 'No more images.')



@bot.message_handler(commands=['start'])
def handle_start(message):
    global current_image_index
    current_image_index = 0
    send_current_image(message.chat.id)
    send_keyboard(message.chat.id)



@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    global current_image_index

    if message.text == "❤️":
        reaction = 1
    elif message.text == "👎":
        reaction = 0
    elif message.text == "ОТПРАВИТЬ РЕЗУЛЬТАТ":
        df.to_csv(f"train_result_{message.chat.id}.csv", index=False)
        bot.send_message(message.chat.id, 'Молодец! Ты отправил результаты.')
    else:
        bot.send_message(message.chat.id, 'Команды не существует. Нажимай на кнопки или отправляй результат, если готов.')
        return

    if current_image_index < len(image_files):
        filename = image_files[current_image_index]
        df.loc[current_image_index] = [filename, reaction]

    current_image_index += 1
    send_current_image(message.chat.id)
    send_keyboard(message.chat.id)



def send_keyboard(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    heart_button = types.KeyboardButton("❤️")
    dislike_button = types.KeyboardButton("👎")
    markup.add(heart_button, dislike_button)
    if current_image_index < len(image_files):
        bot.send_message(chat_id, f'Изображение: {current_image_index+1}/{len(image_files)}', reply_markup=markup)



if __name__ == '__main__':
    image_files = natsort.natsorted([f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    bot.polling(none_stop=True)
