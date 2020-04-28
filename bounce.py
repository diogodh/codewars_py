def bouncingBall(h, bounce, window):

    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    result = 0
    while h > window:
        h = h * bounce
        result += 2

    return result - 1