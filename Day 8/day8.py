import logging

# Configure the logging level of module
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

# Prompt the user for logging level and message
level_name = input("Enter the logging level name accepted levels are (DEBUG, INFO, WARNING, ERROR, CRITICAL) as they are case-sensitive: ")
message = input("Enter the message to log: ")

# Validate the logging level name
valid_levels = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING,
               'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}

if level_name not in valid_levels:
    print("Invalid logging level name. Please try again.")
    exit()

# Get the logging level based on the validated name
level = valid_levels[level_name]

# Log the message with the specified level
logging.log(level, message)