# KML File Editor

This Python script was created to help speed up my work with KML files. When converting DWG files to KML, certain elements like width and names are sometimes missing. This script addresses those issues by adding missing names, setting a default width, and ensuring the altitude mode is optimized for better appearance in Google Earth Pro.

## Features

- **Add Missing Names**: If a `<Placemark>` section is missing a `<name>` tag, the script will copy the text from the `<description>` tag and create a `<name>` tag with that text.
- **Set Default Width**: If a `<LineStyle>` section is missing a `<width>` tag, the script will add `<width>5</width>` by default. You can easily modify the script to change the width value.
- **Optimize Altitude Mode**: The script replaces all `<altitudeMode>` tags with `<gx:altitudeMode>clampToSeaFloor</gx:altitudeMode>` for better visualization in Google Earth Pro.

## Usage

1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Download the Script**: Save the script to a file, for example, `kml_file_editor.py`.

3. **Prepare Your KML File**: Place the KML file you want to edit in a convenient location. Update the file path in the script accordingly.

4. **Run the Script**:
   ```bash
   python kml_file_editor
   
5. ** Modify Width (Optional)**: If you want to change the default width from 5 to something else, update the following line in the script:
line_style = line_style.replace('</LineStyle>', '\t\t\t<width>5</width>\n\t\t</LineStyle>')

## Example

   Here is an example of a <Placemark> section before and after running the script:

  **Before**:
   <Placemark>
    <description>some words here</description>
    <styleUrl>#line5</styleUrl>
    <LineString>
        <altitudeMode>relativeToGround</altitudeMode>
        <coordinates>
            49.665284396,40.593550807,0 49.66682482900001,40.591403898,0
        </coordinates>
    </LineString>
</Placemark>

  **After:**
<Placemark>
    <name>some words herex</name>
    <description>some words herex</description>
    <styleUrl>#line5</styleUrl>
    <LineString>
        <gx:altitudeMode>clampToSeaFloor</gx:altitudeMode>
        <coordinates>
            49.665284396,40.593550807,0 49.66682482900001,40.591403898,0
        </coordinates>
    </LineString>
</Placemark>

## Feel Free to Contribute

Feel free to add any additional features or improvements to the script. Your contributions are welcome!
