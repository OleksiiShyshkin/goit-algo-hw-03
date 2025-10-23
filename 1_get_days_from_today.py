from datetime import datetime

def get_days_from_today(date_input):
    try:
        input_date = datetime.strptime(date_input, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        date_difference = input_date - current_date
        return date_difference.days
    except ValueError:
        return 'Invalid date format. Use "YYYY-MM-DD".'
