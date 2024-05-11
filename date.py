from datetime import datetime, timezone

today = datetime.now(timezone.utc)
formatted_date = today.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)