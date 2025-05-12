def generate_bet_signal(momentum, highs, lows):
    if len(momentum) < 3:
        return "WAIT"
    current = momentum[-1]
    prev = momentum[-2]
    for i, val in highs[-3:]:
        if abs(i - len(momentum) + 1) <= 2 and current < val and prev >= val:
            return "BET BANKER"
    for i, val in lows[-3:]:
        if abs(i - len(momentum) + 1) <= 2 and current > val and prev <= val:
            return "BET PLAYER"
    return "WAIT"