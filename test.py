import tensorflow as tf

# Simple boolean check
gpu_available = tf.config.list_physical_devices('GPU')
print(f"GPU Available: {len(gpu_available) > 0}")
print(f"Number of GPUs: {len(gpu_available)}")