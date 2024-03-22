def invertor(sec):

    hours = sec//3600   
    minutes = sec%3600
    minutes = minutes//60
    seconds = sec%60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

seconds = int(input('seconds ='))

invertor(seconds)