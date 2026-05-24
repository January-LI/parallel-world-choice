
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
    print("2. Decision Fate")
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
    """Feature 2: Ask a question and get fate answer."""
    print("\nEnter your question:")
    question = input("> ").strip()

    if question == "":
        question = "(No question entered)"

    while True:
        result = fate_system.ask(question)

        answer_text = result["fate_answer"]
        line_text = f"Fate says: {answer_text}"
        width = len(line_text) + 8

        print()
        print("-" * width)
        print(line_text.center(width))
        print("-" * width)

        history_system.save_fate(result)

        back = input("\nType 2 for another answer, or 0 for main menu: ").strip()
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
            print(
                f"{i}. [{item['time']}] Q: {item['question']} | "
                f"A: {item['fate_answer']}"
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
