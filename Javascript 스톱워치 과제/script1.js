const timeSecond = document.getElementById('cnt-second');
        const timeMilli = document.getElementById('cnt-milli');
        const startButton = document.getElementById('start-button');
        const stopButton = document.getElementById('stop-button');
        const resetButton = document.getElementById('reset-button');

        let seconds = 0;
        let milliSeconds = 0;
        let interval = 0;

        startButton.addEventListener('click', () => {
            clearInterval(interval);
            interval = setInterval(setStart, 10);
        });

        stopButton.addEventListener('click', () => {
            clearInterval(interval);
            recordTime();
        });

        resetButton.addEventListener('click', () => {
            clearInterval(interval);
            seconds = 0;
            milliSeconds = 0;
            timeSecond.innerText = '00';
            timeMilli.innerText = '00';
        });

        function setStart() {
            milliSeconds++;
            if (milliSeconds < 10) {
                timeMilli.innerText = '0' + milliSeconds;
            } else {
                timeMilli.innerText = milliSeconds;
            }

            if (milliSeconds > 99) {
                seconds++;
                if (seconds < 10) {
                    timeSecond.innerText = '0' + seconds;
                } else {
                    timeSecond.innerText = seconds;
                }

                milliSeconds = 0;
                timeMilli.innerText = '00';
            }
        }

        function recordTime() {
            const recordsContainer = document.getElementById('records');
            const records = document.createElement('div');
            record.className = 'record-main';

            const recordButton = document.createElement('div');
            recordButton.className = 'button-side bi bi-circle';
            recordButton.addEventListener('click', () => {
                recordButton.classList.toggle('bi-circle');
                recordButton.classList.toggle('bi-check-circle');
            });

            const recordSecond = document.createElement('div');
            recordSecond.className = 'record-second';
            const recordMilli = document.createElement('div');
            recordMilli.className = 'record-milli';

            if (seconds < 10) {
                recordSecond.innerText = '0' + seconds + ':';
            } else {
                recordSecond.innerText = seconds + ':';
            }
            if (milliSeconds < 10) {
                recordMilli.innerText = '0' + milliSeconds;
            } else {
                recordMilli.innerText = milliSeconds;
            }

            record.appendChild(recordButton);
            record.appendChild(recordSecond);
            record.appendChild(recordMilli);

            recordsContainer.appendChild(records);
        }