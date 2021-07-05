class DecimalToBinary(object):
    def __init__(self, num_seq="255.255.255.255"):
        self.num_seq = num_seq
        try:
            self.num_list = num_seq.split(".")
        except:
            self.num_list = num_seq
        
        
    def __str__(self):
        return str(self.convertion())
    
    
    def __repr__(self):
        return repr("This object takes in a number sequence, splits it into parts, and converts it into binary notation.")
    
    
    def convertion(self):
        binary_notation = ""
        for num in self.num_list:
            binary_notation += str("{0:08b}.".format(int(num)))
        last_dot = binary_notation[-1]
        return binary_notation.strip(last_dot)
    

if __name__ == "__main__":
    num_seq = DecimalToBinary("127.192.168.1")
    print(f"Passed number sequence:  {num_seq}\n"
          f"Default number sequence: {DecimalToBinary()}\n"
          f"Object description:      {repr(DecimalToBinary())}")
