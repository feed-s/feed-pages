import os
import json
import xml.etree.ElementTree as ET

# 定义输入和输出目录
input_dir = './test/szclsya.xml'
output_file = 'merged_feed.xml'

# 创建 RSS 根元素
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

# 遍历输入目录中的所有 JSON 文件
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # 创建 item 元素
            item = ET.SubElement(channel, "item")
            ET.SubElement(item, "title").text = data.get("title", "")
            ET.SubElement(item, "link").text = data.get("url", "")
            ET.SubElement(item, "description").text = data.get("description", "")
            ET.SubElement(item, "pubDate").text = data.get("published", "")
            ET.SubElement(item, "author").text = data.get("author", "")

# 将合并后的 RSS 写入文件
tree = ET.ElementTree(rss)
tree.write(output_file, encoding='utf-8', xml_declaration=True)

print(f"RSS feed merged into {output_file}")
