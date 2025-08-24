import shutil
import os

def copy_static(src, dst):
    # 2. If the destination directory doesn't exist, create it
    if not os.path.exists(dst):
        os.makedirs(dst)
        print(f"{dst} created as an empty directory.")
    # 3. Loop through everything in the source directory (src)
    for entry in os.listdir(src):
        src_full_path = os.path.join(src, entry)
        # 4. If the item is a file, copy it to the destination
        if os.path.isfile(src_full_path):
            shutil.copy(src_full_path, dst)
            # 6. Optionally: log/print the path of each file you copy for debugging
            print(f"file '{src_full_path}' copied into {dst}")
        # 5. If the item is a directory, call this function again (recursively) for that directory
        elif os.path.isdir(src_full_path):
            dst_subdir = os.path.join(dst, entry)
            copy_static(src_full_path, dst_subdir)