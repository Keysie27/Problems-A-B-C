class Triangle:
    @staticmethod
    def next_edge(side1, side2):
        return (side1 + side2) - 1

def main():

    print(Triangle.next_edge(8, 10))  
    print(Triangle.next_edge(5, 7))   
    print(Triangle.next_edge(9, 2))   

if __name__ == "__main__":
    main()
