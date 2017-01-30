import string

def encrypt(text, rot):
    encryptedText = ""
    for char in text:
        encryptedText += rotate_character(char,rot)
    return encryptedText

def rotate_character(char, rot):
    # Store the index of the final letter of the alphabet_position
    # Should be 25
    alphaLowerFinal = len(string.ascii_lowercase)-1
    alphaUpperFinal = len(string.ascii_uppercase)-1
    # Check if alpha-numeric character
    if char.isalpha():
        newCharIndex = alphabet_position(char)
        # Check if it's lowercase
        if char in string.ascii_lowercase:
            # if alphabet_position + rot > alphaLowerFinal then it is going to cycle
            # otherwise, it's not going to cycle.
            if newCharIndex + rot > alphaLowerFinal:
                # (Subtract to get to end of current alphabet) % Length of alphabet
                # The result is how far into the new alphabet we need to go
                if (rot - (alphaLowerFinal - newCharIndex)) < alphaLowerFinal:
                    newCharIndex = (rot - (alphaLowerFinal - newCharIndex)) - 1
                else:
                    newCharIndex = (rot - (alphaLowerFinal - newCharIndex)) % alphaLowerFinal -2
            else:
                newCharIndex += rot
            return string.ascii_lowercase[newCharIndex]
        # if it's not lowercase, it's uppercase
        else:
            if newCharIndex + rot > alphaUpperFinal:
                if (rot - (alphaUpperFinal - newCharIndex)) < alphaUpperFinal:
                    newCharIndex = (rot - (alphaUpperFinal - newCharIndex)) - 1
                else:
                    newCharIndex = (rot - (alphaUpperFinal - newCharIndex)) % alphaUpperFinal -2
            else:
                newCharIndex += rot
            return string.ascii_uppercase[newCharIndex]
    # If it's not in the alphabet, just return the character.
    else:
        return char

def alphabet_position(letter):
    letter = letter.lower()
    return string.ascii_lowercase.index(letter)
