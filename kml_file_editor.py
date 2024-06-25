import re

def edit_kml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace <altitudeMode> with <gx:altitudeMode>clampToSeaFloor</gx:altitudeMode>
    content = re.sub(r'<altitudeMode>.*?</altitudeMode>', r'<gx:altitudeMode>clampToSeaFloor</gx:altitudeMode>', content)
    
    # Add <name> if it is missing
    placemarks = re.findall(r'(<Placemark>.*?</Placemark>)', content, re.DOTALL)
    updated_placemarks = []
    for placemark in placemarks:
        if '<name>' not in placemark:
            description_match = re.search(r'<description>(.*?)</description>', placemark)
            if description_match:
                description = description_match.group(1)
                placemark = placemark.replace('<description>', f'<name>{description}</name>\n\t\t\t<description>', 1)
        updated_placemarks.append(placemark)
    
    # Replace old placemarks with updated ones
    for old, new in zip(placemarks, updated_placemarks):
        content = content.replace(old, new)
    
    # Add <width>5</width> to <LineStyle> if it is missing
    line_styles = re.findall(r'(<LineStyle>.*?</LineStyle>)', content, re.DOTALL)
    updated_line_styles = []
    for line_style in line_styles:
        if '<width>' not in line_style:
            line_style = line_style.replace('</LineStyle>', '\t\t\t<width>5</width>\n\t\t</LineStyle>')
        updated_line_styles.append(line_style)
    
    # Replace old line styles with updated ones
    for old, new in zip(line_styles, updated_line_styles):
        content = content.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Path to the KML file
file_path = r"C:\Users\samir\OneDrive\Masaüstü\PY\1.kml"
edit_kml(file_path)
