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

### 🎯 How to Play

**🏁 Start the Game**
Run the game using Python
python main.py
