from datetime import datetime, timedelta
import random
def generate_random_date(start_date, end_date, inputFormat="%d-%m-%Y", outputFormat="%d-%m-%Y"):
    start_datetime = datetime.strptime(start_date,inputFormat )
    end_datetime = datetime.strptime(end_date, inputFormat)
    delta = end_datetime - start_datetime
    random_days = random.randint(0, delta.days)
    random_date = start_datetime + timedelta(days=random_days)
    return random_date.strftime(outputFormat)