def detect_support_resistance(momentum):
    highs, lows = [], []
    for i in range(2, len(momentum)-2):
        if momentum[i] > momentum[i-1] and momentum[i] > momentum[i+1]:
            highs.append((i, momentum[i]))
        if momentum[i] < momentum[i-1] and momentum[i] < momentum[i+1]:
            lows.append((i, momentum[i]))
    return highs, lows