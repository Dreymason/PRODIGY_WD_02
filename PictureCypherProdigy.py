# First we need to import from pillow after installation
from PIL import Image

# Function to encrypt an image using pixel manipulation
def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    # This will convert the image to RGB mode (in case it is not)
    img = img.convert("RGB")
    # Get the pixel data
    pixels = img.load()

    # Image encryption by modifying the RGB values
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Apply the encryption formula: shift each color value by the key
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image using pixel manipulation
def decrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    # Decrypt the image by reversing the RGB value shift
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Apply the decryption formula: shift each color value by -key
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to handle user input and perform encryption/decryption
def image_cipher():
    print("Image Encryption and Decryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
        return

    image_path = input("Enter the image file path: ")
    output_path = input("Enter the output file path: ")
    key = int(input("Enter the key (numeric shift value): "))

    if choice == 'E':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

# Run the program
if __name__ == "__main__":
    image_cipher()
