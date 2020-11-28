# PARSE TIME FUNCTION | PARSE TIME INTO "00:00:00" FORMAT | ISAAC KOGAN

def parse_time(seconds):
    """
    :param seconds: The amount of seconds passed (can be float, int)
    :return: Returns the formatted time in HH:MM:SS
    """
    seconds = seconds % (24 * 3600)     # Getting Days
    hour = seconds // 3600              # Creating Hours
    seconds %= 3600                     # Getting Minutes
    minutes = seconds // 60             # Creating Minutes
    seconds %= 60                       # Getting Seconds

    return "%d:%02d:%02d" % (hour, minutes, seconds)        # Returning the values
