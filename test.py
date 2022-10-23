
import hashlib

previous_proof = 1
new_proof = 1
check_proof = False

while check_proof is False:
    hash_operation = hashlib.sha256(
        str(new_proof**2 - previous_proof**2).encode()).hexdigest()
    print('temp hash', hash_operation)
    # break
    if hash_operation[:5] == '00000':
        check_proof = True
    else:
        new_proof += 1

print(new_proof)
print(hash_operation)
