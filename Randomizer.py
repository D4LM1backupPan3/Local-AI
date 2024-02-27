def randomizer():
    import random
    import time
    from LocalAI import greetings
    GreetingTemp = random.choice(greetings)
    time.sleep(5)
    randomizer()