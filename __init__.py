from datetime import datetime

def current_datetime_string_generator():
 datetimee = datetime.now()
 print("datetime is: " + datetimee.__str__())
 datetimeeText = datetimee.strftime("%d-%m-%Y %H%M%S.%f")
 datetimeeTextString = datetimeeText.__str__()
 print("datetimeText is: " + datetimeeTextString)
 return datetimeeTextString

current_datetime_string_generator()