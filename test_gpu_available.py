import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
print(f"GPU available: {len(gpus) > 0}")
print(f"Number of GPUs: {len(gpus)}")

tf.keras.mixed_precision.global_policy().compute_dtype