
def is_started(date):
    from datetime import datetime
    
    now = datetime.now().date()
    return now >= date