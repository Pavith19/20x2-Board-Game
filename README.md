# 🎲 20x2 Game

A captivating console-based board game where players compete against the computer in a strategic race to reach the finish line while avoiding treacherous black holes!

## 🎮 Game Overview

20x2 is an exciting dice-rolling board game where you compete against a computer opponent. Navigate through a 20-block board, dodge black holes, and be the first to reach or pass block 20 to win!

![Game Board Example]
```
 |# |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|18|19|20|
 |H |  |  |  |  |  |  |O |  |  |  |  |  |  |O |  |  |  |  |  |  |
 |C |  |  |  |  |  |  |O |  |  |  |  |  |  |O |  |  |  |  |  |  |
```

## ✨ Features

- Interactive console-based gameplay
- Dynamic board visualization
- Random dice rolling mechanics
- Strategic black hole obstacles
- Automatic game session logging
- Detailed game statistics tracking
- Play multiple rounds
- End-of-game summary reports

## 🎯 Game Rules

1. **Starting the Game**
   - Players must roll a 6 to enter the game board
   - The game begins once a player successfully enters

2. **Movement**
   - Players move based on half the dice value:
     - Roll 6 → Move 3 blocks
     - Roll 5 → Move 2 blocks
     - Roll 4 → Move 2 blocks
     - Roll 3 → Move 1 block
     - Roll 2 → Move 1 block
     - Roll 1 → No movement

3. **Black Holes**
   - Located at blocks 7 and 14
   - Landing on a black hole sends you back to block 1
   - Players can pass over black holes without penalty

4. **Winning**
   - First player to reach or pass block 20 wins
   - Game automatically ends when a winner is determined

## 🛠️ Technical Requirements

- Python 3.x
- Required modules:
  - `random`
  - `time`
  - `datetime`

## 📁 Project Structure

```
20x2_Game/
│
├── 20x2_Game.py           # Main game file
├── tableANDdiceroll.py    # Game board and dice mechanics
├── game_summery.py        # Game statistics display
└── game_session_textfile.py # Session logging functionality
```

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/20x2_Game.git
```

2. Navigate to the project directory:
```bash
cd 20x2_Game
```

3. Run the main game file:
```bash
python 20x2_Game.py
```

## 📊 Game Statistics

The game automatically tracks and saves:
- Total moves made by each player
- Number of black hole hits
- Game outcome
- Session timestamp

## 📝 Session Logging

- Each game session is automatically saved
- Filename format: `YYYY_MM_DD_HH_MM.txt`
- Contains detailed game statistics and outcome

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

<h3 align="center">Connect with me:</h3>
<p align="center">
  <a href="https://instagram.com/_mr_2001__" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="_mr_2001__" height="30" width="40" /></a>
  <a href="https://www.linkedin.com/in/pavith-bambaravanage-465300293/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="pavith-bambaravanage-465300293" height="25" width="35" /></a>
  <a href="https://www.hackerrank.com/@pavith_db" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="@pavith_db" height="40" width="45" /></a>
  <a href="https://www.leetcode.com/pavith_db" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="pavith_db" height="30" width="40" /></a>
  <a href="mailto:pavithd2020@gmail.com" target="blank"><img align="center" src="https://github.com/TheDudeThatCode/TheDudeThatCode/raw/master/Assets/Gmail.svg" alt="pavithd2020@gmail.com" height="30" width="40" /></a>
</p>
