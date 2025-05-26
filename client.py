import socket  # Import library socket

HOST = '127.0.0.1'  # Alamat IP server (localhost)
PORT = 65432        # Port yang digunakan server

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksi ke server menggunakan IP dan port
client_socket.connect((HOST, PORT))

# Loop utama untuk komunikasi dua arah
while True:
    # Minta input dari user untuk dikirim ke server
    msg = input("[CLIENT] Ketik pesan: ")
    client_socket.sendall(msg.encode())  # Kirim pesan ke server

    # Jika pesan adalah "exit", keluar dari loop
    if msg.lower() == 'exit':
        print("[CLIENT] Keluar.")
        break

    # Terima balasan dari server (maks 1024 byte)
    data = client_socket.recv(1024)
    if not data:
        # Jika tidak ada data, berarti server menutup koneksi
        print("[CLIENT] Koneksi ditutup oleh server.")
        break
    print(f"[SERVER] {data.decode()}")  # Tampilkan balasan dari server

# Tutup koneksi dengan server
client_socket.close()
