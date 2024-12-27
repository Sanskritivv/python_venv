import numpy as np
import matplotlib.pyplot as plt

# Generate a 5x5 random matrix with values between 0 and 1
random_matrix = np.random.rand(5, 5)

# Calculate the mean, sum, and transpose of the matrix
matrix_mean = np.mean(random_matrix)
matrix_sum = np.sum(random_matrix)
matrix_transpose = np.transpose(random_matrix)

# Normalize the matrix to have values between 0 and 1
normalized_matrix = (random_matrix - np.min(random_matrix)) / (np.max(random_matrix) - np.min(random_matrix))

# Display the original and normalized matrices
print("Original Matrix:")
print(random_matrix)
print("\nNormalized Matrix:")
print(normalized_matrix)

# Plot the matrices
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(random_matrix, cmap='viridis', interpolation='nearest')
axes[0].set_title("Original Matrix")

axes[1].imshow(normalized_matrix, cmap='plasma', interpolation='nearest')
axes[1].set_title("Normalized Matrix")

plt.tight_layout()
plt.show()
