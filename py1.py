from langdetect import detect, DetectorFactory
import pyttsx3
engine = pyttsx3.init()
ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
engine.setProperty('rate',150)
engine.setProperty('volume', 1 )
voices = engine.getProperty('voices',ru_voice_id)
engine.say('я могу говорить')
detect_language = detect(text)
print(f'Язык текста: {detect_language}'
DetectorFactory.seed = 0
text = input("Введите текст: ")
detect_language = detect(text)
print(f'Язык текста: {detect_language}')