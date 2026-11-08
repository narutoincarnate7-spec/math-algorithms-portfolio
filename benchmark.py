import time
from windowed_exponentiation import fixed_window_mod_exp

def benchmark():
    # Use a large 2048-bit exponent (standard for RSA)
    base = 65537
    modulus = 2**2048 - 1  # A large prime-like modulus
    exponent = 2**2048 - 1

    # Benchmark Python's built-in pow
    start = time.perf_counter()
    result_pow = pow(base, exponent, modulus)
    time_pow = time.perf_counter() - start

    # Benchmark our fixed-window implementation
    start = time.perf_counter()
    result_window = fixed_window_mod_exp(base, exponent, modulus, window_size=4)
    time_window = time.perf_counter() - start

    # Verify correctness
    assert result_pow == result_window, "Results do not match!"

    print(f"Python pow():        {time_pow:.6f} seconds")
    print(f"Fixed-window (w=4):  {time_window:.6f} seconds")
    print(f"Speedup vs built-in: {time_pow / time_window:.2f}x")
    print("Results are correct and identical.")

if __name__ == "__main__":
    benchmark()
