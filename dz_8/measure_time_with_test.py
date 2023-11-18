import time
import unittest


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time} seconds to execute")
        return result
    return wrapper


@timing_decorator
def some_function():
    result = 0
    for i in range(1000):
        result += i
    return result


class TestMeasureTimeFunction(unittest.TestCase):
    def test_measure_time(self):
        decorated_function = timing_decorator(some_function)
        measured_result = decorated_function()
        self.assertIsInstance(measured_result, int)


if __name__ == "__main__":
    unittest.main()
