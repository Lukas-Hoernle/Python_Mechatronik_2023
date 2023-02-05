import random, time

def any(*strategies):
    """
    Kombination aus mehreren Strategien, zum Beispiel:
    
        any(fixedInterval(5), onObstacle(vehicle, 0.8))
    
    Ein Richtungswechsel findet immer statt, wenn einer der übergebenen
    Strategien ihn auslöst.
    """
    while True:
        for strategy in strategies:
            try:
                change = strategy.__next__()
            except:
                pass

            if change:
                break
        
        yield change

def fixedInterval(seconds):
    """
    Richtungswechsel nach festem Zeitintervall.
    """
    prev_time = 0

    while True:
        curr_time = time.monotonic()

        if (curr_time - prev_time) >= seconds:
            yield True
        else:
            yield False

def randomInterval(min_seconds, max_seconds):
    """
    Richtungswechsel nach zufälligem Zeitintervall.
    """
    prev_time = 0
    seconds = random.randint(min_seconds, max_seconds)

    while True:
        curr_time = time.monotonic()

        if (curr_time - prev_time) >= seconds:
            seconds = random.randrange(min_seconds, max_seconds)
            yield True
        else:
            yield False

def onObstacle(vehicle, max_pushback):
    """
    Richtungswechsel bei Hinderniss.
    """
    yield True

    while True:
        if vehicle.speed_total >= 0 and vehicle.obstacle_pushback >= max_pushback:
            yield True
        if vehicle.speed_total < 0 and vehicle.obstacle_pushback <= max_pushback * -1:
            yield True
        else:
            yield False
