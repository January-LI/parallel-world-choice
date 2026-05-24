
from fate import FortuneSystem, FateSystem, HistorySystem


def print_title():
    """Print the system title."""
    title_1 = "Parallel World Choice"
    width = len(title_1) + 8
    print()
    print("=" * width)
    print(title_1.center(width))
    print("=" * width)


def print_menu():
    """Print the main menu."""
    print("\nChoose an option:")
    print("1. Daily Fortune")
    print("2. Mystery Boxes Fate Assist")
    print("3. View History")
    print("0. Exit")


def wait_for_enter():
    """Wait so user can read the result before returning."""
    input("\nPress Enter to return to the main menu...")


def show_daily_fortune(fortune_system, history_system):
    """Feature 1: Draw and display daily fortune."""
    result = fortune_system.draw_daily_fortune()

    level_text = result["fortune_level"]
    message_text = result["fortune_message"]

    border_width = max(len(level_text), len(message_text)) + 8
    border_line = "-" * border_width

    print()
    print(border_line)
    print(level_text.center(border_width))
    print(message_text.center(border_width))
    print(border_line)
    print(f"Lucky Number : {result['lucky_number']}")
    print(f"Lucky Color  : {result['lucky_color']}")

    history_system.save_fortune(result)
    wait_for_enter()


def show_fate_answer(fate_system, history_system):
    """Feature 2: Mystery Boxes Fate Assist System."""
    while True:
        print("\nMystery Boxes Fate Assist System")
        print("Enter your choices one by one.")
        print("Press Enter on an empty line when you finish entering choices.")
        print("Then use a separate command to start analysis.")
        print("Type 0 to return to the main menu.")

        choices = []
        count = 1

        while True:
            value = input(f"Choice {count}: ").strip()

            if value == "0":
                return
            if value == "":
                break

            choices.append(value)
            count += 1

        if len(choices) == 0:
            print("Please enter at least one choice before analysis.")
            continue

        while True:
            cmd = input("\nEnter command (S=start analysis, 0=main menu): ").strip().lower()
            if cmd == "0":
                return
            if cmd == "s":
                break
            print("Invalid command. Please type S or 0.")

        result = fate_system.analyze_choices(choices)

        print()
        print("+======================================+")
        print("|         Parallel Fate Analysis       |")
        print("+======================================+")
        print(f"Recommended Choice: {result['recommended_choice']}")
        print()
        print(f"Lucky resonance: {result['resonance']}")
        print(f"Parallel energy: {result['parallel_energy']}")
        print(f"Lucky color: {result['lucky_color']}")
        print("========================================")
        print(f"Fate message: {result['fate_message']}")

        history_system.save_fate(result)

        back = input("\nType 2 for another analysis, or 0 for main menu: ").strip()
        if back == "2":
            continue
        if back == "0":
            break
        print("Please type 2 or 0.")


def show_history(history_system):
    """Feature 3: Display saved history records."""
    data = history_system.get_history()
    fortune_history = data.get("fortune_history", [])
    fate_history = data.get("fate_history", [])

    print("\n=== Fortune History ===")
    if len(fortune_history) == 0:
        print("No fortune records yet.")
    else:
        for i, item in enumerate(fortune_history, start=1):
            print(
                f"{i}. [{item['time']}] {item['fortune_level']} | "
                f"{item['fortune_message']} | "
                f"Lucky Number: {item['lucky_number']} | "
                f"Lucky Color: {item['lucky_color']}"
            )

    print("\n=== Fate History ===")
    if len(fate_history) == 0:
        print("No fate records yet.")
    else:
        for i, item in enumerate(fate_history, start=1):
            if "input_choices" in item and "recommended_choice" in item:
                choice_text = ", ".join(item.get("input_choices", []))
                print(
                    f"{i}. [{item['time']}] "
                    f"Choices: [{choice_text}] | "
                    f"Recommended: {item.get('recommended_choice', '')} | "
                    f"Energy: {item.get('parallel_energy', '')} | "
                    f"Lucky Color: {item.get('lucky_color', '')}"
                )
            else:
                print(
                    f"{i}. [{item['time']}] Q: {item.get('question', '')} | "
                    f"A: {item.get('fate_answer', '')}"
                )

    wait_for_enter()


def main():
    """Program entry: initialize systems and run menu loop."""
    fortune_system = FortuneSystem()
    fate_system = FateSystem()
    history_system = HistorySystem("save.json")

    print_title()

    while True:
        print_menu()
        choice = input("\nEnter option number: ").strip()

        if choice == "1":
            show_daily_fortune(fortune_system, history_system)
        elif choice == "2":
            show_fate_answer(fate_system, history_system)
        elif choice == "3":
            show_history(history_system)
        elif choice == "0":
            print("\n * May the parallel worlds guide your path. Farewell * ")
            break
        else:
            print("\nInvalid input. Please enter 0 / 1 / 2 / 3.")


if __name__ == "__main__":
    main()
