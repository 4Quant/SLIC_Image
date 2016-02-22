from flask import Flask, jsonify
from glob import glob
from slic_generator import read_and_segment,create_all_area_tags
import json
import numpy as np # always gotta have it

app = Flask(__name__)
base_name = '/slic_generator'
base_img_dir = 'test_images'


class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray): # and obj.ndim == 1:
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('{}/list_images'.format(base_name), methods=['GET'])
def list_images():
    file_list = map(lambda x: x.split('/')[1],glob('{}/*.*g'.format(base_img_dir)))
    return jsonify({'images': file_list}),201

@app.route('{}/create_slic/<string:image_path>/<int:seg_size>'.format(base_name), methods=['GET'])
def create_slic(image_path,seg_size,sigma = 1.0, compactness = 1.0):
    all_im_data = read_and_segment('{}/{}'.format(base_img_dir,image_path), 
                                   segmentSize = seg_size, sigma = sigma, compactness = compactness, 
                                   max_iter = 100)
    (areaTags,areaDicts) = create_all_area_tags(all_im_data['image'],all_im_data['segments'])
    return json.dumps({'tags': areaTags, 'areas': areaDicts}, cls = NumpyAwareJSONEncoder), 201

@app.route('{}/grab_image/<string:image_path>'.format(base_name), methods=['GET'])
def grab_image(image_path):
    full_path = '{}/{}'.format(base_img_dir,image_path)
    data_uri = open(full_path, "rb").read().encode("base64").replace("\n", "")
    return jsonify({'data_url': "data:image/png;base64,{0}".format(data_uri)}),201
    
app.run(debug=True,host = '0.0.0.0', port = 5000, use_evalex=False)