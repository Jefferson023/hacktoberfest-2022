def compute_wage(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * rate * 1.5

if __name__ == "__main__":
    hours = float(input())
    rate = float(input())
    print(f"Salario: {compute_wage(hours, rate):.2f}")