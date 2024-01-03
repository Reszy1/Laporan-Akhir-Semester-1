import tkinter as tk
from tkinter import messagebox

class TokoEbookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Toko Digital Ebook")

        # Variabel untuk menyimpan data transaksi
        self.transaksi = []

        # Daftar menu produk
        self.menu_produk = [
            {"nama": "Python Programming", "harga": "25.000"},
            {"nama": "Web Development Basics", "harga": "30.000"},
            {"nama": "Data Science Essentials", "harga": "35.000"},
            {"nama": "C++ Uncover", "harga": "60.000"},
            {"nama": "Pascal Uncover", "harga": "50.000"},
            {"nama": "HTML Uncover", "harga": "50.000"},
            {"nama": "CSS Uncover", "harga": "60.000"},
            {"nama": "PHP Uncover ", "harga": "60.000"},
            {"nama": "Bootstrap Uncover", "harga": "60.000"},
        ]

        # Opsi pembayaran
        self.metode_pembayaran = [
            "Transfer Bank",
            "Kartu Kredit",
            "E-wallet",
            "Tunai (Bayar di Tempat)"
        ]

        # Frame untuk input
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(padx=10, pady=10)

        # Label dan Entry untuk input buku dan harga
        tk.Label(self.frame_input, text="Produk:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_produk = tk.StringVar()
        self.combo_produk.set(self.menu_produk[0]["nama"])
        self.dropdown_produk = tk.OptionMenu(self.frame_input, self.combo_produk, * [produk["nama"] for produk in self.menu_produk])
        self.dropdown_produk.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Jumlah:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_jumlah = tk.Entry(self.frame_input)
        self.entry_jumlah.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Metode Pembayaran:").grid(row=2, column=0, padx=5, pady=5)
        self.combo_pembayaran = tk.StringVar()
        self.combo_pembayaran.set(self.metode_pembayaran[0])
        self.dropdown_pembayaran = tk.OptionMenu(self.frame_input, self.combo_pembayaran, *self.metode_pembayaran)
        self.dropdown_pembayaran.grid(row=2, column=1, padx=5, pady=5)

        # Tombol tambah produk
        tk.Button(self.frame_input, text="Tambah Produk", command=self.tambah_produk).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame untuk output
        self.frame_output = tk.Frame(root)
        self.frame_output.pack(padx=10, pady=10)

        # Output transaksi (nota)
        tk.Label(self.frame_output, text="Nota Transaksi").grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.text_nota = tk.Text(self.frame_output, height=10, width=40)
        self.text_nota.grid(row=1, column=0, columnspan=2)

        # Tombol selesai
        tk.Button(self.frame_output, text="Selesai", command=self.pesanan_selesai).grid(row=2, column=0, columnspan=2, pady=10)

    def tambah_produk(self):
        produk_terpilih = self.combo_produk.get()
        jumlah = self.entry_jumlah.get()
        metode_pembayaran = self.combo_pembayaran.get()

        if jumlah and jumlah.isdigit():
            harga = next((produk["harga"] for produk in self.menu_produk if produk["nama"] == produk_terpilih), None)
            total_harga = float(harga) * int(jumlah)

            self.transaksi.append((produk_terpilih, harga, jumlah, total_harga, metode_pembayaran))
            self.update_nota()
            self.entry_jumlah.delete(0, tk.END)

    def update_nota(self):
        self.text_nota.delete(1.0, tk.END)
        total_pembelian = 0

        for produk, harga, jumlah, total_harga, metode_pembayaran in self.transaksi:
            self.text_nota.insert(tk.END, f"{produk} ({harga} per item) x {jumlah}: {total_harga:.2f} - {metode_pembayaran}\n")
            total_pembelian += total_harga

        self.text_nota.insert(tk.END, "\nTotal Pembelian: {:.2f}".format(total_pembelian))

    def pesanan_selesai(self):
        if not self.transaksi:
            messagebox.showinfo("Pesanan Selesai", "Anda belum menambahkan produk.")
        else:
            self.update_nota()
            total_pembelian = sum(item[3] for item in self.transaksi)
            metode_pembayaran = self.transaksi[-1][4]  # Mengambil metode pembayaran dari transaksi terakhir
            messagebox.showinfo("Pesanan Selesai", f"Pesanan selesai! Total pembelian: {total_pembelian:.2f}\nMetode Pembayaran: {metode_pembayaran}")

            with open("nota_pembelian.txt", "w") as file:
                file.write("Nota Transaksi\n")
                for produk, harga, jumlah, total_harga, metode_pembayaran in self.transaksi:
                    file.write(f"{produk} ({harga} per item) x {jumlah}: {total_harga:.2f} - {metode_pembayaran}\n")
                file.write("\nTotal Pembelian: {:.2f}".format(total_pembelian))

            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TokoEbookApp(root)
    root.mainloop()
