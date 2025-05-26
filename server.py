import socket  # Import library socket

HOST = '127.0.0.1'  # Alamat IP lokal (localhost)
PORT = 65432        # Port yang digunakan (harus sama dengan client)

# Membuat socket TCP (SOCK_STREAM untuk TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port
server_socket.bind((HOST, PORT))

# Mulai mendengarkan koneksi yang masuk
server_socket.listen()

print(f"[SERVER] Menunggu koneksi di {HOST}:{PORT}...")

# Menerima koneksi dari client (blocking, menunggu hingga client connect)
conn, addr = server_socket.accept()
print(f"[SERVER] Terhubung dengan {addr}")

# Loop utama untuk komunikasi dua arah
while True:
    # Terima data dari client (maks 1024 byte)
    data = conn.recv(1024)
    if not data:
        # Jika data kosong, berarti client memutus koneksi
        print("[SERVER] Koneksi ditutup oleh client.")
        break
    print(f"[CLIENT] {data.decode()}")  # Tampilkan pesan dari client

    # Minta input dari server (admin) untuk membalas
    reply = input("[SERVER] Ketik balasan: ")
    conn.sendall(reply.encode())  # Kirim balasan ke client

    # Jika balasan adalah "exit", maka keluar dari loop
    if reply.lower() == 'exit':
        print("[SERVER] Keluar.")
        break

# Tutup koneksi dengan client
conn.close()
