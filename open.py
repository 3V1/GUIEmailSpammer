import time
import smtplib
import random

from dearpygui import core
from dearpygui.core import *
from dearpygui.simple import *
from multiprocessing import Process
from multiprocessing import *


def append_logged_info(sender_address, time):
    rgb = [random.choice(range(0, 255)), random.choice(
        range(0, 255)), random.choice(range(0, 255)), 255]
    core.add_text(f'Sent Email To {sender_address}',
                  parent='Logs Window', color=rgb)
    core.add_text(f'Took {time} To Execute', parent='Time Window', color=rgb)


def send_server_email(sender_address, account_password, subject, body, receiver_address):
    for i in range(0, core.get_value('Ammount Of Emails To Send')):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            begin = time.time()
            smtp_server.login(sender_address, account_password)
            message = f"Subject: {subject}\n\n{body}"
            smtp_server.sendmail(sender_address, receiver_address, message)
            end = time.time()
            append_logged_info(receiver_address, f'{end-begin}')


def start_main():
    with window('EMail Window'):
        core.add_text('Soy Email Client')
        core.add_input_text('Your Email')
        core.add_input_text('Your Email Password', password=True)
        core.add_input_text('Email Reciever')
        core.add_input_text('Email Subject')
        core.add_input_text('Email Body')
        core.add_slider_int('Ammount Of Emails To Send')
        core.add_button('Send Emails', parent='EMail Window', callback=lambda: send_server_email(f"{core.get_value('Your Email')}",
                                                                                                 f"{core.get_value('Your Email Password')}", f"{core.get_value('Email Subject')}",
                                                                                                 f"{core.get_value('Email Body')}", f"{core.get_value('Email Reciever')}"))
        set_main_window_size(1000, 500)
        core.add_separator(name='Separator', parent='EMail Window')
        end()
        with window('Logs Window', width=350, height=300):
            add_dummy()
        with window('Time Window', width=350, height=300):
            add_dummy()
    start_dearpygui(primary_window='EMail Window')

add_additional_font('uni-sans.heavy-caps.otf')
set_theme("Cherry")

if __name__ == '__main__':
    main_process = Process(target=start_main)
    main_process.start()
    main_process.join()
