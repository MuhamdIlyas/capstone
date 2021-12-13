import * as tf from '@tensorflow/tfjs';

let model;
async function init() {
    console.log('model loading....');
    model = undefined;
    model = await tf.loadLayersModel()
}