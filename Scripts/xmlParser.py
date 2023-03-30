import xml.etree.ElementTree as ET

def filter_urls_above_priority(filename, priority_threshold):
    output_filename = filename[0:-4] + '.txt'
    # Define the namespace
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Find all URL nodes with a priority above the threshold
    urls_above_priority = []
    for url in root.findall('s:url', ns):
        priority = float(url.find('s:priority', ns).text)
        if priority >= priority_threshold:
            loc = url.find('s:loc', ns).text
            urls_above_priority.append(loc)
    
    # Write the filtered URLs to a text file
    with open(output_filename, 'w') as f:
        for url in urls_above_priority:
            f.write(url + '\n')

filter_urls_above_priority('moib.gov.pk.xml', 0.8)