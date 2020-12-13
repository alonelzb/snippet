def retry(func):
    def wrapper(*args, **kwargs):
        i = 0
        while i < 3:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                i += 1
                print('retry', i, e)
            else:
                break
        return result

    return wrapper
