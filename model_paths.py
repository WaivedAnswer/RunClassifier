

def get_model_path(relativePath):
    model_prepend = "models/"
    return model_prepend + relativePath


squeezePath = get_model_path("squeezenet_weights_tf_dim_ordering_tf_kernels.h5")
resPath = get_model_path("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
inceptionPath = get_model_path("inception_v3_weights_tf_dim_ordering_tf_kernels.h5")
resCocoPath = get_model_path("resnet50_coco_best_v2.0.1.h5")
densePath = get_model_path("DenseNet-BC-121-32.h5")
yoloTinyPath = get_model_path("yolo-tiny.h5")
yoloPath = get_model_path("yolo.h5")
holoPath = get_model_path("custom/hololens-ex-60--loss-2.76.h5")
holoConfigPath = get_model_path("custom/detection_config.json")
