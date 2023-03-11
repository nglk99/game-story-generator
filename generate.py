import random

# Define lists of possible story elements
characters = ["hero", "villain", "ally", "mentor"]
goals = ["save the world", "protect a loved one", "seek revenge", "gain power"]
settings = ["medieval castle", "cyberpunk city", "alien planet", "underwater kingdom"]
obstacles = ["evil minions", "difficult puzzles", "natural disasters", "betrayal"]
twists = ["unexpected ally", "surprise betrayal", "sacrifice", "shocking reveal"]
cliches = ["chosen one", "prophecy", "magical artifact", "love triangle"]

# Define a function to generate a story based on keywords and avoiding cliches
def generate_story(char, goal, setting, obstacle, twist):
    story = ""
    # Determine if the story includes a cliche
    has_cliche = random.randint(0, 1)
    # Choose a character
    character = char
    # Choose a goal
    goal = goal
    # Choose a setting
    setting = setting
    # Choose an obstacle
    obstacle = obstacle
    # Choose a twist
    twist = twist
    # Avoid cliches if possible
    if has_cliche:
        # Remove cliched story elements
        if "chosen one" in goal:
            goal.remove("chosen one")
        if "prophecy" in setting:
            setting.remove("prophecy")
        if "magical artifact" in obstacle:
            obstacle.remove("magical artifact")
        if "love triangle" in twist:
            twist.remove("love triangle")
    # Generate the story
    story += f"Once upon a time, there was a {character} on a mission to {goal}. The journey took them to a {setting}, where they encountered {obstacle}. But just when things seemed hopeless, a {twist} turned the tide in their favor, and they emerged victorious. The end."
    return story

# Get input from the user for the story keywords
char_input = input("Enter a character ({}, {}, {}, {}): ".format(*characters))
goal_input = input("Enter a goal ({}, {}, {}, {}): ".format(*goals))
setting_input = input("Enter a setting ({}, {}, {}, {}): ".format(*settings))
obstacle_input = input("Enter an obstacle ({}, {}, {}, {}): ".format(*obstacles))
twist_input = input("Enter a twist ({}, {}, {}, {}): ".format(*twists))

# Convert input strings to lists
char = [x.strip() for x in char_input.split(',')]
goal = [x.strip() for x in goal_input.split(',')]
setting = [x.strip() for x in setting_input.split(',')]
obstacle = [x.strip() for x in obstacle_input.split(',')]
twist = [x.strip() for x in twist_input.split(',')]

# Generate the story based on the input
story = generate_story(char, goal, setting, obstacle, twist)

# Print the generated story
print(story)