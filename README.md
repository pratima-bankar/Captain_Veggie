# 🥕 Captain Veggie 🐇

## 🎮 Game Overview
**Captain Veggie** is a fun, interactive game where the player takes on the role of Captain Veggie, who must **harvest as many vegetables as possible** before a group of hungry rabbits eats them! The game ends when all vegetables have been removed from the field, and the player’s **final score** is displayed.

## 🚀 Features
- **Randomized game board** with vegetables scattered across the field.
- **Player-controlled movement** using W/A/S/D keys.
- **Rabbits move randomly**, consuming vegetables in their path.
- **Dynamic scoring system** based on vegetable values.
- **Game over display** showing the collected vegetables and total score.
- **High score tracking** to save and compare player achievements.

## 🛠️ Game Components
The game is structured using **object-oriented programming (OOP)** principles with the following classes:

### 🌿 **Game Entities**
- **FieldInhabitant**: Base class for all objects in the field.
- **Veggie**: Represents vegetables with different point values.
- **Creature**: Base class for movable entities (Captain & Rabbits).
- **Captain**: The player character, controlled using keyboard inputs.
- **Rabbit**: Moves randomly, consuming vegetables in its path.

### 🕹️ **Game Logic**
- **GameEngine**: Handles game setup, player and rabbit movements, field updates, scoring, and game over conditions.

## 📂 Files & Code Structure
```
📂 Captain-Veggie-Game
│── 📄 README.md           # This file
│── 📄 FieldInhabitant.py  # Base class for all field objects
│── 📄 Veggie.py           # Vegetable class
│── 📄 Creature.py         # Base class for moving entities
│── 📄 Captain.py          # Captain Veggie (player)
│── 📄 Rabbit.py           # Rabbits (AI enemies)
│── 📄 GameEngine.py       # Core game logic
│── 📄 main.py             # Runs the game
│── 📄 highscore.data      # Stores high scores
│── 📄 veggie.txt          # Stores vegetable data
```


## 🎯 How to Play

### 🏁 **Start the Game**
1. **Run the game using Python**
   ```bash
   python main.py
   ```

2. **Move Captain Veggie using the following keys:**
   - `W` - Move **Up**
   - `A` - Move **Left**
   - `S` - Move **Down**
   - `D` - Move **Right**

3. **Game Objectives**
   - Move around the field to **collect vegetables**.
   - Avoid stepping on **rabbits**.
   - Harvest as many vegetables as possible before they are all gone.

4. **Game Over**
   - The game ends when all vegetables are collected.
   - The final **score** and list of collected vegetables will be displayed.

---
## 📊 Scoring System
- Each vegetable has a **different point value**.
- The more vegetables you collect, the **higher your score**.
- The **final score** is displayed at the end.

---

## 🏆 High Score Tracking
- After the game ends, **enter your initials** to save your score.
- The game will store and display the **top high scores**.

---

## 🛠️ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Captain-Veggie.git
   cd Captain-Veggie
   ```
2. **Run the game**:
   ```bash
   python main.py
   ```

---
