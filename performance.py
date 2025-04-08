import time

def measure_tokens_per_second(fn, *args, **kwargs):
    start = time.time()
    result = fn(*args, **kwargs)
    elapsed = time.time() - start
    tokens = sum(len(chunk['text'].split()) for chunk in args[0]) if args else 1
    tps = tokens / elapsed if elapsed > 0 else 0
    return result, tps
