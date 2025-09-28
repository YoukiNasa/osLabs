import os

r, w = os.pipe()

pid = os.fork()
if pid > 0:
    os.close(r)
    os.write(w, b"Hello from parent!")
    os.close(w)
else:
    os.close(w)
    data = os.read(r, 100)
    print(f"Child received: {data.decode()}")
    os.close(r)