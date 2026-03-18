# AI-Powered 2D → Cartoon Converter

Uses **free** Hugging Face Inference API models to convert any photo into cartoon-style artwork via AI image generation.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a free Hugging Face token
1. Sign up at https://huggingface.co (free)
2. Go to https://huggingface.co/settings/tokens
3. Create a token (Read access is enough)

### 3. Set the token
```bash
export HF_TOKEN=hf_your_token_here
```

---

## Usage

### Command Line

```bash
# Standard cartoon style
python cartoon_converter.py photo.jpg cartoon.png

# Studio Ghibli / anime aesthetic
python cartoon_converter.py photo.jpg ghibli.png --style ghibli

# Comic-book ink style
python cartoon_converter.py photo.jpg comic.png --style comic

# Direct cartoon look
python cartoon_converter.py photo.jpg out.png --style cartoon

# Custom prompt
python cartoon_converter.py photo.jpg out.png --prompt "watercolor illustration, soft pastels"
```

### Python API

```python
from cartoon_converter import convert_image

# Simple
convert_image("photo.jpg", "cartoon.png")

# With style
convert_image("photo.jpg", "ghibli.png", style="ghibli")

# Full control
convert_image(
    "photo.jpg",
    "output.png",
    style="comic",
    guidance_scale=8.5,
    steps=30,
    image_guidance=1.2,
)
```

---

## Styles

| Style      | Model                             | Description                              |
|------------|-----------------------------------|------------------------------------------|
| `standard` | timbrooks/instruct-pix2pix        | Instruction-based img2img, best quality  |
| `cartoon`  | Falconsai/cartoon_image_generator | Direct cartoon diffusion                 |
| `ghibli`   | nitrosocke/Ghibli-Diffusion       | Studio Ghibli / anime watercolor         |
| `comic`    | ogkalu/comic-diffusion            | Comic book ink and halftone style        |

## Parameters

| Parameter        | Default | Description                                    |
|------------------|---------|------------------------------------------------|
| `--style`        | standard| Style preset (see table above)                 |
| `--prompt`       | —       | Custom prompt, overrides style default         |
| `--max-size`     | 512     | Resize longest edge before upload              |
| `--image-guidance` | 1.5   | How strongly to follow input image (img2img)   |
| `--guidance-scale` | 7.5   | How strongly to follow the prompt              |
| `--steps`        | 20      | Diffusion steps (more = better, slower)        |

## Notes

- **Free tier**: HF Inference API is free but rate-limited. Models may take 20–60s to warm up on first call — retries are automatic.
- **Image size**: Images are auto-resized to 512px max before upload to stay within API limits.
- **No GPU needed**: Everything runs on HF's servers.
