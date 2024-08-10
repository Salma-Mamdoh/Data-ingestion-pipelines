import time
import random
import os

def write_log_entry(filename, message):
    with open(filename, 'a') as file:
        file.write('{},{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), message))

def generate_log_entry(filename):
    log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
    log_level = random.choice(log_levels)
    message = 'This is a {} message. Process ID: {}'.format(log_level, os.getpid())
    write_log_entry(filename, message)

num_entries = 100
filename = 'log.txt'
for _ in range(num_entries):
    generate_log_entry(filename)
    time.sleep(1)
