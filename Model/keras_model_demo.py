import keras
from keras.utils import plot_model

"""example multi-input model from keras
"""

# image inputs
image_inputs = keras.layers.Input(shape=(5,), name='image_input')
# feature inputs
feature_inputs = keras.layers.Input(shape=(6,), name='feature_input')

# image processing layer
image_1 = keras.layers.Dense(10, name='image_1')(image_inputs)

# concatenation layer, joins the features and image layer
combined = keras.layers.concatenate([image_1, feature_inputs], name='concatenate')

# one more processing layer, and then output
process = keras.layers.Dense(20, name='process')(combined)
output = keras.layers.Dense(9, name='output')(process)

# models based on whole thing (model) and part of the thing (model2)
model = keras.Model([image_inputs, feature_inputs], output)
model2 = keras.Model(image_inputs, image_1)

# plot the models 
plot_model(model, to_file='test.png', show_shapes=True)
plot_model(model2, to_file='test2.png', show_shapes=True)
