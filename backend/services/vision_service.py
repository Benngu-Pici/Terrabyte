import base64
import io
from PIL import Image
from config.openai_config import client

SYSTEM_PROMPT = """
Bạn là chuyên gia nông nghiệp.
Chỉ trả lời về cây trồng, bệnh cây,
tưới nước, ánh sáng, dinh dưỡng.
Trả lời ngắn, rõ ràng, dễ hiểu.
"""

def handle_vision_chat(message, image_file=None):

    content = []

    if message:
        content.append({
            "type": "text",
            "text": message
        })

    if image_file:
        img = Image.open(image_file)
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{img_base64}"
            }
        })

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # 👁️ CÓ THỊ GIÁC
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content}
        ],
        max_tokens=400
    )

    return response.choices[0].message.content
