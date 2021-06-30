import re


with open("django_success.log") as log_file:
    logfile = ''.join(log_file.readlines())
    hide_admin = re.sub(r'(?P<admin> \/admin\/)', ' /xxxxx/', logfile)
    with open("new_log.txt", 'w') as new_log:
        new_log.write(hide_admin)
    print(hide_admin)

with open("new_log.txt") as log_file:
    logfile = ''.join(log_file.readlines())
    hide_date = re.sub(r'(?P<date>\[\d{2}\/[\w]{3}\/\d{4} (\d{2}:){2}\d{2}])', '[XX/XXX/XXXX XX:XX:XX]', logfile)
    with open("new_log.txt", 'w') as new_log:
        new_log.write(hide_date)
    print(hide_date)

