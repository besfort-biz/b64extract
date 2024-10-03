import re
import base64
import os

# Define the base path where to save extracted files
output_dir = "assets"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the input HTML file
input_html_file = "index.html"
with open(input_html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Regular expression to match base64 data URIs including webp
# Matches: data:[mime-type];base64,[data]
base64_regex = re.compile(r'data:(image|font|application)/(png|jpeg|jpg|gif|svg\+xml|webp|woff|woff2|ttf|otf);base64,([a-zA-Z0-9+/=]+)')

# Keep track of the number of found assets
asset_count = 1

# Find all matches in the HTML content
for match in base64_regex.finditer(html_content):
    asset_type = match.group(1)  # image or font
    asset_format = match.group(2)  # png, jpg, gif, svg, webp, etc.
    base64_data = match.group(3)  # base64 content

    # Generate a filename for the asset
    filename = f"{asset_type}_{asset_count}.{asset_format}"
    file_path = os.path.join(output_dir, filename)

    # Save the decoded base64 data into the appropriate file
    with open(file_path, "wb") as asset_file:
        asset_file.write(base64.b64decode(base64_data))

    # Replace the base64 data URI in the HTML content with the new file reference
    html_content = html_content.replace(match.group(0), f"{filename}")

    print(f"Extracted {filename} from base64 data and replaced it in the HTML.")

    # Increment the asset count for unique filenames
    asset_count += 1

# Save the modified HTML content back to a file
output_html_file = "cleaned_index.html"
with open(output_html_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Modified HTML file saved as {output_html_file}.")
