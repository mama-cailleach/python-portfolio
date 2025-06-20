# Testing the Scorecard Generator

## Setup
1. Make sure you're in the project root directory
2. Install test dependencies:
```bash
pip install pytest
```

## Running Tests
Run all tests:
```bash
python -m unittest discover tests
```

Run a specific test file:
```bash
python -m unittest tests/test_models.py
```

Run a specific test class:
```bash
python -m unittest tests/test_models.py TestPlayer
```

Run a specific test method:
```bash
python -m unittest tests/test_models.py TestPlayer.test_player_initialization
```

## Test Structure
- `tests/test_models.py`: Tests for Player and Team classes
- `tests/test_game_logic.py`: Tests for game logic functions
- `tests/test_scorecard.py`: Tests for scorecard generation
- `tests/test_data/`: Contains test data files

## Writing New Tests
1. Create test methods that start with `test_`
2. Use descriptive names that explain what you're testing
3. Use assertions to check expected vs actual results
4. Group related tests in test classes
5. Use setUp() for common initialization
