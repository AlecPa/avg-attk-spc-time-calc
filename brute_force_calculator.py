'''
Created on Dec 3, 2020

@author: alecp
'''

pass_length = int(input('Enter password length: '))
possible_chars = int(input('Enter amount of possible characters in password: '))
possible_combos = possible_chars ** pass_length
print(f'Total possible combinations: {possible_combos:,}')
attempt_time = int(input('Enter time per attempt in nsec: '))
average_search_space = possible_combos / 2
total_time = (attempt_time * average_search_space)# what gets done in if statements / 1000000000 / 60 / 60 / 24 / 365
print(total_time)

# total_time is full time to attempt 50% of all possible combinations
# in nsec. There are 1,000,000,000 nsec in 1 sec. Checks for seconds,
# minutes, hours, days, and years and stores all
seconds = 0
minutes = 0
hours = 0
days = 0
years = 0

if total_time > 1000000000:
    seconds = total_time % 1000000000
    total_time = (total_time - seconds) / 1000000000
if total_time > 60:
    minutes = total_time % 60
    total_time = (total_time - minutes) / 60
if total_time > 60:
    hours = total_time % 60
    total_time = (total_time - hours) / 60
if total_time > 24:
    days = total_time % 24
    total_time = (total_time - days) / 24
if total_time > 365:
    years = total_time / 365

print(f'{years:.0f}years {days:.0f}days {hours:.0f}hours {minutes:.0f}minutes {seconds:.0f}seconds')









