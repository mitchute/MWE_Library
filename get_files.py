import os


basename = os.path.basename
join = os.path.join
dirname = os.path.dirname

here = dirname(__file__)
mwe_pkg_dir = join(here, "mwe_lib")

include_file_exts = [".py", ".rb", ".csv"]
exclude_files = ["dont-include.xml"]

lib_files = []

for root, dirs, files in os.walk(mwe_pkg_dir):
    for f in files:
        f_name = os.path.basename(f)
        ext = os.path.splitext(f)[1]
        if ext in include_file_exts and f_name not in exclude_files:
            full_path = join(root, f)
            f_path = full_path.split(here)[1]
            lib_files.append(f_path)

print(lib_files)
