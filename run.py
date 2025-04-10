import sys
from lsa.interpreter import interpret

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python run.py yourscript.lsa")
        sys.exit(1)
    
    script_path: str = sys.argv[1]

    try:
        with open(script_path, "r") as file:
            code = file.read()
        interpret(code)
    except FileNotFoundError:
        print(f"Error: File not found: {script_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Execution error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()