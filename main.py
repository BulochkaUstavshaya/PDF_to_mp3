from gtts import gTTS
from PyPDF2 import PdfReader
import gtts.lang
import os.path
import argparse


def pdf_to_mp3(language: str, path_pdf: str):
    try:
        with open(path_pdf, 'rb') as pdf_file:
            print('[INFO] Converting...')

            pdf_read = PdfReader(pdf_file)
            text = '\n'.join([page.extract_text() for page in pdf_read.pages])
            mp3 = gTTS(text, lang=language)
            name = os.path.basename(path_pdf).split('.')[0]
            mp3.save(f'{name}.mp3')

            print('[INFO] Complete!')
    except Exception as e:
        print(f'[ERROR]\n{e}')


def is_valid_terminal_data(language: str, path_pdf: str) -> bool:
    if not os.path.exists(path_pdf):
        print('[ERROR] Invalid file path!')
        return False

    if path_pdf[-4:] != '.pdf':
        print('[ERROR] Must be a pdf!')
        return False

    if language not in gtts.lang.tts_langs().keys():
        print('[ERROR] Incorrect language!')
        return False

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('language', help='language in pdf file (ru, en...)', type=str)
    parser.add_argument('path', help='path to file', type=str)
    args = parser.parse_args()

    if is_valid_terminal_data(args.language, args.path):
        pdf_to_mp3(args.language, args.path)


if __name__ == '__main__':
    main()