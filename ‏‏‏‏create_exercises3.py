import os
import random
from PIL import Image

# Paths to folders containing images of each digit and operator
digits_folders = {
    '0': 'archive (3)/0',
    '1': 'archive (3)/1',
    '2': 'archive (3)/2',
    '3': 'archive (3)/3',
    '4': 'archive (3)/4',
    '5': 'archive (3)/5',
    '6': 'archive (3)/6',
    '7': 'archive (3)/7',
    '8': 'archive (3)/8',
    '9': 'archive (3)/9'
}

operators_folders = {
    '+': 'archive (3)/add',
    '-': 'archive (3)/sub',
    '*': 'archive (3)/mul',
    '/': 'archive (3)/div',
    '=': 'archive (3)/eq'
}

output_folder = 'math_exercises3'
uniform_size = (400, 500)  # Define the uniform size for all images

# Load a random image from a folder and resize it
def load_random_image(folder):
    images = [file for file in os.listdir(folder) if file.endswith('.png') or file.endswith('.jpg')]
    if not images:
        return None
    random_image = random.choice(images)
    img = Image.open(os.path.join(folder, random_image))
    img = img.resize(uniform_size, Image.LANCZOS)  # Resize image to uniform size
    return img

# Generate a random math expression
def generate_expression():
    length = random.randint(3, 15)
    expression = ""
    
    while True:
        expression = ""
        num_length = 0
        has_operator = False
        last_char_was_operator = False
        
        while num_length < length:
            if last_char_was_operator or len(expression) == 0:
                digit_length = random.randint(1, min(3, length - num_length))
                if digit_length == 1:
                    digit = random.choice('123456789')
                else:
                    digit = random.choice('123456789')
                    for _ in range(digit_length - 1):
                        digit += random.choice('0123456789')
                expression += digit
                num_length += digit_length
                last_char_was_operator = False
            else:
                if num_length < length - 1:
                    operator = random.choice('+-*/')
                    expression += operator
                    num_length += 1
                    last_char_was_operator = True
                    has_operator = True
                else:
                    break
        
        if has_operator and not last_char_was_operator:
            break

    return expression + '='

# Create a new image by combining images of digits and operators
def create_expression_image(expression):
    images = []
    for char in expression:
        if char.isdigit():
            images.append(load_random_image(digits_folders[char]))
        elif char in operators_folders:
            images.append(load_random_image(operators_folders[char]))
    
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    
    new_image = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for img in images:
        new_image.paste(img, (x_offset, 0))
        x_offset += img.width
    
    return new_image

def save_expression_image(image, expression, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    safe_expression = expression.replace('/', 'div').replace('*', 'mul').replace('+', 'add').replace('-', 'sub').replace('=', 'eq')
    image.save(os.path.join(output_folder, safe_expression + '.png'))

# Main function
def main():
    for _ in range(500):  # Generate 500 expressions
        expression = generate_expression()
        image = create_expression_image(expression)
        save_expression_image(image, expression, output_folder)
        print(f"Generated: {expression}")

if __name__ == "__main__":
    main()
