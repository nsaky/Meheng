from datetime import datetime

def get_local_date():
    try:
        months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        current_year = datetime.today().strftime('%Y')
        current_month = int(datetime.today().strftime('%m').lstrip("0"))-1
        current_month= months[current_month]
        current_date = datetime.today().strftime('%d')
        statement=f"It's {current_date}th {current_month} {current_year} today."
        return statement
    except:
        return "Unable to get the date at the moment"