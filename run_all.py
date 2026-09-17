from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for nb in sorted((root/"notebooks").glob("*.ipynb")):
    print("Executing",nb.name)
    subprocess.run([sys.executable,"-m","jupyter","nbconvert","--to","notebook","--execute",
                    "--ExecutePreprocessor.timeout=600","--inplace",str(nb)],cwd=root,check=True)
print("Complete.")
