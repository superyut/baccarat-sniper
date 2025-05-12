def check_pattern_memory(results):
    pattern_window = 6
    if len(results) < pattern_window * 2:
        return None
    latest = results[-pattern_window:]
    for i in range(len(results) - pattern_window * 2):
        if results[i:i + pattern_window] == latest:
            return i
    return None