from rich import print as rprint
from rich.console import Console
from get_files import get_files
def main():
    files = get_files()
    console = Console()
    for file in files:
        with open(file,"r") as f:
            lines = f.readlines()
            Lines = []
            for line in lines:
                Lines.append(line.replace("\n", ""))
            for line in Lines:
                if "debug" in line.lower():
                    pre_debug = Lines[Lines.index(line)].split('debug')                        
                    pretty_line = f"{pre_debug[0]}[red underline]debug{pre_debug[1]}[/red underline]"
                    console.print(f"DEBUG STATEMENT AT {f.name.rsplit('/',1)[1]}:{Lines.index(line)+1}: {pretty_line} ",highlight=False)
if __name__ == "__main__":
    main()