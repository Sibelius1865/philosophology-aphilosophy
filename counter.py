import os


def count_characters_in_files():
  total_characters = 0
  file_counts = {}
  current_directory = os.getcwd()
  
  for root, _, files in os.walk(current_directory):
    for file in files:
      if file.endswith('.txt') or file.endswith('.md'):
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, current_directory)
        try:
          with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            char_count = len(content)
            file_counts[relative_path] = char_count
            total_characters += char_count
        except Exception as e:
          print(f"Error reading file {relative_path}: {e}")

  return total_characters, file_counts


if __name__ == "__main__":
  total_characters, file_counts = count_characters_in_files()

  for relative_path, char_count in file_counts.items():
    print(f"{relative_path}: {char_count} characters")