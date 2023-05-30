from datetime import datetime, timedelta
import random
def generate_random_date(start_date, end_date, input_format="%d-%m-%Y", output_format="%d-%m-%Y"):
    start_datetime = datetime.strptime(start_date,input_format )
    end_datetime = datetime.strptime(end_date, input_format)
    delta = end_datetime - start_datetime
    random_days = random.randint(0, delta.days)
    random_date = start_datetime + timedelta(days=random_days)
    return random_date.strftime(output_format)