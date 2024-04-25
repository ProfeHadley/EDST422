import random


def generate_motivational_quote():
    quotes = [
        "We are more alike, my friends, than we are unalike. - Maya Angelou",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Injustice anywhere is a threat to justice everywhere. - Martin Luther King Jr.",
        "The most common way people give up their power is by thinking they don't have any. - Alice Walker",
        "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. - Maya Angelou",
        "We all have dreams. But in order to make dreams come into reality, it takes an awful lot of determination, dedication, self-discipline, and effort. - Jesse Owens",
        "Success is not about how much money you make, it's about the difference you make in people's lives. - Michelle Obama"
    ]
    return random.choice(quotes)

# Generate and display a motivational quote
print("Here's your motivational quote for today:")
print(generate_motivational_quote())
