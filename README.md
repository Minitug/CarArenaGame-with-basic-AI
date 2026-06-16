# CarArena – AI Learning Journey
Python-based vehicle simulation project built as part of my AI learning journey.

This project focuses on building a simple driving environment with custom physics and later training AI agents to drive efficiently.

## Current Features
- **Game**: Real-time car driving sandbox.  
- **Physics**: Physics:
-- Acceleration and braking
-- Steering with gradual turn-in and return
-- Friction / coasting behaviour
-- Arena boundary collision
- **Rendering:** 
-- Pygame-based renderer
-- Rotating vehicle visualisation
-- HUD showing current speed

## How to run
1. Clone the repo  
2. Create and activate a virtual environment
3. Run from project root in .venv "python -m runners.play_gui"


## Tech Stack
- Python 3.13
- Pygame (rendering + GUI)

## Architecture
- Modular package structure (core, rendering, runners)
- OOP design (Car, environment, physics systems)

## Concepts & Techniques
- Delta time simulation
- Continuous input handling
- Vehicle movement modelling
- Collision handling
- Real-time rendering loop

## Planned Future Additions
### Arena
- Static obstacles
- Multiple arena layouts
- Improved collision handling
- Surface behaviour experimentation

### AI
- Genetic Algorithm driver
- NEAT-based driver
- Compare AI driving styles