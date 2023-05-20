from datetime import datetime, timedelta

data = (datetime.now() - timedelta(hours=3)).strftime('%d/%m/%Y %H:%M')



print(data)
