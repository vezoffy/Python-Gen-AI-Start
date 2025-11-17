import numpy as np

test_scores = np.array([[80, 90, 85], [70, 78, 80], [56, 60, 42]])

pass_scores = test_scores >= 70
print(pass_scores)
print(test_scores[pass_scores])