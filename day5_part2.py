"""
what is the password?
"""
from hashlib import md5

door_id = "ojvtpuvg"
# door_id = "abc"
password = ["", "", "", "", "", "", "", ""]
count = 0
for i in range(1, 115278569):
    candidate = door_id + str(i)
    digest = md5(candidate.encode("utf-8")).hexdigest()
    if digest.startswith("00000"):
        try:
            pos = int(digest[5])
            if pos < 8 and password[pos] == "":
                password[pos] = digest[6]
                count += 1
                print(password)
        except ValueError:
            continue
    if count == 8:
        break
print("".join(password))
