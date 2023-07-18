def caesarCypherV2(alphabet, text, shift, direction):
    """
        !! explnation of alphabet[shift:] + alphabet[:shift]
        The line `updated_list = alphabet[shift:] + alphabet[:shift]` creates the `updated_list` by combining two parts of the `alphabet` list.

        Let's break down the line step by step:

        1. `alphabet[shift:]`: This part creates a sublist of `alphabet` starting from the `shift` index 
            and includes all elements until the end of the list. 
            For example, if `shift` is 3, `alphabet[shift:]` will be `['d', 'e', 'f', ..., 'z']`. 
            This sublist contains the elements that need to be moved to the beginning of the `updated_list`.

        2. `alphabet[:shift]`: This part creates a sublist of `alphabet` starting from index 0 
            and includes all elements until the `shift` index (excluding). 
            For example, if `shift` is 3, `alphabet[:shift]` will be `['a', 'b', 'c']`. 
            This sublist contains the elements that need to be moved to the end of the `updated_list`.

        3. `alphabet[shift:] + alphabet[:shift]`: By concatenating the two sublists, 
            we create the `updated_list`. The elements from `alphabet[shift:]` are placed first in the `updated_list`, 
            followed by the elements from `alphabet[:shift]`. 
            This arrangement ensures that the elements are shifted by the specified `shift` amount.

        The resulting `updated_list` will contain the elements of `alphabet` 
        rearranged according to the `shift` value.
        For example, if `alphabet` is `['a', 'b', 'c', 'd', 'e', 'f', 'g']` and `shift` is 2, 
        the resulting `updated_list` will be `['c', 'd', 'e', 'f', 'g', 'a', 'b']`.
    """
    
    if direction.lower() == "decode":
        shift = -shift
    
    if shift > (len(alphabet) - 1):
        shift = shift % (len(alphabet) - 1)
    
    updated_list = alphabet[shift:] + alphabet[:shift]
    print(alphabet[shift:], alphabet[:shift])
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += updated_list[index]
        else:
            result += char
    
    return result

def caesarCypherV1(alphabet, text, shift, direction):
    if direction.lower() == "decode":
        shift = -shift

    indices_to_remove = range(0, abs(shift))
    deleted_list = []
    updated_list = []
    for i, item in enumerate(alphabet):
        if i not in indices_to_remove:
            updated_list.append(item)
        else:
            deleted_list.append(item)
    
    for i, item in enumerate(deleted_list):
        updated_list.append(item)
    
    if shift < 0:
        shift_list = alphabet
        alphabet = updated_list
        updated_list = shift_list
        
    encription = ""
    
    for item in text:
        if item in alphabet:
            index = alphabet.index(item)
            encription += updated_list[index]
        else:
            encription += item
    
    return encription

def caesarCypherAngela(alphabet, plain_text, shift_amount, direction):
    alphabet *= 2
    result = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction.lower() == "encode":
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount
        result += alphabet[new_position]

    return result
            

