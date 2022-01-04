For Windows MSVC: 
  Put the .natvis in (for example)
  ```
    %USERPROFILE%\Documents\Visual Studio 2019\Visualizers
  ```

For Windows MinGW / macOS / Linux:
  Add the following lines (for example) to your ~/.lldbinit (create one if does not exist):
  ```
    command script import ~/lldb/ProtobufFormatters.py
    command source ~/lldb/ProtobufFormatters.lldb
  ```
