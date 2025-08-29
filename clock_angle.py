"""
Clock Angle Practice Generator
------------------------------
This program generates random math problems about the angle between the
hour and minute hands of a clock. It also includes an optional function
to draw a clock diagram with matplotlib.
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def random_clock_problem():
    """
    Generate a random time, create a question, and calculate the angle.
    Returns:
        (question: str, angle: int, hour: int, minute: int, period: str)
    """
    # Randomly pick hour, minute, and AM/PM
    hour = random.randint(1, 12)
    minute = random.randint(0, 59)
    period = random.choice(["a.m.", "p.m."])

    # Compute the angle
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6
    diff = abs(hour_angle - minute_angle)
    angle = int(min(diff, 360 - diff))

    # Format time
    time_str = f"{hour}:{minute:02d} {period}"

    # Question templates
    templates = [
        "What is the angle between the hour and minute hands at {time}?",
        "Find the angle made by the clock hands when the time is {time}.",
        "At {time}, what angle separates the hour hand and the minute hand?",
        "When the clock reads {time}, what is the angle between the hands?",
        "How many degrees separate the hands of a clock at {time}?"
    ]

    # Pick a variation
    template = random.choice(templates)
    question = template.format(time=time_str)

    return question, angle, hour, minute, period


def draw_clock(hour, minute):
    """
    Draw a simple clock diagram with given hour and minute.
    The hour hand is black, the minute hand is red.
    """
    fig, ax = plt.subplots(figsize=(5, 5))

    # Draw clock circle
    circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)
    ax.add_artist(circle)

    # Mark hours
    for h in range(12):
        angle = np.deg2rad(90 - h * 30)
        x = 0.9 * np.cos(angle)
        y = 0.9 * np.sin(angle)
        ax.text(x, y, str(h if h != 0 else 12), ha="center", va="center", fontsize=12, weight="bold")

    # Hour hand
    hour_angle = np.deg2rad(90 - (hour % 12) * 30 - minute * 0.5)
    ax.plot([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)], linewidth=4, color="black")

    # Minute hand
    minute_angle = np.deg2rad(90 - minute * 6)
    ax.plot([0, 0.8 * np.cos(minute_angle)], [0, 0.8 * np.sin(minute_angle)], linewidth=2, color="red")

    # Center dot
    ax.plot(0, 0, 'o', color="black")

    # Formatting
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    print("🕒 Clock Angle Practice Questions\n")
    for i in range(1, 6):  # change 6 to 11 if you want 10 questions
        question, answer, hour, minute, period = random_clock_problem()
        print(f"Q{i}: {question}")
        print(f"   Answer: {answer}°\n")

        # Uncomment this line if you want to show a clock diagram for each question
        # draw_clock(hour, minute)
