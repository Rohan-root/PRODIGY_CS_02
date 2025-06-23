from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGBA")  
    pixels = img.load()

    for i in range(img.size[0]): 
        for j in range(img.size[1]):  
            r, g, b, a = pixels[i, j]

            new_r = (r ^ (key + i + j)) % 256
            new_g = (g ^ (key + i + j)) % 256
            new_b = (b ^ (key + i + j)) % 256

            pixels[i, j] = (new_r, new_g, new_b, a)

    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)

print("Image Encryption Tool")
choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().lower()
input_path = input("Enter the path to the image: ")
output_path = input("Enter the output path for the result (with extension): ")
key = int(input("Enter the encryption key (integer 0-255): "))

if choice == 'e':
    encrypt_image(input_path, output_path, key)
elif choice == 'd':
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid choice. Please enter 'E' or 'D'.")
