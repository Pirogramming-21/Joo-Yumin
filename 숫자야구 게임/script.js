const submitButton = document.querySelector('.submit-button');
let maxAttempt = 9;
let randomNumbers = [];

create_random_number();
console.log(`남은 시도 횟수: ${maxAttempt}`);
console.log(randomNumbers);

// 게임 초기화
submitButton.addEventListener('click', () => {
    if (check_numbers()) {
        maxAttempt--;
        console.log(`남은 시도 횟수: ${maxAttempt}`);
        if (maxAttempt === 0) {
            document.getElementById('game-result-img').src = "fail.png";
            document.getElementById('game-result-img').style.display = 'block';
        } 
    }
});

// 게임 재시작 함수
function restartGame() {
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    document.getElementById('container').innerHTML = ''; // 결과 창 초기화
    submitButton.disabled = false; // 버튼 활성화
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
        submitButton.disabled = true; // 버튼 비활성화
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

    // 정답 숫자가 위치와 관계없이 포함되어 있는지 확인하여 볼 수를 계산
    if (randomNumbers.includes(inputNumber1)) ballNumbers++;
    if (randomNumbers.includes(inputNumber2)) ballNumbers++;
    if (randomNumbers.includes(inputNumber3)) ballNumbers++;

    // 스트라이크 계산
    if (randomNumbers[0] === inputNumber1) strikeNumbers++;
    if (randomNumbers[1] === inputNumber2) strikeNumbers++;
    if (randomNumbers[2] === inputNumber3) strikeNumbers++;

    // 결과 HTML을 생성하여 반환
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
