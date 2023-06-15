import platform
import random
import sys

def main():
  if len(sys.argv) != 2:
    raise RuntimeError("bad argument, needs one")

  match sys.argv[1]:
    case "runner":
      match random.randint(0, 2):
        case 0: print("ubuntu-latest")
        case 1: print("windows-latest")
        case 2: print("macos-latest")

    case "info":
      print(f"{platform.system()} {platform.uname()}")

    case _:
      raise RuntimeError(f"bad argument '{sys.argv[1]}'")

if __name__ == "__main__":
  main()