from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def test_image(name="test.jpg", size=(250, 250)):
    img = Image.new("RGB", size)
    content = img.tobytes()
    return SimpleUploadedFile(name, content=content, content_type="image/jpeg")
