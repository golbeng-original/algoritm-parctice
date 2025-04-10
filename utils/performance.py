import time

def timer(func):

    def wrapper(*args, **kwargs):
        

        start_time = time.time_ns()
        result = func(*args, **kwargs)
        end_time = (time.time_ns() - start_time) // 1000
        print(f"Execution time: {end_time} ms")
        return result
    
    return wrapper
