def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius): 
    return celsius + 273.15

if __name__ == "__main__":
    celsius = float(input("ป้อนอุณหภูมิ (องศาเซลเซียส): "))

    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print(f"{celsius:.2f} องศาเซลเซียส เท่ากับ {fahrenheit:.2f} องศาฟาเรนไฮต์")
    print(f"{celsius:.2f} องศาเซลเซียส เท่ากับ {kelvin:.2f} เคลวิน")
