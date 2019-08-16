import random

def generate_random_color():
    return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
