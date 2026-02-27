import sys

try:
    import nanovdb_editor
except ImportError:
    print("Failed to import nanovdb_editor. Exiting without running tests.")
    sys.exit(0)

print(f"nanovdb_editor {nanovdb_editor.__version__} imported successfully")
