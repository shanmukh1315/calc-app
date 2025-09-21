from calculator import add, subtract, multiply, divide

HELP = """Simple Calculator REPL
Commands:
  add A B
  sub A B
  mul A B
  div A B
  help
  quit / exit
"""

def parse_two_numbers(parts):
    if len(parts) != 3:
        raise ValueError("Expected exactly two numbers, e.g., 'add 2 3'")
    try:
        a = float(parts[1]); b = float(parts[2])
    except ValueError:
        raise ValueError("Arguments must be numbers, e.g., 'mul 2 4.5'")
    return a, b

def main():
    print(HELP)
    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not line:
            continue
        op = line.split()[0].lower()
        if op in ("quit", "exit"):
            print("Goodbye!"); break
        if op == "help":
            print(HELP); continue
        parts = line.split()
        try:
            a, b = parse_two_numbers(parts)
            if op in ("add", "+"): print(add(a, b))
            elif op in ("sub", "subtract", "-"): print(subtract(a, b))
            elif op in ("mul", "multiply", "*"): print(multiply(a, b))
            elif op in ("div", "divide", "/"): print(divide(a, b))
            else: print("Unknown command. Type 'help' for usage.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
