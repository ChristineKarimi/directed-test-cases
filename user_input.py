# Question 3: Write a Python function that displays a prompt asking 
# for the user's age and captures the input(5 Marks).

def test_get_user_age(solution):
    try:
        from io import StringIO
        import sys
        
        # Prepare mock input
        mock_input = "25\n"
        
        # Redirect stdin and stdout
        sys.stdin = StringIO(mock_input)
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute student's solution
        age = solution()
        
        # Reset stdin and stdout
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        
        # Check if input is captured correctly
        if age == "25":
            return 1.0  # Full marks if input is correct
        else:
            return 0.5  # Partial marks if input is incorrect
    
    except Exception as e:
        print("Error:", e)
        return 0.0  # No marks if an error occurs
