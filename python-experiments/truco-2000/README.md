# truco-2000 (Legacy Version)

> **This directory is no longer actively developed. The project now lives in its own repository: [mama-cailleach/truco-2000](https://github.com/mama-cailleach/truco-2000). Please visit the new repo for the latest updates and ongoing work.**

---

## About This Directory

This folder contains the **legacy code and experiments** from the earliest development stages of the `truco-2000` project. It is preserved here for historical purposes and to showcase the project's evolution.

All new development, bug fixes, and features are now handled in the dedicated repository linked above.

## What is truco-2000?

`truco-2000` is a Python project exploring the digital implementation and simulation of the traditional card game Truco. It began as an experiment in this directory and has since grown into a standalone project.

## Where to Go Next

- For the newest code, documentation, issues, and contributions, visit the main repository:  
  👉 [https://github.com/mama-cailleach/truco-2000](https://github.com/mama-cailleach/truco-2000)

- This directory will remain as a reference and should not be used as a base for new development.

---
*Legacy directory – maintained for historical and reference purposes only.*

---


# Truco 2000

## Introduction

**Truco 2000** is a feature-rich command-line implementation of the popular Brazilian card game "Truco" developed by mama. This game showcases advanced Python programming skills with object-oriented design, sophisticated game logic, and an immersive ASCII-based user interface with a retro Y2K aesthetic. Currently available in Brazilian Portuguese.

---

### What is Truco?

Truco is a popular card game in Brazil and parts of Latin America. It's a trick-taking game with unique rules:

- Players compete to win rounds ("rodadas") using a reduced deck of 40 cards
- Features a special "manilha" (trump) card system that changes each hand
- Includes strategic elements like bluffing and calling "truco" to raise the stakes
- Players can call truco at strategic moments to increase point values
- The first player to reach 12 points wins the game

---

## ✨ Features

### **Core Gameplay**
- ✅ Complete implementation of authentic Brazilian Truco rules
- ✅ Strategic truco calling system (1 → 3 → 6 → 9 → 12 points)
- ✅ Player vs intelligent computer opponent
- ✅ Proper turn-based mechanics respecting traditional Truco rules
- ✅ Authentic "manilha" (trump card) system with card hierarchy

### **Advanced Visual Experience**
- 🎨 Beautiful ASCII art card representations
- 🖥️ Clean screen-clearing interface for organized gameplay
- ⚔️ **Battle Zone**: Dedicated area showing played cards side-by-side
- 📊 Real-time game status with scores and hand values
- 🎯 Progressive card revelation with dramatic timing
- 📱 Organized layout optimized for terminal play

### **Strategic Gameplay Elements**
- 🧠 **Power Move Truco**: Call truco after seeing opponent's card
- 🏃 **Strategic Running**: Escape from unfavorable truco situations
- 🎲 **Intelligent AI**: Opponent makes strategic decisions about truco calls
- 🔄 **Complete Truco Sequence**: Support for all escalation levels
- ⚖️ **Correct Point Calculation**: Proper scoring when players run from truco

### **Enhanced User Experience**
- ✅ Robust input validation with clear error messages
- ⏱️ Smooth game flow with strategic pauses for dramatic effect
- 🎮 Intuitive controls with numbered card selection
- 📋 Clear game state display showing round results and standings
- 🎯 Visual feedback for all game actions

---

## 🎮 How to Play

### **Starting the Game**
1. Run the script: `python truco_2000_v1.0.py`
2. Follow the ASCII art intro and choose to play
3. The game displays your cards side-by-side with clear numbering

### **During Each Round**
- **Select cards**: Enter the number (1, 2, or 3) of the card you want to play
- **Call Truco**: Enter 'T' to raise the stakes (available when strategic)
- **Strategic Truco**: You can call truco after seeing your opponent's card!
- **Escape**: Enter 'F' to run away from unfavorable situations
- **Watch the Battle Zone**: See both cards displayed clearly with results

### **Truco Escalation System**
- **Normal Hand**: 1 point
- **Truco**: 3 points (first escalation)
- **Retruco**: 6 points (counter-raise)
- **Vale 9**: 9 points (further escalation)
- **Vale 12**: 12 points (maximum stakes)

### **Winning Strategy**
- Win 2 out of 3 rounds to win the hand
- Use truco strategically to maximize points
- Call truco after seeing opponent's card for maximum advantage
- Know when to run to minimize losses

---

## 🃏 Card Ranking & Rules

### **Standard Card Hierarchy** (lowest to highest)
**4, 5, 6, 7, Q, J, K, A, 2, 3**

### **Manilha System**
- The "vira" card is revealed at the start of each hand
- The next card in sequence becomes the manilha (trump)
- Manilhas beat all other cards
- When both players have manilhas, suit order determines winner: ♣ > ♥ > ♠ > ♦

### **Hand Resolution**
- Best 2 out of 3 rounds wins the hand
- Winner of each round starts the next round
- Strategic timing of truco calls can dramatically change point values

---

## 🏗️ Technical Excellence

This project demonstrates advanced programming concepts:

### **Object-Oriented Design**
- Clean class structure with separated concerns
- Encapsulated game state and behavior
- Modular methods for different game phases

### **Advanced Game Logic**
- Complex truco sequence handling
- Proper state management across rounds and hands
- Accurate implementation of Brazilian Truco rules

### **User Interface Innovation**
- Dynamic ASCII art generation
- Screen clearing and layout management
- Progressive visual reveals with timing
- Battle zone system for card display

### **Code Quality**
- Comprehensive input validation
- Error handling and edge case management
- Clean, readable, and maintainable code structure

---

## 🎨 Visual Design

### **Retro Y2K Aesthetic**
- ASCII art banner with "TRUCO 2000" branding
- Organized sections with visual separators
- Clean typography and spacing
- Terminal-optimized layout for various screen sizes

### **Battle Zone Innovation**
- Dedicated area for displaying played cards
- Side-by-side view of user and opponent cards
- Clear indication of round winner in the battle zone

---

## 🚀 Recent Improvements

### **Phase 1-3 Visual Enhancements**
- ✅ Screen clearing between rounds for clean experience
- ✅ Side-by-side card display instead of vertical stacking
- ✅ Battle zone implementation with progressive card reveals
- ✅ Organized game layout with clear sections
- ✅ Real-time game status updates

### **Strategic Gameplay Additions**
- ✅ Power move truco calling after seeing opponent's card
- ✅ Correct point calculation for truco escapes
- ✅ Proper truco state management between hands
- ✅ Enhanced AI decision making

---

## 🎯 Planned Improvements

### **Phase 4: Enhanced Polish**
- 🔜 Fine-tuned retro Windows 98/2000 aesthetic
- 🔜 Color support where available
- 🔜 Enhanced spacing and visual hierarchy
- 🔜 Sound effects simulation with ASCII

### **Gameplay Enhancements**
- 🔜 Multiple AI difficulty levels with different strategies
- 🔜 Statistics tracking across games
- 🔜 Tournament mode
- 🔜 Replay system

### **Educational Features**
- 🔜 Interactive tutorial for new players
- 🔜 Rule explanations and strategy tips
- 🔜 Practice mode against different AI personalities

### **Platform Expansion**
- 🔜 Executable (.exe) compilation for easy distribution
- 🔜 English translation
- 🔜 Cross-platform compatibility improvements

---

## 👨‍💻 About the Developer

This game showcases mama-cailleach's expertise in:

- **Advanced Python Programming**: Complex game logic and state management
- **User Experience Design**: Intuitive interfaces and visual feedback
- **Game Development**: Authentic rule implementation and strategic AI
- **Software Architecture**: Clean, maintainable, and extensible code
- **Cultural Gaming**: Authentic Brazilian card game experience

---

## 🎲 Getting Started

1. **Requirements**: Python 3.x
2. **Installation**: Download `truco_2000_v1.0.py`
3. **Run**: `python truco_2000_v1.0.py`
4. **Enjoy**: Experience authentic Brazilian Truco with modern enhancements!

---

**Note:** This project was created as a programming showcase and for entertainment purposes. Truco 2000 celebrates Brazilian gaming culture while demonstrating advanced software development techniques.

**Boa sorte e que vença o melhor!** 🃏✨
