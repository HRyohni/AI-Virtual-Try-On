from Tools.i18n.msgfmt import generate
from google import genai
from google.genai import types
from PIL import Image
import time
from io import BytesIO

from traitlets.config.loader import ConfigLoader

client = genai.Client(api_key='your api key')


def export_image(response, exportName, showImage=False):
    try:
        image_parts = [
            part.inline_data.data
            for part in response.candidates[0].content.parts
            if part.inline_data
        ]
        if image_parts:
            image = Image.open(BytesIO(image_parts[0]))
            image.save(exportName)
            print(f"✅ Successfully saved image to {exportName}")
            if showImage:
                image.show()
        else:
            print("❌ No image data found in the response.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("--- Full Response ---")
        print(response)

# --- Main Logic ---

try:
    # model is a person who you want to dress
    model_image = Image.open('model.png')
    # This image contains the person wearing the complete outfit you want to transfer to *model*
    outfit_image = Image.open('clothing_image3.png')
except FileNotFoundError as e:
    print(f"Error: Make sure the image file '{e.filename}' exists.")
    exit()

# Image 1 -> model_image
# Image 2 -> outfit_image
# you can change your prompt
comprehensive_prompt = """
Create a single, realistic, full-body e-commerce fashion photograph.

**Goal:** Take the **entire outfit** (shirt, pants, and shoes) worn by the person in the **second image** and realistically place it on the person from the **first image**.

**Instructions:**
- The person from the first image is the final model.
- The clothing from the second image should be seamlessly transferred to the final model.
- Ensure the complete outfit fits the final model's body and pose naturally.
- The final image must be cohesive, with consistent lighting, shadows, and textures.
"""

print("🚀Generating image with the complete outfit🚀")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[model_image, outfit_image, comprehensive_prompt],
)

# name your output file
export_image(response, "model_with_transferred_outfit 3.png", showImage=True)