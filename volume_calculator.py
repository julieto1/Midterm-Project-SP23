
import math



def volume_cone():
    
    radius_cone = float(input('Please enter the radius of the cone: '))
    height_cone = float(input('Please enter the height of the cone: '))

    result = (1/3) * math.pi * (radius_cone**2) * height_cone

    return result


def volume_cyl():

    radius_cyl = float(input('Please enter the radius of the cylinder: '))
    height_cyl = float(input('Please enter the height of the cylinder: '))

    result = math.pi * (radius_cyl**2) * height_cyl

    return result


def volume_cube():

    length_cube = float(input('Please enter the length of one side of the cube: '))

    result = length_cube**3

    return result


    
print('Choose an option below:')
print('1. Find the volume of a cone')
print('2. Find the volume of a cylinder')
print('3. Find the volume of a cube')
print()
user_choice = input('Enter your menu choice: ')

if (user_choice == "1"):
    total = volume_cone()
elif(user_choice == "2"):
    total = volume_cyl()
elif(user_choice == "3"):
    total = volume_cube()
else:
    print('Error: You entered a bad value. Goodbye!')
    exit()

print()
print('The volume is: ' + str(total))


