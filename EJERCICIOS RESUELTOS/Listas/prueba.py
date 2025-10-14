from list_ import List
from super_heroes_data import superheroes


def count_superheroes(superheroes_list):
  """
  Counts the total number of superhero and villain characters in a list.

  Args:
    superheroes_list: A list of dictionaries, where each dictionary
                      represents a character.

  Returns:
    An integer representing the total count of characters.
  """
  return len(superheroes_list)

# Example usage with the provided data:
# Assuming the list from the file is available as 'superheroes'

total_characters = count_superheroes(superheroes)
print(f"Total number of characters: {total_characters}")
