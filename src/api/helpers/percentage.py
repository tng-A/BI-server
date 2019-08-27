""" Percentage helper"""

def get_percentage(num, deno):
    """
    Calculate percentage and round to 2dpls
    num: numerator
    deno: denominator
    """

    try:
        percentage = round((num / deno) * 100, 2)
    except ZeroDivisionError:
        percentage = 0
    return percentage
