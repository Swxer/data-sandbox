import pandas as pd
import numpy as np

# sample_array = np.array([x for x in range(1, 6)])
sample_array = np.arange(1, 6)
print(f"Sample Array:\n{sample_array}\n")
print(f"Average: {np.average(sample_array)}")

# The size of list for each key in the dictionary should be the same to create a DataFrame.
# If the sizes are different, it will raise a ValueError.
d = {
    "Items": ["Apple", "Banana", "Orange", "Grapes", "Mango"],
    "Price": [100, 80, 90, 120, 150],
    "Quantity": [5, 10, 8, 6, 4],
}

df = pd.DataFrame(d)
print(f"DataFrame:\n{df}\n")
