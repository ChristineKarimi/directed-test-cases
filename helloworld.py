# Question 1: Write a simple Python function that prints 'hello world'(2 Marks).

def test_hello_world(solution):
    try:
        import sys
        from io import StringIO
        
        # Redirect stdout to StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute student's solution
        solution()
        
        # Get the value of printed output
        output = captured_output.getvalue().strip()
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Check if output is correct
        if output == "Hello World":
            return 1.0  # Full marks if output is correct
        else:
            return 0.5  # Partial marks if output is incorrect
        
    except Exception as e:
        print("Error:", e)
        return 0.0  # No marks if an error occurs
