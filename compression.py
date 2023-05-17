
class Compression:

    def __init__(self):
        self.table_of_codes = {}
        self.list_of_symbols = []
        self.sequence = []

    def compress(self, source_path: str, dest_path: str) -> None:
        [self.list_of_symbols.append(chr(x)) for x in range(2**16)]

        with open(source_path, "r") as f:
            file_str = f.read()

            total_str = file_str[:1]
            tmp_str = total_str
            # self.sequence.append(self.list_of_symbols.index(tmp_str))
            for i in range(1, len(file_str)):
                ch = file_str[i]
                tmp_str += ch
                if tmp_str in self.list_of_symbols:
                    pass
                else:
                    self.list_of_symbols.append(tmp_str)
                    seq_to_append = tmp_str[:len(tmp_str)-1]
                    self.sequence.append(self.list_of_symbols.index(seq_to_append))
                    tmp_str = tmp_str[len(tmp_str)-1:]
        print()






