import numpy as np
import pandas as pd
income = np.array([10000, 12000, 15000, 13000, 16000, 18000, 20000, 22000, 25000, 27000])
income_without_tax = income * 0.7
expenses = np.array([4000, 6000, 8000, 2000, 7000, 3000, 7000, 5000, 8000, 9000])
df = pd.DataFrame({
    'Income without tax':income_without_tax, 
    'Expenses':expenses}, 
    index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'
])
print("Full DataFrame:")
print(df)
print("\nFirst quarter data:")
print(df.iloc[:3])