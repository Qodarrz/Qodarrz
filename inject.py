import re

def patch_svg(filename, ascii_lines):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Calculate dynamic font size and spacing based on total lines
    total_lines = len(ascii_lines)
    max_height = 500.0 # max pixel height available in SVG
    line_spacing = max_height / max(total_lines, 1)
    font_size = line_spacing * 0.85 # scale font size slightly smaller than spacing

    if 'dark_mode' in filename:
        text_color = '#ffffff'
    else:
        text_color = '#000000'

    # Create new ascii text block
    new_ascii = f'''<text x="15" y="30" fill="{text_color}" class="ascii" style="font-size: {font_size:.2f}px; font-family: monospace; letter-spacing: 0px;">\n'''
    
    # We use dy to relative position each line, which is much easier
    for i, line in enumerate(ascii_lines):
        line = line.rstrip('\n')
        # escape xml
        line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        if not line.strip():
            line = ' ' # ensure empty lines still take up space
            
        svg_total_height = 680.0
        bottom_margin = 20.0
        start_y = svg_total_height - max_height - bottom_margin
        
        y_pos = start_y + (i * line_spacing)
        new_ascii += f'<tspan x="15" y="{y_pos:.2f}">{line}</tspan>\n'
        
    new_ascii += '</text>'

    # regex replace the old ascii block
    pattern = re.compile(r'<text[^>]*class="ascii"[^>]*>.*?</text>', re.DOTALL)
    
    # Clean up any leftover gradient defs
    content = re.sub(r'<defs>\s*<linearGradient id="asciiGradient".*?</defs>\s*', '', content, flags=re.DOTALL)
    
    new_content = pattern.sub(lambda m: new_ascii, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched {filename}")

if __name__ == '__main__':
    try:
        with open('ascii.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Ensure there are lines
        if not lines:
            print("Error: ascii.txt is empty! Make sure you saved the file.")
        else:
            patch_svg('dark_mode.svg', lines)
            patch_svg('light_mode.svg', lines)
            print("Successfully injected the new ASCII art!")
    except FileNotFoundError:
        print("Error: ascii.txt not found!")
