# Add package to path to allow for imports inside modules
from pathlib import Path
import sys
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(parent))
del Path, sys
