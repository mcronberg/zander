def getLetter(key, count):
    """Return the letter corresponding to the key and count."""
    keypad_dict = {
        0: [' '],
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }
    return keypad_dict[key][count - 1]


def multi_tap(keys, times):
    
    result = ""
    count = 1

    for i in range(1, len(keys)):
        # Check if the key has changed or there is a pause
        key_changed = keys[i] != keys[i-1]
        there_is_a_pause = times[i] - times[i-1] > 0.5

        if key_changed == True or there_is_a_pause == True:
            result += getLetter(keys[i-1], count)
            count = 1
        else:
            count += 1

    # Add the last letter to the result
    result += getLetter(keys[-1], count)
    return result

keys = [7, 7, 7, 7, 6, 6, 6, 4, 7, 7, 7, 2, 6]
times = [0.4, 1.5, 1.8, 2.0, 2.2, 2.6, 2.9, 3.0, 3.3, 3.6, 3.9, 4.2, 4.3]
print(multi_tap(keys, times))  # Outputs: 'PROGRAM'


# print(getLetter(9,3))


keys = [7, 7, 7, 7, 6, 6, 6, 4, 7, 7, 7, 2, 6]
times = [0.4, 1.5, 1.8, 2.0, 2.2, 2.6, 2.9, 3.0, 3.3, 3.6, 3.9, 4.2, 4.3]
print(multi_tap(keys, times))  # Outputs: 'PROGRAM'

keys = [2, 5, 5, 5, 3, 3, 9, 9, 2, 6, 6, 3, 3, 3, 7, 7, 7]
times = [0.1, 0.2, 0.2, 0.2, 0.1, 0.2, 0.9,
          0.2, 0.2, 0.9, 0.2, .9, 1.5, 0.2, 1, .5, .5]
print(multi_tap(keys, times))  # Outputs: 'ALEXANDER'

keys = [7, 7, 7, 7, 6, 6, 6]
times = [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]
print(multi_tap(keys, times), '==', 'PRO')
