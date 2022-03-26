# Function to find the HCF/GCD using the Euclidian algorithm

def main():
    
    def compute_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x

    num1 = 300
    num2 = 400
    
    hcf = compute_hcf(num1, num2)
    
    print("\nThe HCF is of", num1, "and", num2, "is", hcf, "\n")
    
if __name__ == "__main__":
    main()