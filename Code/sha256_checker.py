import hashlib

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(1024):
            h.update(chunk)
    return h.hexdigest()

print(sha256sum('large_test_file.txt'))
print(sha256sum('received_large_file.txt'))
