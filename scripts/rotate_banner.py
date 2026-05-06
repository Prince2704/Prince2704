from datetime import datetime
from pathlib import Path
import re

README_PATH = Path("README.md")

BANNERS = [
    "./assets/banner-1.svg",
    "./assets/banner-2.svg",
    "./assets/banner-3.svg",
]

def main():
    readme = README_PATH.read_text(encoding="utf-8")

    day_number = datetime.utcnow().toordinal()
    selected_banner = BANNERS[day_number % len(BANNERS)]

    new_banner_block = f"""<!-- BANNER_START -->
<p align="center">
  <img src="{selected_banner}" width="100%" alt="Prince Raj Developer Banner" />
</p>
<!-- BANNER_END -->"""

    updated_readme = re.sub(
        r"<!-- BANNER_START -->.*?<!-- BANNER_END -->",
        new_banner_block,
        readme,
        flags=re.DOTALL,
    )

    README_PATH.write_text(updated_readme, encoding="utf-8")

if __name__ == "__main__":
    main()
