const timeSecond = document.getElementById('cnt-second');
const timeMilli = document.getElementById('cnt-milli');
const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');
const resetButton = document.getElementById('reset-button');

let seconds = 0;
let milliSeconds = 0;
let interval = 0;




startButton.addEventListener('click', ()=> {
    clearInterval(interval);
    interval = setInterval(setStart, 10);
})

stopButton.addEventListener('click', () => {
    clearInterval(interval);
    recordTime();
})

resetButton.addEventListener('click', ()=> {
    clearInterval(interval);
    

    seconds = 0;
    milliSeconds =0;
    timeSecond.innerText = '00';
    timeMilli.innerText = '00';
})

function setStart() {
    milliSeconds++;

    if (milliSeconds <= 9) {
        timeMilli.innerText = '0' +milliSeconds;
    }
    if (milliSeconds > 9) {
        timeMilli.innerText = milliSeconds;
    }

    if (milliSeconds > 99) {
        seconds++;
        if (seconds < 10) {
            timeSecond.innerText = '0'+seconds;
        } else {
            timeSecond.innerText = seconds;
        }
        
        milliSeconds = 0;
        timeMilli.innerText = '0' + milliSeconds;
    }
        
}

function recordTime() {

    const recordsContainer = document.querySelector('.records');
    const record = document.createElement('div')
    record.className = 'record-main';
    const recordButton = document.createElement('i');
    recordButton.className = 'button-side bi-circle';

    recordButton.addEventListener('click', ()=> {
        recordButton.classList.toggle('button-side bi-circle');
        recordButton.classList.toggle('bi bi-check-circle');
    })

    const recordSecond = document.createElement('div');
    recordSecond.className = 'record-second';
    const recordMilli = document.createElement('div');
    recordMilli.className = 'record-milli';

    record.appendChild(recordButton);
    record.appendChild(recordSecond);
    record.appendChild(recordMilli);

    //recordButton.classList('bi-circle');
    recordSecond.innerText = (seconds + ':');
    recordMilli.innerText = milliSeconds;
    console.log();
    recordsContainer.appendChild(record);



}

