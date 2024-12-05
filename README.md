
# DODUO RPG

DODUO RPG is a text-based battle game where you control a hero fighting dangerous enemies. The game features turn-based combat, special abilities, and now supports saving and loading progress!

## 🧩 Game Features
- **Character Creation**: Heroes and enemies are generated with attributes like health, level, and special abilities.
- **Combat System**:
  - Normal and special attacks.
  - Defend mode to reduce incoming damage.
- **Random Enemies**: Each match spawns unique enemies with different types and skills.
- **Save and Load Progress**:
  - Save the game state to a file.
  - Load a saved game to continue where you left off.
- **ASCII Art**: Stylish presentation for terminal immersion.

## 🎮 How to Play
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/doduo-rpg.git
   cd doduo-rpg
   ```
2. Run the game:
   ```bash
   python doduo_rpg.py
   ```
3. Enter your hero's name and start the battle!

### Battle Options
- **1**: Perform a normal attack.
- **2**: Use a special attack (limited by stamina).
- **3**: Defend to reduce damage on the next turn.
- **4**: Save your progress and quit the game.

### Starting from a Saved Game
- If a saved game exists, you will be prompted to load it when starting the game.

## 💾 Code Structure
- `Character`: Base class for heroes and enemies.
- `Hero`: Player-controlled hero with special skills.
- `Enemy`: Randomly generated enemies with different types.
- `Game`: Manages the game flow, including saving and loading progress.

## 🛠️ Technical Features
- **Save Progress**:
  - Hero and enemy state is saved in a `game_save.pkl` file using the `pickle` module.
- **Load Progress**:
  - Checks for an existing save file and restores the game state.
- **Error Handling**:
  - Validates the existence of a save file before loading.

## 🚀 Future Improvements
- Add new enemy types and abilities.
- Implement adjustable difficulty levels.
- Enhance terminal interface visuals.

## 🤝 Contributions
Feel free to open issues or submit pull requests with suggestions and improvements.

---

💡 **Enjoy playing DODUO RPG!**
