"""Practicing Dictionaries for Exercise 03"""

__author__: "730649767"


def invert(Colors: dict[str, str]) -> dict[str, str]:
    """Invert Keys and Values of Dictionary"""
    return {value: key for key, value in Colors.items()}

   if __name__ == "__main__":
        Colors_invert = {"black": "blue", "purple": "pink"}
        inverted_dict = invert(Colors_invert)
        print(inverted_dict)
    


def count(values: list[str]) -> dict[str, int]:
      """Count occurences of unique values in list"""
      result = {}
      for item in values: 
            if item in result: 
                  result[item] += 1
            else:
                  result[item] = 1
        return result 

if __name__ == "__main__":
    list_result = ["1","2","3"]
    counted_values = count(list_result)
    print(counted_values)



def favorite_color(favs: dict[str, str]) -> str:
      """Return the most frequent Fav Color"""
      count_colors = count(list(favorites.values()))
      return max(count_colors, key=count_colors.get)


if __name__ == "__main__":
      favorite_dict = {"Alice": "blue", "Bob": "red", "Charlie": "blue"}
      most_freq = favorite_color(favorite_dict)
      print(most_freq)



def bin_len(Strings: list[str]) -> dict[int, set[str]]:
      """Bin strings by lengths into a dictionary"""
      result = {}
      for string in strings:
            length = len(string)
            if length in result: 
                  result[len].add(string)
            else:
                  result[length] = {string}
        return result 

if __name__ == "__main__":
      strobe = ["sky", "earth", "ocean", "moon"]
      bin_strings = bin_len(strobe)
      print(bin_strings)
      