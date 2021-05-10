# Performace-Test

1) Performance test — Pure Python [pure_python_test.py]
    Here’s a list of tasks performed in this benchmark: 

      1) Create a list l containing 100,000,000 random integers between 100 and 999
      2) Square every item in l
      3) Take a square root of every item in l
      4) Multiply corresponding squares and square roots
      5) Divide corresponding squares and square roots
      6) Perform an integer division of corresponding squares and square roots
    
    The test was made only with built-in Python libraries, so Numpy wasn’t allowed.
    
    
2) Performance test — Numpy [numpy_test.py]
    Here’s a list of tasks performed in this benchmark:
      
      1) Matrix multiplication
      2) Vector multiplication
      3) Singular Value Decomposition
      4) Cholesky Decomposition
      5) Eigendecomposition
      
    The original benchmark script was taken from Markus Beuckelmann on Github, and modified slightly, so both start and end time is captured.
    
    
3) Performance test — Pandas [pandas_test.py]     
    Here’s a list of tasks:
      
      1) Create an empty data frame
      2) Assign it a column (X) of 100,000,000 random integers between 100 and 999
      3) Square every item in X
      4) Take a square root of every item in X
      5) Multiply corresponding squares and square roots
      6) Divide corresponding squares and square roots
      7) Perform an integer division of corresponding squares and square roots
      
4) Performance test — Scikit-Learn [sklearn_test.py]
    Here’s a list of tasks performed in the benchmark:
    
      1) Get the dataset from the web
      2) Perform a train/test split
      3) Declare a Decision tree model and find optimal hyperparameters (2400 combinations + 5-fold cross-validation)
      4) Fit a model with optimal parameters
      
    It’s a more or less standard model training procedure, disregarding testing out multiple algorithms, data preparation, and feature engineering.
      
      
