from cabrillo.parser import parse_log_file

cab = parse_log_file('logs/DL5XL.log')
# cab = parse_log_file('logs/PA7F.log')

print(cab.callsign)

print(cab.qso)

print(cab.text())
