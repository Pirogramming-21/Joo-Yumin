const submitButton = document.querySelector('.submit-button');
let maxAttempt = 9;
let randomNumbers = []; // randomNumbers 변수를 전역 범위에서 정의

create_random_number();

// 게임 초기화
submitButton.addEventListener('click', () => {
    if (check_numbers()) {
        maxAttempt--;
        console.log(`남은 시도 횟수: ${maxAttempt}`);
        if (maxAttempt === 0) {
            restartGame();
            create_random_number();    
        } 
    }
});

// 게임 재시작 함수
function restartGame() {
    maxAttempt = 9;
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    console.log(`남은 시도 횟수: ${maxAttempt}`);
}

// 중복되지 않는 3개의 랜덤한 숫자 생성 함수
function create_random_number() {
    const numbers = [];

    for (let i = 0; i < 9; i++) {
        numbers.push(i + 1);
    }

    randomNumbers = [];

    for (let n = 0; n < 3; n++) {
        const index = Math.floor(Math.random() * numbers.length);
        randomNumbers.push(numbers[index]);
        numbers.splice(index, 1);
    }

    console.log(randomNumbers);
}

// 숫자 입력 확인 함수
function check_numbers() {
    let inputNumber1 = parseInt(document.getElementById('number1').value);
    let inputNumber2 = parseInt(document.getElementById('number2').value);
    let inputNumber3 = parseInt(document.getElementById('number3').value);

    if (isNaN(inputNumber1) || isNaN(inputNumber2) || isNaN(inputNumber3)) {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return false;
    } 
    
    let resultHTML = contrast_numbers(inputNumber1, inputNumber2, inputNumber3);
    document.getElementById('container').innerHTML += resultHTML;

    if (resultHTML.includes('3 <div class="strike num-result">S</div>')) {
        document.getElementById('game-result-img').src = "success.png";
        document.getElementById('game-result-img').style.display = 'block';
        submitButton.disabled = true;
    }

    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    return true;
}

// 입력된 숫자와 정답을 비교하여 결과를 생성하는 함수
function contrast_numbers(inputNumber1, inputNumber2, inputNumber3) {
    let strikeNumbers = 0;
    let ballNumbers = 0;

    for (let i = 0; i < randomNumbers.length; i++) {
        if (randomNumbers[i] === inputNumber1 && i === 0 ||
            randomNumbers[i] === inputNumber2 && i === 1 ||
            randomNumbers[i] === inputNumber3 && i === 2) {
            strikeNumbers++;
        } else if (randomNumbers.includes(inputNumber1) && i !== 0 ||
        randomNumbers.includes(inputNumber2) && i !== 1 ||
        randomNumbers.includes(inputNumber3) && i !== 2) {
        ballNumbers++;
        }
    }

    return `
        <div class="check-result">
            <div class="left">${inputNumber1} ${inputNumber2} ${inputNumber3}</div>
            :
            <div class="right">
                ${strikeNumbers} <div class="strike num-result">S</div>
                ${ballNumbers - strikeNumbers} <div class="ball num-result">B</div>
                ${3 - (strikeNumbers + (ballNumbers - strikeNumbers))} <div class="out num-result">O</div>
            </div>
        </div>
    `;
}
