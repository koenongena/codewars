function fibonacci(n) {
    const cache = {};

    const _fibonacci = (n) => {
        if (n === 0 || n === 1) {
            return n;
        } else if (!cache[n]) {
            cache[n] = _fibonacci(n - 1) + _fibonacci(n - 2);
        }

        return cache[n];
    }

    return _fibonacci(n);
}

const evaluateMultiplicationsAndDivision = string => {
    const parts = string.trim().split(' ');
    return parts.reduce((acc, el, index) => {
        if (parts[index - 1] === '*') {
            return acc * el;
        } else if (parts[index - 1] === '/') {
            return acc / el;
        }
        return acc;
    });
};

const Calculator = function () {
    this.evaluate = string => {
        let s = string.trim();
        while (s.match(/(\d\.?\d*) [*/] (\d\.?\d*)/)) {
            console.log(s);
            s = s.replace(/(\d\.?\d*) ([*\/]) (\d\.?\d*)/, (x, a, operator, b) => {
                return operator === '*' ? a * b : a / b;
            })
        }

        return s
            .replace(/- (\d\.?\d*)+/g, "+ -$1")
            .split(' + ')
            .reduce((acc, el) => {
                return acc + parseFloat(el);
            }, 0);
    }

};

(() => {
    // console.log(fibonacci(70));

    const calculate = new Calculator();
    // console.log(calculate.evaluate('127'));
    // console.log(calculate.evaluate('2 + 3'));
    // console.log(calculate.evaluate('5 - 3 - 1'));
    // console.log(calculate.evaluate('9 - 3 * 8 / 2'));
    // console.log(calculate.evaluate('2 / 2 + 3 * 4 - 6'));
    // console.log(calculate.evaluate('31 / 37 / 91 * 37'));
    // console.log(calculate.evaluate('86 - 91 / 90 - 77 - 32'));
    // console.log(calculate.evaluate('93 / 85 * 66'));
    console.log(calculate.evaluate('10 * 5 / 2'));
    //
    // console.log(evaluateMultiplicationsAndDivision("31 / 37 / 91 * 37"))
})();
