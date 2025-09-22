class FileReader:
    def __init__(self, file_name: str, max_lines: int):
        self.file_name = file_name
        self.max_lines = max_lines

    def read(self):
        try:
            with open(self.file_name, encoding="utf-8") as f:
                for _ in range(self.max_lines):
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split()
                    if len(parts) == 2:
                        yield parts[0], parts[1]
        except FileNotFoundError as e:
            raise e