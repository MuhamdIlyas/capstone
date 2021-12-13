import * as tf from '@tensorflow/tfjs';

function main() {
    const buttonModal = document.getElementById("modalLabel");

    const buttonPredict = document.getElementById('predict');

    const model = tf.Sequential({
        layers: [
            tf.keras.layers.LSTM(60, input_shape=(None,1)),
            tf.keras.layers.Dense(40, activation='relu'),
            tf.keras.layers.Dense(20, activation='relu'),
            tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
        ]});
    
    
}



export default main;