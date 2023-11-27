def add_time(start, duration):
    new_time=0
    n=0
    x=start.split(":")
    hour_start=int(x[0])
    mi=x[2]
    min=mi.split(" ")
    minute_start=int(min[0])
    time_indication=min[2]
    y=duration.split(":")

    hour=int(y[0])
    minutes=int(y[1])
    new_minute=minute_start+minutes
    if (new_minute >= 60):
        new_hour=new_hour+1
        new-minute=new_minute % 60
    if (new_minute < 9) :
        new_m='0' + str(new_minute)
    new_hour=hour_start+hour
    
    if (new_hour > 12 and time_indication=="PM"):
        new_hour=newhour-12 
        time_indication="AM"
        n=n+1
    
    
    
    
    

    
    





    return new_time
