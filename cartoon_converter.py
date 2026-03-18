import sys, argparse
from pathlib import Path
from PIL import Image

def convert_image(input_path, output_path, version="v2", size=512):
    import torch
    input_path  = Path(input_path)
    output_path = Path(output_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")
    print(f"Input   : {input_path}")
    print(f"Version : AnimeGANv2 {version}")
    image = Image.open(input_path).convert("RGB")
    print(f"Image   : {image.width}x{image.height}")
    print("Loading AnimeGANv2 model (downloading ~50MB on first run)...")
    model = torch.hub.load(
        "AK391/animegan2-pytorch:main", "generator",
        pretrained=("face_paint_512_v1" if version=="v1" else True),
        progress=True, verbose=False,
    )
    face2paint = torch.hub.load(
        "AK391/animegan2-pytorch:main", "face2paint",
        size=size, side_by_side=False, verbose=False,
    )
    print("Cartoonifying...")
    with torch.no_grad():
        result = face2paint(model, image)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(str(output_path))
    print(f"Cartoon saved -> {output_path}  ({result.width}x{result.height})")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--version", choices=["v1","v2"], default="v2")
    p.add_argument("--size", type=int, default=512)
    a = p.parse_args()
    try:
        convert_image(a.input, a.output, a.version, a.size)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)
    except ImportError:
        print("Error: Run: pip install torch torchvision", file=sys.stderr); sys.exit(1)
