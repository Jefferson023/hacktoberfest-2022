def weighted_mean(n1:float, n2:float, n3:float)->float:
    return (n1*2 + n2*3 + n3*5)/10

if __name__ == "__main__":
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    print(f"Media ponderada: {weighted_mean(n1, n2, n3):.1f}")
    