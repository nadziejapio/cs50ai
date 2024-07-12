At first I am trying to compile sequential model with:
    1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Flatten layer
    4) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    5) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
        accuracy: 0.0558 - loss: 3.4942


II try:
     1) Convolutional layer
        - 64 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Flatten layer
    4) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    5) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
        accuracy: 0.0576 - loss: 3.5026

III try:
     1) Convolutional layer
        - 64 (3, 3)
        - activation = "tanh"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Flatten layer
    4) Hidden layer 
        - Dense (128, activation="tanh")
        - Dropout (0.5)
    5) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.0512 - loss: 3.5192

IV try:
     1) Convolutional layer
        - 64 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 64 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    7) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.8114 - loss: 0.6166

V try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    7) Hidden layer 
        - Dense (128, activation="relu")
        - Dropout (0.5)
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9240 - loss: 0.2869

VI try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (128, activation="relu")
    7) Hidden layer 
        - Dense (128, activation="relu")
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9506 - loss: 0.2486


VII try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (64, activation="relu")
    7) Hidden layer 
        - Dense (64, activation="relu")
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9574 - loss: 0.2153

VIII try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(4, 4)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (64, activation="relu")
    7) Hidden layer 
        - Dense (64, activation="relu")
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.7843 - loss: 0.7400

IX try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (64, activation="relu")
        - Dropout (0.2)
    7) Hidden layer 
        - Dense (64, activation="relu")
        - Dropout (0.2)
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9429 - loss: 0.2099

X try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (512, activation="relu")
        - Dropout (0.2)
    7) Hidden layer 
        - Dense (512, activation="relu")
        - Dropout (0.2)
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9270 - loss: 0.2988

XI try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (32, activation="relu")
        - Dropout (0.2)
    7) Hidden layer 
        - Dense (32, activation="relu")
        - Dropout (0.2)
    8) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.4043 - loss: 1.7530

XII try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (32, activation="relu")
        - Dropout (0.2)
    7) Hidden layer 
        - Dense (32, activation="relu")
        - Dropout (0.2)
    8) Hidden layer 
        - Dense (32, activation="relu")
        - Dropout (0.2)
    9) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.0559 - loss: 3.5008

XIII try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (64, activation="relu")
        - Dropout (0.2)
    7) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9627 - loss: 0.1458

XIV try:
     1) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    2) Pooling layer
        - pool_size=(2, 2)
    3) Convolutional layer
        - 32 (3, 3)
        - activation = "relu"
        - input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    4) Pooling layer
        - pool_size=(2, 2)
    5) Flatten layer
    6) Hidden layer 
        - Dense (1024, activation="relu")
        - Dropout (0.2)
    7) Output layer
        - Dense(NUM_CATEGORIES, activation="softmax")
    
    Compiled with:
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]

    **Result**
       accuracy: 0.9384 - loss: 0.3337


**CONCLUSION**
    Best results I got with only one hidden layer, with 2^n dense, with small dropout.
    Small Dense can cause  incredibly low accuracy. High dense, doesn't affect accuracy that much. It was needed to add convulation layer and pooling layer two times to image conversion part to get good results.
    Bigger amount of hidden layers caused smaller accuracy.
    Some of tries had accuracy ~5% and I think it was not dependend on the model settings.