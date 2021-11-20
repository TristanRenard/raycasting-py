import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8080))
print('Server started')


while True:
    socket.listen(100)
    conn, addr = socket.accept()
    print('Connected by', addr)

    data = conn.recv(1024)
    data = data.decode('utf-8')
    score = data + str(addr[0])+ ':' + str(addr[1])

    if data == 'exit':
        break

conn.close()
socket.close()