import os

files_list = os.listdir('GIS_COURSES/PRG_jednostki_administracyjne_2023')

for file in files_list:
    if file.endswith('shp'):
        layer_name = file.split('.')[0]
        layer = iface.addVectorLayer(f'GIS_COURSES/PRG_jednostki_administracyjne_2023/{file}', layer_name, 'ogr')
        
uri = QgsDataSourceUri()
uri.setConnection('localhost', '5432', 'PGR', 'postgres', 'postgres')

objects = ['gminy', 'jedew', 'obreby', 'panstwo', 'powiaty', 'woj']

for object in objects:
    uri.setDataSource('public', object, 'geom')
    vlayer = QgsVectorLayer(uri.uri(), object, 'postgres')
    QgsProject.instance().addMapLayers([vlayer])
