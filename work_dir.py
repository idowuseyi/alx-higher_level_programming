from pathlib import Path

# Absolute path
# c:\Program Filee\Microsoft
# /usr/local/bin
# Relative path
path = Path()
#print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)