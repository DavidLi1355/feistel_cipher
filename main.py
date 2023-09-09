def rand_key(p: int):
    import random

    key: str = ""
    for _ in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key = key + temp

    return key


def exor(a: str, b: str):
    temp = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            temp += "0"
        else:
            temp += "1"

    return temp


def string_to_hex(s: str):
    str_data = ""
    for i in range(0, len(s), 4):
        temp_data = s[i : (i + 4)]
        str_data += str(hex(int(temp_data, 2)))[-1]
    return str_data


def encrypt(password: str):
    password_ascii: str = "".join([format(ord(x), "08b") for x in password])
    m: int = len(password_ascii) // 2
    left: str = password_ascii[:m]
    right: str = password_ascii[m:]

    key1: str = rand_key(len(right))
    f1 = exor(right, key1)
    right1: str = exor(f1, left)
    left1 = right

    key2: str = rand_key(len(right1))
    f2 = exor(right1, key2)
    right2: str = exor(f2, left1)
    left2 = right1

    ans = left2 + right2

    cipher = string_to_hex(ans)
    key1_hex = string_to_hex(key1)
    key2_hex = string_to_hex(key2)

    return cipher, key1_hex, key2_hex


def decrypt(cipher: str, key1_hex: str, key2_hex: str):
    password_ascii: str = "".join([format(int(x, 16), "04b") for x in cipher])
    key1 = "".join([format(int(x, 16), "04b") for x in key1_hex])
    key2 = "".join([format(int(x, 16), "04b") for x in key2_hex])

    m: int = len(password_ascii) // 2
    left: str = password_ascii[:m]
    right: str = password_ascii[m:]

    f1 = exor(left, key2)
    left1: str = exor(right, f1)
    right1 = left

    f2 = exor(left1, key1)
    left2: str = exor(right1, f2)
    right2 = left1

    ans = left2 + right2

    str_data = ""
    for i in range(0, len(ans), 8):
        temp_data = ans[i : i + 8]
        decimal_data = int(temp_data, 2)
        str_data = str_data + chr(decimal_data)

    print("password:", str_data)

    return 0


if __name__ == "__main__":
    x = int(input("(1)Decrypt (2)Encrypt: "))

    if x == 1:
        cipher: str = input("Cipher: ")
        key1: str = input("Key1: ")
        key2: str = input("Key2: ")
        decrypt(cipher, key1, key2)
    elif x == 2:
        password: str = input("Password: ")
        cipher, key1, key2 = encrypt(password)
        print("cipher: " + cipher, "key1: " + key1, "key2: " + key2, sep="\n")
    else:
        exit()
