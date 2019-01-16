# Import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

physical_sciences = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
print(physical_sciences.head())
physical_sciences.year
# Plot in blue the % of degrees awarded to women in the Physical Sciences
#plt.plot(year, physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
#plt.plot(year, computer_science , color='red')

# Display the plot
# plt.show()
