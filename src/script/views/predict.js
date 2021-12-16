import * as tf from '@tensorflow/tfjs';

let input = document.querySelector('input');
let button = document.querySelector('button');
button.addEventListener('click', onClick);

let isModelLoaded = false;

let model;
async function init() {
    console.log('model loading....');
    model = undefined;
    model = await tf.loadLayersModel('https://raw.githubusercontent.com/muhamadilyas17/capstone/main/model/model.json');
    console.log('model loaded..');
}

// kategori air
const Water_Classes = {
    0:'Asam Sulfat',
    1:'Asam Sitrat',
    2:'Asam Askarbonat',
    3:'Asam Nitrat',
    4:'Asam Chlorogenic',
    5:'Asam Amino',
    6:'Air Netral',
    7:'Air Laut',
    8:'Natrium Bikarbonat',
    9:'Alkali',
    10:'Amonia',
    11:'Natrium',
    12:'Natrium Hipoklorit',
    13:'Natrium Hidroksida'
};

async function classify(btnPredict, spinnerGrow, classifiedIcon, classifiedName) {
    
    setTimeout(() => {
        spinnerGrow.classList.add('d-none');
        btnPredict.disabled = false;
        classifiedIcon.classList.remove('d-none');
        classifiedName.classList.remove('d-none');
    }, 3000);
}

function getInput() {
    const inputPH = document.getElementById('input');
    return inputPH.value;
}

function onClick() {
    if(!isModelLoaded) {
        alert('Model not loaded yet');
        return;
    }

    if(getInput() === '') {
        alert("Predict Can't be Null");
        document.getElementById('input').focus();
        return;
    }
}

export { init, classify}