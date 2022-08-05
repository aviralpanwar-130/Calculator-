from cx_Freeze import *

includefiles = ['calculator.ico']
base = "Win32GUI"


shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Directory_
     "Calculator", # Name
     "TARGETDIR", # Component_
     "[TARGETDIR]\calculator.exe", # Target
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #IconINdex
     None, #ShowCmd
     "TARGETDIR", #WkDir
      )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined table

bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Calculator",
    author="Aviral Panwar",
    name="AMD Calculator",
    options={'build_exe':{'include_files': includefiles},"bdist_msi": bdist_msi_options,},
    executables=[
        Executable(
            script="calculator.py",
            base=base,
            icon='calculator.ico',
        )
    ]
)