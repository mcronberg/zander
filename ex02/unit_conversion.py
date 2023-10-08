def unit_conversion(feet, inches):
    # Convert foot to inches and add to the provided inches
    total_inches = (feet * 12) + inches

    # Convert the total inches to centimeters
    cm = total_inches * 2.54

    # Round to the nearest integer
    rounded_cm = int(cm)

    # Construct the result message
    result = f"{feet} ft {inches} in is equal to {rounded_cm} cm."

    return result

# Test the function
print(unit_conversion(7, 5))
