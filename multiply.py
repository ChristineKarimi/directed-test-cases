# Question 2: Write a simple Python function that takes in 2 numbers and 
# returns their product(3 Marks).

def test_multiply(solution):
    try:
        # Test cases
        test_cases = [
            ((3, 4), 12),
            ((-2, 5), -10),
            ((0, 7), 0)
        ]
        
        # Initialize variables for partial marks distribution
        total_marks = 0
        obtained_marks = 0
        
        # Evaluate each test case
        for inputs, expected_output in test_cases:
            total_marks += 1
            if solution(*inputs) == expected_output:
                obtained_marks += 1
        
        # Calculate partial marks
        partial_marks = obtained_marks / total_marks
        
        return partial_marks
    
    except Exception as e:
        print("Error:", e)
        return 0.0  # No marks if an error occurs
