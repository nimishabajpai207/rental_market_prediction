import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker and set up variables
fake = Faker()
counties = ['Alameda', 'Contra Costa', 'Marin', 'Napa', 'San Francisco', 'San Mateo', 'Santa Clara', 'Solano', 'Sonoma']
num_records = 20000

# Create a list of sample data
data = []
for _ in range(num_records):
    record = {
        'Property_ID': fake.uuid4(),
        'County': np.random.choice(counties),
        'Address': fake.address().replace('\n', ', '),
        'Zip_Code': fake.zipcode(),
        'Crime_Rate': round(np.random.uniform(2.0, 5.0), 1),
        'Bedrooms': np.random.randint(1, 5),
        'Bathrooms': np.random.randint(1, 4),
        'Walkability_Score': np.random.randint(60, 100),
        'Floor': np.random.randint(1, 5),
        'New_Construction': np.random.choice([True, False]),
        'Renovated': np.random.choice([True, False]),
        'Washer_Dryer': np.random.choice([True, False]),
        'Trash_Service': np.random.choice(['INCLUDED', 'NOT_INCLUDED']),
        'Average_Rent': f"${np.random.randint(2000, 4000)}"
    }
    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('bay_area_rentals_sample.csv', index=False)
