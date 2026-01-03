from storage_expansion import load_data
from cli import run_cli

def main():
    data = load_data()
    run_cli(data)

if __name__ == "__main__":
    main()
