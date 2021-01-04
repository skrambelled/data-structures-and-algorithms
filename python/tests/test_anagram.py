from code_challenges.anagram.anagram import anagram


def test_one():
  assert anagram("Eleven plus two", "Twelve plus one") == True


def test_two():
  assert anagram("Clint Eastwood", "Old West Action") == True


def test_three():
  assert anagram("Software", "Swear often") == False


def test_four():
  assert anagram("Astronomers", "Moon starers") == True
