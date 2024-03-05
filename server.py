import socket
    def server(host='localhost', port=2000):
        # create socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # bind socket to address
            sock.bind((host, port))
            print("[+] Server listening on {0}:{1}".format(host, port))
            
            while True:
                # receive message from client
                data, addr = sock.recvfrom(4096)
                print("[+] Received from", addr)
                
                # process the message
                response = data.decode('utf-8').upper()
                
                # send response back to client
                sock.sendto(response.encode('utf-8'), addr)
                print("[+] Sent", repr(response), "to", addr)

    if __name__ == "__main__":
        server()
