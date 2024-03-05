import socket

def client(host='localhost', port=2000):
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # send message to server
        message = input("[+] Enter string: ")
        sock.sendto(message.encode('utf-8'), (host, port))
        print("[+] Sending to {0}:{1}".format(host, port))

        # receive response from server
        response, addr = sock.recvfrom(4096)
        print("[+] Received", repr(response.decode('utf-8')))

if __name__ == "__main__":
    client()
