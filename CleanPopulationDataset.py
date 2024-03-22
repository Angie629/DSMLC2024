import pandas as pd

# Load the Excel file
file_path = 'C:/Users/Angie/Downloads/population-and-demography.xlsx'
data = pd.read_excel(file_path)

# Clean and prepare the data (this part can vary based on what cleaning steps were taken)
cleaned_data = data[['country_name', 'year', 'population']]

# Group the data by 'year' and sum the 'population' for each year
yearly_population_sum = cleaned_data.groupby('year')['population'].sum().reset_index()

# Save the aggregated data to an Excel file
aggregated_file_path = 'C:/Users/Angie/Downloads/aggregated_population_by_year.xlsx'
yearly_population_sum.to_excel(aggregated_file_path, index=False)
