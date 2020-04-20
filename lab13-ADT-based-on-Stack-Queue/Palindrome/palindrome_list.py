from arraystack import ArrayStack


class Palindrome:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self._palindromes = []

    def _read_words(self):
        f = open(self.input_file, encoding = 'utf-8')
        lines = f.readlines()
        f.close()
        lines = list(map(lambda line: line.split()[0], lines))
        return lines

    def _is_palindrome(self, word):
        stack1 = ArrayStack(word)
        stack2 = ArrayStack(word[::-1])
        for i in range(len(word)):
            if stack1.pop() != stack2.pop():
                return False
        return True

    def _find_palindromes(self, words):
        for word in words:
            if self._is_palindrome(word):
                self._palindromes.append(word)
        
    def _write_palindromes(self):
        f = open(self.output_file, 'w', encoding='utf-8')
        for palindrome in self._palindromes:
            print(palindrome, file=f)
        f.close()
    
    def process(self):
        words = self._read_words()
        self._find_palindromes(words)
        self._write_palindromes()


if __name__ == '__main__':
    pal1 = Palindrome('base.lst', 'palindrome_uk.txt')
    pal1.process()
    pal2 = Palindrome('words.txt', 'palindrome_en.txt')
    pal2.process()
