from datetime import datetime, timedelta

format_dt = '%Y-%m-%d'



def date_range():
    result = []
    start_date = input("Enter start date in YYYY-MM-DD format: ")
    end_date = input("Enter end date in YYYY-MM-DD format: ")
    try:
        if start_date > end_date:
            return result
        else:
            start_dt = datetime.strptime(start_date, format_dt)
            end_dt = datetime.strptime(end_date, format_dt)
            while start_dt <= end_dt:

                result.append(datetime.strftime(start_dt, format_dt))
                start_dt += timedelta(days=1)

            return result
    except:
        return []


print(date_range())