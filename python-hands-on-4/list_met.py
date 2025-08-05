#| Method         | Description                                              | Example                |
#| -------------- | -------------------------------------------------------- | ---------------------- |
#| `append(x)`    | Adds `x` to the end of the list                          | `lst.append(10)`       |
#| `extend(iter)` | Adds elements of `iter` to the end of the list           | `lst.extend([4, 5])`   |
#| `insert(i, x)` | Inserts `x` at index `i`                                 | `lst.insert(1, 99)`    |
#| `remove(x)`    | Removes the first occurrence of `x`                      | `lst.remove(3)`        |
#| `pop(i)`       | Removes and returns the item at index `i` (default last) | `lst.pop()`            |
#| `clear()`      | Removes all items from the list                          | `lst.clear()`          |
#| `index(x)`     | Returns the index of the first `x`                       | `lst.index(10)`        |
#| `count(x)`     | Returns number of times `x` appears                      | `lst.count(2)`         |
#| `sort()`       | Sorts the list in place (ascending by default)           | `lst.sort()`           |
#| `reverse()`    | Reverses the list in place                               | `lst.reverse()`        |
#| `copy()`       | Returns a shallow copy of the list                       | `new_lst = lst.copy()` |

#________________________________________________________________________________________

import random
import time

# List of emojis to choose from
emojis = ["😀", "😂", "🤣", "😍", "🥰", "😎", "🔥", "💀", "🎉", "💯", "🚀", "🌟", "🎶", "🍕", "🎮", "⚽", "🐍", "🧠", "🌍", "👑", "🦾", "🤖", "❤️", "😈", "😇"]

# Print 1000 emojis (random)
for _ in range(1000):
    print(random.choice(emojis), end=" ")

# OR uncomment this one to print forever (WARNING: Infinite loop)
# while True:
#     print(random.choice(emojis), end=" ")
#     time.sleep(0.05)  # slow it down a little bit

