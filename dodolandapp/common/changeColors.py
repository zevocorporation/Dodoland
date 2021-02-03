import xml.etree.ElementTree as ET


def changeColors(template, baseColor, highlightColor,accentColor):
    for elem in template.iter():
        attributes = elem.attrib
        if 'fill' in attributes:
            if attributes['fill'] == '#898989':
                elem.set('fill', baseColor)
            elif attributes['fill'] == '#5B5B5B':
                elem.set('fill', highlightColor)
            elif attributes['fill'] == '#0C0C0C':
                elem.set('fill', accentColor)
            elif attributes['fill'] == '#D8D8D8':
                elem.set('fill', highlightColor)
            elif attributes['fill'] == '#B7B7B7':
                elem.set('fill', accentColor)
            elif attributes['fill'] == '#6D6D6D':
                elem.set('fill', highlightColor)

    return template
