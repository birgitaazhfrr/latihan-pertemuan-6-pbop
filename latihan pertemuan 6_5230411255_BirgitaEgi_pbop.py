
class Order:
    def __init__(self, Id, nama_skincare, informasi_produk):
        self.Id = Id
        self.nama_skincare = nama_skincare
        self.informasi_produk = informasi_produk

    def set_order(self):
        print(f"Order : {self.Id}, nama_skincare: {self.nama_skincare}, informasi_produk: {self.informasi_produk}")


class Delivery:
    def __init__(self, Id, nama_produk, informasi_skincare, date, address):
        self.Id = Id
        self.nama_produk = nama_produk
        self.informasi_skincare = informasi_skincare
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"Process delivery: {self.Id}, nama_produk: {self.nama_produk}, informasi_skincare: {self.informasi_skincare}, date: {self.date}, address: {self.address}")


order1 = Order(1, "SKINTIFIC", "SERUM")
order2 = Order(2, "SK II", "MOIST")
order3 = Order(3, "CAMILLE", "CUSHION")
order1.set_order()
order2.set_order()
order3.set_order()

delivery1 = Delivery(1, "CLAYMASK", "SKINTIFIC", "2021-12-21", "Jl.kapan kapan")
delivery2 = Delivery(2, "LIPSERUM", "OMG", "2021-12-21", "Jl.hahahaha")
delivery3 = Delivery(3, "MASCARA", "MAYBELINE", "2021-12-21", "Jl.wkwkwk")
delivery1.process_delivery()
delivery2.process_delivery()
delivery3.process_delivery()