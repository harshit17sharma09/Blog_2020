# Code for counting word in a article adn general read time

import datetime
import re 
import math

from django.utils.html import strip_tags


#function fro counting words

def count_words(string):
    # html_string = """ <h1> This is a title </h1> """
    word_string = strip_tags(string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_read_time(string): 
    count = count_words(string)
    read_time_min = math.ceil(count/200)  # assuming 200 wpm
    # read_time_sec = read_time_min * 60
    # read_time = str(datetime.timedelta(minutes=read_time_min))
    return int(read_time_min)