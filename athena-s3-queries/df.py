import pandas as pd
import xml.etree.ElementTree as ET

# XMLデータを解析
tree = ET.parse('data.xml')
root = tree.getroot()

# XMLデータをPythonのデータ構造に変換
data_list = []
for item in root.findall('item'):  # 'item'はXML内の要素名に置き換えてください
    data = {}
    data['field1'] = item.find('field1').text  # 'field1'はXML内の要素名に置き換えてください
    data['field2'] = item.find('field2').text  # 'field2'はXML内の要素名に置き換えてください
    data_list.append(data)

# Pythonデータ構造をPandasデータフレームに変換
df = pd.DataFrame(data_list)

# データフレームをCSVにエクスポート
df.to_csv('data.csv', index=False)
