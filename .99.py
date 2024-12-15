
import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    
        base = float(input("ป้อนความยาวฐาน: "))
        height = float(input("ป้อนความสูง: "))
        area = calculate_triangle_area(base, height)
        print(f"พื้นที่ของสามเหลี่ยมคือ: {area:.2f}")

    
   
    
