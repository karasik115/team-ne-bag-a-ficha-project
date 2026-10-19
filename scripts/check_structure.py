"""Проверка структуры учебного репозитория."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    "README.md", ".gitignore", "docs/team-contract.md",
    "docs/roles-and-responsibilities.md", "docs/raci-matrix.md", "scripts/",
]
for number in range(1, 9):
    base = f"practical-works/practical-work-{number:02d}"
    expected.append(f"{base}/report.md")
    expected.append(f"{base}/{'assets' if number <= 3 else 'src'}/")

missing = [path for path in expected if not (root / path).exists()]
if missing:
    print("Отсутствуют пути:")
    print("\n".join(missing))
    sys.exit(1)
print("Структура репозитория соответствует образцу: работы 01–08 и документы команды.")
