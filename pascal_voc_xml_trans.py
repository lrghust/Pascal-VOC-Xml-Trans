import xml.dom.minidom

def pascal_voc_xml_trans(\
xml_filename,\
folder,\
filename,\
source_database,\
source_annotation,\
source_image,\
width,\
height,\
depth,\
segmented,\
name,\
pose,\
truncated,\
difficult,\
xmin,\
ymin,\
xmax,\
ymax
):
    # root
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'annotation', None)
    node_annotation = dom.documentElement
    # folder
    node_folder = dom.createElement('folder')
    text_folder = dom.createTextNode(folder)
    node_folder.appendChild(text_folder)
    node_annotation.appendChild(node_folder)
    # filename
    node_filename = dom.createElement('filename')
    text_filename=dom.createTextNode(filename)
    node_filename.appendChild(text_filename)
    node_annotation.appendChild(node_filename)
    # source
    node_source=dom.createElement('source')
    node_source_database=dom.createElement('database')
    text_source_database=dom.createTextNode(source_database)
    node_source_database.appendChild(text_source_database)
    node_source_annotation=dom.createElement('annotation')
    text_source_annotation=dom.createTextNode(source_annotation)
    node_source_annotation.appendChild(text_source_annotation)
    node_source_image=dom.createElement('image')
    text_source_image=dom.createTextNode(source_image)
    node_source_image.appendChild(text_source_image)
    node_source.appendChild(node_source_database)
    node_source.appendChild(node_source_annotation)
    node_source.appendChild(node_source_image)
    node_annotation.appendChild(node_source)
    # size
    node_size=dom.createElement('size')
    node_size_width=dom.createElement('width')
    text_size_width=dom.createTextNode(width)
    node_size_width.appendChild(text_size_width)
    node_size_height=dom.createElement('height')
    text_size_height=dom.createTextNode(height)
    node_size_height.appendChild(text_size_height)
    node_size_depth=dom.createElement('depth')
    text_size_depth=dom.createTextNode(depth)
    node_size_depth.appendChild(text_size_depth)
    node_size.appendChild(node_size_width)
    node_size.appendChild(node_size_height)
    node_size.appendChild(node_size_depth)
    node_annotation.appendChild(node_size)
    # segmented
    node_segmented=dom.createElement('segmented')
    text_segmented=dom.createTextNode(segmented)
    node_segmented.appendChild(text_segmented)
    node_annotation.appendChild(node_segmented)
    # object
    node_object=dom.createElement('object')
    node_object_name=dom.createElement('name')
    text_object_name=dom.createTextNode(name)
    node_object_name.appendChild(text_object_name)
    node_object_pose=dom.createElement('pose')
    text_object_pose=dom.createTextNode(pose)
    node_object_pose.appendChild(text_object_pose)
    node_object_truncated=dom.createElement('truncated')
    text_object_truncated=dom.createTextNode(truncated)
    node_object_truncated.appendChild(text_object_truncated)
    node_object_difficult=dom.createElement('difficult')
    text_object_difficult=dom.createTextNode(difficult)
    node_object_difficult.appendChild(text_object_difficult)
    # object-bndbox
    node_object_bndbox=dom.createElement('bndbox')
    node_object_bndbox_xmin=dom.createElement('xmin')
    node_object_bndbox_ymin=dom.createElement('ymin')
    node_object_bndbox_xmax=dom.createElement('xmax')
    node_object_bndbox_ymax=dom.createElement('ymax')
    text_object_bndbox_xmin=dom.createTextNode(xmin)
    text_object_bndbox_ymin=dom.createTextNode(ymin)
    text_object_bndbox_xmax=dom.createTextNode(xmax)
    text_object_bndbox_ymax=dom.createTextNode(ymax)
    node_object_bndbox_xmin.appendChild(text_object_bndbox_xmin)
    node_object_bndbox_ymin.appendChild(text_object_bndbox_ymin)
    node_object_bndbox_xmax.appendChild(text_object_bndbox_xmax)
    node_object_bndbox_ymax.appendChild(text_object_bndbox_ymax)
    node_object_bndbox.appendChild(node_object_bndbox_xmin)
    node_object_bndbox.appendChild(node_object_bndbox_ymin)
    node_object_bndbox.appendChild(node_object_bndbox_xmax)
    node_object_bndbox.appendChild(node_object_bndbox_ymax)
    node_object.appendChild(node_object_name)
    node_object.appendChild(node_object_pose)
    node_object.appendChild(node_object_truncated)
    node_object.appendChild(node_object_difficult)
    node_object.appendChild(node_object_bndbox)
    node_annotation.appendChild(node_object)

    pascal_voc_xml=open(xml_filename,'w+')
    content=node_annotation.toprettyxml()
    pascal_voc_xml.writelines(content)
    pascal_voc_xml.close()

gts=open('blue_gt.txt','r')
bboxes=gts.readlines()
gts.close()
for bbox in bboxes:
    bbox=bbox.split()
    filename=bbox[0]
    xmin=bbox[1]
    ymin=bbox[2]
    xmax=bbox[3]
    ymax=bbox[4]
    width='640'
    height='480'
    depth='3'
    xml_filename='./annotations/'+filename.split('.')[0]+'.xml'
    pascal_voc_xml_trans(\
        xml_filename,\
        'armor',\
        filename,\
        'armor',\
        'armor',\
        'armor',\
        width,\
        height,\
        depth,\
        '0',\
        'armor',\
        'Unspecified',\
        '0',\
        '0',\
        xmin,\
        ymin,\
        xmax,\
        ymax
        )
