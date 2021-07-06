class HexToDecimal(object):
    def __init__(self, hex_string="ff.ff.ff.ff"):
        self.hex_string = hex_string
        try:
            self.hex_list = hex_string.split(".")
        except:
            self.hex_list = hex_string
        
        
    def __str__(self):
        return str(self.convertion())
    
    
    def __repr__(self):
        return repr("This object takes in a hexadecimal-string, splits it into bytes, and converts it into decimal notation.")
    
    
    def convertion(self):
        decimal_notation = ""
        for hexa in self.hex_list:
            decimal_notation += str(int(hexa, 16)) + "."
        last_dot = decimal_notation[-1]
        return decimal_notation.strip(last_dot)
    

if __name__ == "__main__":
    hex_string = HexToDecimal("7f.c0.a8.1")
    print(f"Passed hex-string:  {hex_string}\n"
          f"Default hex-string: {HexToDecimal()}\n"
          f"Object description: {repr(HexToDecimal())}")
