import random
import time


def translate(text, language):
    translations = {
        "Welcome to the 1998 World Cup Final Simulation!\n": {
            "english": "Welcome to the 1998 World Cup Final Simulation!\n",
            "portuguese": "Bem-vindo à Simulação da Final da Copa do Mundo de 1998!\n"
        },
        "Select your team:\n": {
            "english": "Select your team:\n",
            "portuguese": "Selecione sua equipe:\n"
        },
        "1. Brazil\n": {
            "english": "1. Brazil",
            "portuguese": "1. Brasil"
        },
        "2. France\n": {
            "english": "2. France\n",
            "portuguese": "2. França\n"
        },
        "Enter your choice: ": {
            "english": "Enter your choice: ",
            "portuguese": "Digite sua escolha: "
        },
        "Simulation of the 1998 World Cup Final:": {
            "english": "Simulation of the 1998 World Cup Final:",
            "portuguese": "Simulação da Final da Copa do Mundo de 1998:"
        },
        "First Half:": {
            "english": "First Half:",
            "portuguese": "Primeiro Tempo:"
        },
        "Halftime break.": {
            "english": "Halftime break.",
            "portuguese": "Intervalo."
        },
        "Press 1 to continue to the second half: ": {
            "english": "Press 1 to continue to the second half: ",
            "portuguese": "Pressione 1 para continuar para o segundo tempo: "
        },
        "Second Half:": {
            "english": "Second Half:",
            "portuguese": "Segundo Tempo:"
        },
        "Loading...": {
            "english": "Loading...",
            "portuguese": "Carregando..."
        },
        "wins the match!": {
            "english": "wins the match!",
            "portuguese": "vence o jogo!"
        },
        "It's a draw!": {
            "english": "It's a draw!",
            "portuguese": "É um empate!"
        },
        "Brazil": {
            "english": "Brazil",
            "portuguese": "Brasil"
        },
        "France": {
            "english": "France",
            "portuguese": "França"
        }
    }
    return translations[text][language]


def simulate_match(team1, team2, language):
    print(translate("Simulation of the 1998 World Cup Final:", language),
          f"{translate(team1, language)} vs {translate(team2, language)}\n")

    # First Half
    print(translate("First Half:", language))
    goals_team1_first_half = random.randint(0, 3)
    goals_team2_first_half = random.randint(0, 3)
    print(translate("Loading...", language))
    time.sleep(5)
    print(
        f"{translate(team1, language)} {goals_team1_first_half} - {translate(team2, language)} {goals_team2_first_half}\n")

    # Halftime break
    print(translate("Halftime break.", language))
    input(translate("Press 1 to continue to the second half: ", language))

    # Second Half
    print("\n" + translate("Second Half:", language))
    goals_team1_second_half = random.randint(0, 3)
    goals_team2_second_half = random.randint(0, 3)
    print(translate("Loading...", language))
    time.sleep(5)
    print(
        f"{translate(team1, language)} {goals_team1_first_half + goals_team1_second_half} - {translate(team2, language)} {goals_team2_first_half + goals_team2_second_half}\n")

    total_goals_team1 = goals_team1_first_half + goals_team1_second_half
    total_goals_team2 = goals_team2_first_half + goals_team2_second_half

    if total_goals_team1 > total_goals_team2:
        print(f"{translate(team1, language)} {translate('wins the match!', language)}")
    elif total_goals_team1 < total_goals_team2:
        print(f"{translate(team2, language)} {translate('wins the match!', language)}")
    else:
        print(translate("It's a draw!", language))


def main():
    print("Choose your language:\n")
    print("1. English")
    print("2. Português")
    language_choice = input("Enter your choice: ")

    if language_choice == '1':
        language = 'english'
    elif language_choice == '2':
        language = 'portuguese'
    else:
        print("Invalid choice. Defaulting to English.")
        language = 'english'

    print(translate("Welcome to the 1998 World Cup Final Simulation!\n", language))
    print(translate("Select your team:\n", language))
    print(translate("1. Brazil\n", language))
    print(translate("2. France\n", language))
    choice = input(translate("Enter your choice: ", language))

    if choice == '1':
        simulate_match("Brazil", "France", language)
    elif choice == '2':
        simulate_match("France", "Brazil", language)
    else:
        print("Invalid choice. Please enter 1 for Brazil or 2 for France.")


if __name__ == "__main__":
    main()
