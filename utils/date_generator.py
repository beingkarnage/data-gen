from datetime import datetime, timedelta
from dateutil import parser
import random
def generate_random_date(start_date, end_date, input_format="%d-%m-%Y", output_format="%d-%m-%Y"):
    delta = parser.parse(end_date) - parser.parse(start_date)
    random_days = random.randint(0, delta.days)
    random_date = parser.parse(start_date) + timedelta(days=random_days)
    return random_date.strftime(output_format)