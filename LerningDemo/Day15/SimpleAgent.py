def recommend_clothing(temperature):
    """Recommends clothing based on temperature."""
    if temperature > 25:  # Celsius
        return "Wear shorts and a t-shirt."
    elif temperature > 15:
        return "Wear jeans and a light jacket."
    elif temperature > 5:
        return "Wear a sweater and a jacket."
    else:
        return "Wear a heavy coat, gloves, and a hat."

# Example usage:
temperature = 18
recommendation = recommend_clothing(temperature)
print(f"The temperature is {temperature} degrees Celsius.  I recommend: {recommendation}")