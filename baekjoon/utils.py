def _input_str(n, s):
    for _ in range(n):
        input_str = s.readline().strip()
        yield str(input_str)
