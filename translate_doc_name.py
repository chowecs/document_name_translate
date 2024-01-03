from googletrans import Translator
import os

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest = target_lang)
    return translation.text

def translate_file_name(original_file_path, target_lang):
    file_name = os.path.basename(original_file_path)
    base_name, extension = os.path.splitext(file_name)
    translated_file_name = translate_text(base_name, target_lang)
    translated_file_name += extension
    translated_file_path = os.path.join(os.path.dirname(original_file_path), translated_file_name)
    os.rename(original_file_path, translated_file_path)
    return translated_file_path

translate_file_name('C:\\Users\\02008623\\Documents\\Python\\東京愛情故事.txt', 'en')