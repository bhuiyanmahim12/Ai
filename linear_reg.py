import numpy as np
import matplotlib.pyplot as plt

def linear_regression_fit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)
    
    # Calculate slope (m) and intercept (b)
    numerator = n * sum_xy - sum_x * sum_y
    denominator = n * sum_x_squared - (sum_x ** 2)
    m = numerator / denominator
    b = (sum_y - m * sum_x) / n
    
    return m, b

def predict(x, m, b):

    return m * x + b

def mean_squared_error(y_actual, y_predicted):

    n = len(y_actual)
    mse = np.sum((y_actual - y_predicted) ** 2) / n
    return mse

# Sample Dataset (Hours studied vs Exam Score)
# Independent variable (Feature)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Dependent variable (Target)
y = np.array([55, 60, 65, 70, 80, 75, 85, 90, 95, 100])

# Fit the linear regression model
slope, intercept = linear_regression_fit(x, y)
print(f"Slope (m): {slope:.2f}")
print(f"Intercept (b): {intercept:.2f}")
print(f"Regression line equation: y = {slope:.2f}x + {intercept:.2f}")

# Make predictions for all data points
y_predicted = predict(x, slope, intercept)

# Calculate and print Mean Squared Error
mse = mean_squared_error(y, y_predicted)
print(f"Mean Squared Error (MSE): {mse:.2f}")

# --- Visualization ---
plt.figure(figsize=(10, 6))
# Plot the actual data points
plt.scatter(x, y, color='blue', label='Actual Data', s=80)
# Plot the regression line
plt.plot(x, y_predicted, color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Simple Linear Regression: Hours Studied vs. Exam Score')
plt.legend()
plt.grid(True)
plt.show()

# Predict a new value
hours_studied = 7.5
predicted_score = predict(hours_studied, slope, intercept)
print(f"\nPredicted exam score for studying {hours_studied} hours: {predicted_score:.2f}")