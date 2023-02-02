import random, time

def fixedInterval(seconds):
    """
    Richtungswechsel nach festem Zeitintervall.
    """
    prev_time = 0

    while True
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

    while True
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
    while True
        if vehicle.obstacle_pushback >= max_pushback:
            yield True
        else:
            yield False