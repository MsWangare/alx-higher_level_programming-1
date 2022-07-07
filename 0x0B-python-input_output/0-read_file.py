def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        txtfile = f.read()
        print(txtfile)
