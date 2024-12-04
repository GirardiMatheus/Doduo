
# DODUO

**DODUO** is a simple and engaging turn-based combat game written in Python. Players take control of a hero to battle randomly generated enemies, leveraging strategic attacks and defenses to emerge victorious.

---

## Features

- **Dynamic Characters**: Choose your hero's name and face off against randomly selected enemies, including bats, goblins, and even dragons.
- **Turn-Based Combat**: Plan your moves carefully! Choose between normal attacks, powerful special attacks, or defense strategies.
- **Special Abilities**: Heroes can use unique skills, but be mindful of limited stamina for special moves.
- **Randomized Challenges**: Each battle includes a randomly selected enemy with unique stats and characteristics.

---

## How to Play

1. **Hero Creation**: At the start, you will enter the name of your hero.
2. **Combat Options**:
   - **Normal Attack**: Deal consistent damage to the enemy.
   - **Special Attack**: Use a powerful skill to inflict massive damage (limited by stamina).
   - **Defend**: Reduce incoming damage for the next enemy attack.
3. **Victory Conditions**: Reduce the enemy's health to 0 to win the battle.
4. **Defeat Conditions**: If your hero's health reaches 0, you lose.

---

## Installation

1. **Prerequisites**:
   - Python 3.x installed on your machine.

2. **Download**:
   Clone the repository or download the project files to your local machine.

3. **Run**:
   Navigate to the project folder and execute the following command in your terminal:

   ```bash
   python main.py
   ```

---

## Game Design Overview

- **Hero**: Your customizable character with:
  - A name of your choice.
  - A fixed skill: "Super Strength."
  - Limited stamina for special attacks.
- **Enemy**: Randomly generated opponents:
  - Types: Bat, Goblin, Dragon.
  - Each has unique health, level, and damage output.
- **Combat System**:
  - Normal and special attacks based on character stats.
  - Turn-based structure, alternating between the hero and the enemy.

---

## Example Gameplay

```text
==================================================
DODUO - TURN-BASED COMBAT GAME
==================================================

Welcome to DODUO! Prepare for an epic battle!

Instructions:
1. Use Normal Attacks to deal consistent damage.
2. Save stamina for powerful Special Attacks.
3. Strategically manage your moves to defeat the enemy.

Enter your hero's name: DoduoKing
Battle Start!

=== Current Stats ===
Name: DoduoKing
Health: 100
Level: 5

Name: Dragon
Health: 120
Level: 6
=====================

Press Enter to continue...
Choose (1 - Normal Attack, 2 - Special Attack, 3 - Defend): 2
DoduoKing used the special skill Super Strength on Dragon and dealt 45 damage!
Dragon (Boss) attacked DoduoKing and dealt 20 damage!
...
```

---

## Future Improvements

- Add more character classes with unique abilities.
- Implement a leveling system for the hero.
- Add multiple battles in a single session.
- Include a high-score tracker.

---

## License

This project is free to use and modify. Contributions are welcome!
