"""
what is the password?
"""
from hashlib import md5

door_id = "ojvtpuvg"
# door_id = "abc"
password = ""

for i in range(1, 115278569):
    candidate = door_id + str(i)
    digest = md5(candidate.encode("utf-8")).hexdigest()
    if digest.startswith("00000"):
        password += digest[5]
        print(password)
    if len(password) == 8:
        break
print(password)
