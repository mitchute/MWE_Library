import mwe_lib
from pathlib import Path


def increment(x: int) -> int:
    mwe_root = Path(mwe_lib.__file__).parent
    message_file = mwe_root / 'message.txt'
    message_contents = message_file.read_text()
    print(message_contents)
    return x + 1
