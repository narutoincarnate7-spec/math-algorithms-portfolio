def fixed_window_mod_exp(base, exponent, modulus, window_size=4):
    """
    Computes (base ** exponent) % modulus using fixed-window exponentiation.
    Processes the exponent in blocks of `window_size` bits.
    """
    if modulus == 1:
        return 0

    # 1. Precompute table of base^0, base^1, ..., base^(2^w - 1) mod modulus
    # This is the "precomputation" phase. It uses 2^w - 2 multiplications.
    table = [1] * (1 << window_size)
    table[1] = base % modulus
    for i in range(2, (1 << window_size)):
        table[i] = (table[i - 1] * base) % modulus

    # 2. Convert exponent to binary and process in windows
    # We use binary string for simplicity to align with the mathematical explanation
    bin_exp = bin(exponent)[2:]  # Convert to binary, remove '0b'
    result = 1

    # Pad the binary string to a multiple of window_size (left-pad with zeros)
    padding = (window_size - (len(bin_exp) % window_size)) % window_size
    bin_exp = '0' * padding + bin_exp

    # 3. Main loop: Square for each window, then multiply by table value
    # The number of squarings is the bit-length, and multiplications are reduced.
    for i in range(0, len(bin_exp), window_size):
        window_bits = bin_exp[i:i + window_size]
        window_value = int(window_bits, 2)

        # Square the result `window_size` times
        for _ in range(window_size):
            result = (result * result) % modulus

        # Multiply by the precomputed value for this window
        result = (result * table[window_value]) % modulus

    return result

# Example usage: (3^200) mod 50
if __name__ == "__main__":
    print(fixed_window_mod_exp(3, 200, 50, window_size=4))  # Should output 1
