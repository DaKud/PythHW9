from logging import basicConfig

from datetime import datetime as dt

def calculator_fractions(data):
    time = dt.now().date
    with open('logger.csv', 'a') as file:
        file.write('')
