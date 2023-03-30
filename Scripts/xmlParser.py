import xml.etree.ElementTree as ET

def filter_urls_above_priority(filename, priority_threshold):
    output_filename = filename[0:-4] + '.txt'
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    urls_above_priority = []
    for url in root.findall('s:url', ns):
        priority = float(url.find('s:priority', ns).text)
        if priority >= priority_threshold:
            loc = url.find('s:loc', ns).text
            urls_above_priority.append(loc)
    
    with open(output_filename, 'w') as f:
        for url in urls_above_priority:
            f.write(url + '\n')

filter_urls_above_priority('sites\mocc.gov.pk.xml', 0.8)