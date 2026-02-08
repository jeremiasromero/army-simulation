# Army Simulation

This project is a modeling exercise that simulates armies belonging to different
civilizations. Each army is composed of military units that can be trained,
transformed, and used in battles against other armies.

The main goal of the exercise is to correctly represent the problem domain
using object-oriented design.

## Problem Description

Armies belong to a civilization and start with a predefined number of units:
Pikemen, Archers, and Knights. Multiple armies of the same civilization can
coexist.

Each army starts with:
- A set of initial units depending on its civilization
- 1000 gold coins
- A battle history recording all battles fought

### Units

There are three types of units:
- Pikeman (5 strength)
- Archer (10 strength)
- Knight (20 strength)

Each unit has an age and a strength value.

### Training

Units can be trained to increase their strength at a gold cost:

| Unit     | Strength Increase | Gold Cost |
|----------|------------------|-----------|
| Pikeman  | +3               | 10        |
| Archer   | +7               | 20        |
| Knight   | +10              | 30        |

### Transformation

Units can transform into stronger units at a gold cost:

| From     | To        | Cost |
|----------|-----------|------|
| Pikeman  | Archer    | 30   |
| Archer   | Knight    | 40   |
| Knight  | Not allowed | -    |

### Battles

An army can attack another army at any time, even if they belong to the same
civilization.

- The army with the highest total strength wins
- The winner gains 100 gold
- The loser loses its two strongest units
- In case of a draw, both armies lose one unit (decision left to the programmer)

## Project Structure

```bash
army-simulation/
│
├── armies.py # Core domain logic
├── main.py # Example usage
└── README.md
```

## How to Run

Make sure you have Python 3 installed.

From the project root, run:

```bash
python main.py
```

This will execute a simple simulation demonstrating army creation,
training, transformation, and battle resolution.

## Notes

- No persistence is used
- No user interface is implemented
- The focus is strictly on modeling the domain