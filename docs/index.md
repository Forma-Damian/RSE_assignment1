# Taylor Expansion Project

Welcome to the documentation! This project uses Numba to calculate Taylor series expansions quickly.

## Usage
```python
from hello_numba.taylor_expansion import taylor_expansion_sin

# Calculate sin(0.5) using 5 terms
result = taylor_expansion_sin(0.5, 5)
print(result)